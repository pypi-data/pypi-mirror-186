# -*- coding: utf-8 -*-

from plone import api
from plone.registry import Record
from plone.registry import field
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from eea.facetednavigation.layout.interfaces import IFacetedLayout

import os


def upgrade_faceted_dashboard_config(
    context, layout=None, config_path="dashboard/faceted_config.xml"
):
    context.restrictedTraverse("@@faceted_settings").toggle_left_column()
    if layout is not None:
        IFacetedLayout(context).update_layout(layout)
    config_xml = os.path.join(os.path.dirname(__file__), config_path)
    context.unrestrictedTraverse("@@faceted_exportimport").import_xml(
        import_file=open(config_xml, "r")
    )


def upgrade_citizen_draft_folder(context):
    portal = api.portal.get()
    # Create the draft folder for each language
    lrfs = api.content.find(context=portal, portal_type="LRF")
    lrfs = [e.getObject() for e in lrfs]
    if not lrfs:
        lrfs = [api.portal.get_navigation_root(portal)]
    for folder in lrfs:
        if u"citizen-drafts" in folder:
            api.content.disable_roles_acquisition(obj=folder["citizen-drafts"])


def upgrade_to_1002(context):
    """
    - Add cpskin.citizen.browser.settings.ISettings.published_states record
    - Add is_citizen_content index
    - Add citizen_action index
    """
    setup_tool = api.portal.get_tool(name="portal_setup")
    setup_tool.runImportStepFromProfile("profile-cpskin.citizen:default", "catalog")

    brains = api.content.find(object_provides=u"cpskin.citizen.behavior.ICitizenAccess")
    for brain in brains:
        if brain.has_claim or brain.validation_required:
            brain.getObject().reindexObject()

    registry = getUtility(IRegistry)
    records = registry.records

    if "cpskin.citizen.browser.settings.ISettings.published_states" in records:
        return

    record = Record(
        field.List(
            title=u"Published states",
            description=u"List of object states that can be assimilate to published",
            value_type=field.Choice(
                title=u"states", vocabulary="plone.app.vocabularies.WorkflowStates"
            ),
        ),
        value=[
            u"active",
            u"published",
            u"published_and_shown",
            u"published_and_hidden",
        ],
    )
    records["cpskin.citizen.browser.settings.ISettings.published_states"] = record


def upgrade_to_1003(context):
    portal = api.portal.get()
    lrfs = api.content.find(context=portal, portal_type="LRF")
    lrfs = [(e.getObject(), e.id) for e in lrfs]
    if not lrfs:
        lrfs = [
            (api.portal.get_navigation_root(portal), api.portal.get_default_language())
        ]
    for folder, lng in lrfs:
        if u"citizen-dashboard" not in folder:
            # This happen if cpskin.citizen was not correctly configured
            continue
        dashboard_folder = folder[u"citizen-dashboard"]
        if "admin-claims" in dashboard_folder:
            api.content.delete(dashboard_folder["admin-claims"])
        if "admin-content" in dashboard_folder:
            upgrade_faceted_dashboard_config(
                dashboard_folder["admin-content"],
                config_path="dashboard/faceted_admin_config.xml",
            )
    setup_tool = api.portal.get_tool(name="portal_setup")
    setup_tool.runImportStepFromProfile("profile-cpskin.citizen:default", "actions")


def upgrade_to_1004(context):
    """
    - Add cpskin.citizen.browser.settings.ISettings.manager_email record
    """
    registry = getUtility(IRegistry)
    records = registry.records

    if "cpskin.citizen.browser.settings.ISettings.manager_email" in records:
        return

    record = Record(
        field.TextLine(
            title=u"Email address of persons that manage citizen contents",
            description=(
                u"If there are multiple email addresses, separate them with semicolons"
            ),
        ),
        value=u"",
    )
    records["cpskin.citizen.browser.settings.ISettings.manager_email"] = record
