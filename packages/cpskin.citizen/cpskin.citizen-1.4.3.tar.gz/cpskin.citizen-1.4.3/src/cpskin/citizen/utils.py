# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from AccessControl import getSecurityManager
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import setSecurityManager
from AccessControl.User import UnrestrictedUser as BaseUnrestrictedUser
from persistent.dict import PersistentDict
from plone import api
from plone.app.linkintegrity.exceptions import LinkIntegrityNotificationException
from plone.app.stagingbehavior.utils import get_baseline  # noqa API
from plone.app.stagingbehavior.utils import get_relations  # noqa API
from plone.app.stagingbehavior.utils import get_working_copy as get_wc
from plone.dexterity import utils
from plone.registry.interfaces import IRegistry
from z3c.form import field
from zc.relation.interfaces import ICatalog
from zope.annotation import IAnnotations
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.schema.vocabulary import SimpleVocabulary

from cpskin.citizen import ANNOTATION_KEY
from cpskin.citizen.behavior import ICitizenAccess
from cpskin.citizen.browser.settings import ISettings
from cpskin.citizen.interfaces import ICitizenCreationFolder


DRAFT_FOLDER_ID = "citizen-drafts"
DASHBOARD_FOLDER_ID = "citizen-dashboard"
DASHBOARD_FOLDERS_IDS = (
    "citizen-content",
    "citizen-claims",
    "citizen-map",
    "citizen-propose-content",
    "admin-content",
)


def citizen_access_portal_types():
    """Return the portal types where the CitizenAccess is active"""
    portal_types = api.portal.get_tool("portal_types")
    types = []
    cls = cls_fullpath(ICitizenAccess)
    for portal_type in portal_types:
        if cls in getattr(portal_types[portal_type], "behaviors", []):
            types.append(portal_type)
    return types


def cls_fullpath(cls):
    """Return the complete path of a class"""
    return u"{module}.{classname}".format(module=cls.__module__, classname=cls.__name__)


class UnrestrictedUser(BaseUnrestrictedUser):
    """Unrestricted user that still has an id."""

    def getId(self):
        """Return the ID of the user."""
        return self.getUserName()


def execute_under_unrestricted_user(portal, function, user, *args, **kwargs):
    """
    Execute code under unrestricted user privileges.

    Example how to call::

        execute_under_unrestricted_user(
            portal,
            doSomeNormallyNotAllowedStuff,
            "admin",
            source_folder,
            target_folder,
        )

    @param portal: Reference to ISiteRoot object whose access controls we are using
    @param function: Method to be called with special privileges
    @param user: User to use for special privileges
    @param args: Passed to the function
    @param kwargs: Passed to the function
    """
    sm = getSecurityManager()
    try:
        try:
            # Create new temporary unrestricted user using the current user ID
            # Note that the username (getId()) is left in exception
            # tracebacks in the error_log,
            # so it is an important thing to store.
            tmp_user = UnrestrictedUser(user, "", [""], "")
            # Wrap the user in the acquisition context of the portal
            tmp_user = tmp_user.__of__(portal.acl_users)
            newSecurityManager(None, tmp_user)
            # Call the function
            return function(*args, **kwargs)
        except LinkIntegrityNotificationException as e:
            raise e
        except:  # noqa
            # If special exception handlers are needed, run them here
            pass
    finally:
        # Restore the old security manager
        setSecurityManager(sm)


def can_edit(user, context):
    """
    Verify if the given user have the 'Modify portal content' permission
    on the given context
    """
    if api.user.is_anonymous():
        return False
    if is_citizen(user):
        return False
    return api.user.has_permission(
        "Modify portal content", user=user, obj=context
    ) or api.user.has_permission("Copy or Move", user=user, obj=context)


def can_edit_citizen(user, context):
    """
    Verify if the given user have the 'Modify citizen content' permission
    on the given context
    """
    if api.user.is_anonymous():
        return False
    return api.user.has_permission("Modify citizen content", user=user, obj=context)


def is_citizen(user):
    """
    Verify if the given user is a citizen (member of the Citizens group)
    """
    if api.user.is_anonymous():
        return False
    user_groups = api.group.get_groups(user=user)
    # In some usecase, the group can be `None`
    return "Citizens" in [g.id for g in user_groups if g]


