# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.memoize import ram
from plone.principalsource.source import PrincipalSource
from time import time
from zope.globalrequest import getRequest
from zope.i18n import translate
from zope.interface import implements
from zope.schema.interfaces import IContextSourceBinder

from cpskin.citizen import _
from cpskin.citizen import utils


@ram.cache(lambda *args: time() // (60 * 60))
def get_users():
    users = api.user.get_users(groupname="Citizens")
    return [user.id for user in users]


class CitizensSource(PrincipalSource):
    def __init__(self, context):
        super(CitizensSource, self).__init__(context)

    def _search(self, id=None, exact_match=True):
        users = get_users()
        if id is not None:
            return [{"id": user_id} for user_id in users if user_id == id]
        return [{"id": user_id} for user_id in users]


class CitizensSourceBinder(object):
    """Bind the principal source with either users or groups"""

    implements(IContextSourceBinder)

    def __call__(self, context):
        return CitizensSource(context)


CitizensVocabulary = CitizensSourceBinder()


class CitizensPortalTypesVocabularyFactory(object):
    def __call__(self, context):
        portal_types = api.portal.get_tool("portal_types")
        content = {
            k: v.title
            for k, v in portal_types.items()
            if k in utils.citizen_access_portal_types()
        }
        return utils.dict_2_vocabulary(content)


CitizensPortalTypesVocabulary = CitizensPortalTypesVocabularyFactory()


class CitizensAllowedCreationTypesVocabularyFactory(object):
    def _translate(self, msgid):
        request = getRequest()
        translation = translate(msgid, context=request)
        return translation.encode("utf-8")

    def __call__(self, context):
        portal_types = api.portal.get_tool("portal_types")
        content = {}
        for k, v in portal_types.items():
            if k not in utils.get_allowed_creation_types():
                continue
            title = self._translate(_(v.title))
            if v.description:
                description = self._translate(_(v.description))
                content[k] = "{0}  ({1})".format(title, description)
            else:
                content[k] = title
        return utils.dict_2_vocabulary(content)


CitizensAllowedCreationTypesVocabulary = CitizensAllowedCreationTypesVocabularyFactory()


class CitizensActionsVocabularyFactory(object):
    def __call__(self, context):
        return utils.dict_2_vocabulary({
            u"allow-management": _(u"Allow management"),
            u"awaiting-for-approval": _(u"Awaiting for approval"),
        })


CitizensActionsVocabulary = CitizensActionsVocabularyFactory()