def can_claim(user, context):
    """Verify if the given user can claim the given context"""
    if can_edit_citizen(user, context) is True:
        return False
    if not is_citizen(user):
        return False
    return context.portal_type in get_allowed_claim_types()


def have_claimed(user, context):
    """Verify if the given user alredy claimed the given context"""
    return user.id in get_claim_users(context)


def get_claim_users(context):
    """Return the users that have claimed the given context"""
    claims = get_annotations(context).get("claim", [])
    return [isinstance(e, str) and e or e[0] for e in claims]


def get_draft_folder(context):
    """Return the citizen draft folder for the given context (object)"""
    navigation_root = api.portal.get_navigation_root(context)
    folder = navigation_root[DRAFT_FOLDER_ID]
    if context.portal_type not in allowed_content_types(folder):
        return context.aq_parent
    return folder


def allowed_content_types(context):
    """Return the ids of the allowed content types for the given context"""
    return [
        p.id
        for p in execute_under_unrestricted_user(
            context, context.allowedContentTypes, ""
        )
    ]


def dict_2_vocabulary(dictionary):
    """Transform a dictionary into a vocabulary"""
    terms = [SimpleVocabulary.createTerm(k, k, v) for k, v in dictionary.items()]
    return SimpleVocabulary(terms)


def get_settings():
    return getUtility(IRegistry).forInterface(ISettings)


def get_creation_folder(context, request, portal_type):
    """Return the creation folder for a proposal from a citizen"""
    navigation_root = api.portal.get_navigation_root(context)
    adapter = queryMultiAdapter(
        (context, request), ICitizenCreationFolder, name=portal_type
    )
    if adapter:
        return adapter.get_folder(navigation_root, portal_type)
    adapter = getMultiAdapter((context, request), ICitizenCreationFolder)
    return adapter.get_folder(navigation_root, portal_type)


def get_allowed_creation_types():
    settings = get_settings()
    allowed_types = settings.creation_types
    if not allowed_types:
        allowed_types = citizen_access_portal_types()
    return allowed_types


def get_allowed_claim_types():
    settings = get_settings()
    claim_types = settings.claim_types
    if not claim_types:
        claim_types = citizen_access_portal_types()
    return claim_types


def get_annotations(context):
    annotations = IAnnotations(context)
    if ANNOTATION_KEY not in annotations:
        annotations[ANNOTATION_KEY] = PersistentDict()
    return annotations[ANNOTATION_KEY]


def get_required_fields(portal_type):
    """Return the required fields for a given dexterity portal type"""
    schemas = utils.iterSchemataForType(portal_type)
    fields = []
    for schema in schemas:
        fields.extend(
            [(k, f) for k, f in field.Fields(schema).items() if f.field.required]
        )
    return fields


def iterate_claims(claims):
    """Backward compatibility method for claims without reason"""
    for claim in claims:
        if isinstance(claim, tuple):
            yield claim
        else:
            yield (claim, "")


def get_claims(context):
    annotations = get_annotations(context)
    if "claim" not in annotations:
        return []
    return iterate_claims(annotations["claim"])


def add_claim(context, user_id, reason):
    annotations = get_annotations(context)
    if "claim" not in annotations:
        annotations["claim"] = []
    if user_id not in [e[0] for e in iterate_claims(annotations["claim"])]:
        annotations["claim"].append((user_id, reason))
        annotations._p_changed = True
        context.reindexObject()


def remove_claim(context, user_id):
    annotations = get_annotations(context)
    annotations["claim"] = [
        e for e in iterate_claims(annotations["claim"]) if e[0] != user_id
    ]
    annotations._p_changed = True
    context.reindexObject()


def remove_relation(obj):
    catalog = getUtility(ICatalog)
    for relation in get_relations(obj):
        if relation.to_object is None:
            catalog.unindex(relation)


def get_working_copy(obj):
    try:
        return get_wc(obj)
    except KeyError:  # This happen if a link is broken
        return


def has_claim(obj):
    """Check if the given object has awaiting claims"""
    if obj != get_working_copy(obj):
        annotations = get_annotations(obj)
        return len(annotations.get("claim", [])) > 0
    return False


def validation_required(obj):
    """Check if the given object is awaiting for validation"""
    if obj == get_working_copy(obj):
        annotations = get_annotations(obj)
        return annotations.get("validation_required", False)
    return False
