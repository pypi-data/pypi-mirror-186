# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.z3cform.select2.widget.widget import MultiSelect2FieldWidget
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.autoform import directives as form
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface

from cpskin.citizen import _


class ISettings(Interface):

    proposal_folders = schema.Dict(
        title=_(u"Proposal default folders"),
        description=_(
            u"The folders where (by default) new content proposed "
            u"by citizens will be created"
        ),
        key_type=schema.Choice(
            title=_(u"Content type"),
            vocabulary="cpskin.citizen.portal_types",
            required=True,
        ),
        value_type=schema.TextLine(
            title=_(u"Default folder"),
            description=_(
                u"Path to the folder from the navigation root "
                u"(should not contains the language folder)"
            ),
            required=True,
        ),
        required=False,
    )

    form.widget(claim_types=MultiSelect2FieldWidget)
    claim_types = schema.List(
        title=_(u"Claim content types"),
        description=_(u"Allowed content types for the claim procedure"),
        value_type=schema.Choice(
            title=_(u"Claim content types"), vocabulary="cpskin.citizen.portal_types"
        ),
        required=False,
    )

    form.widget(creation_types=MultiSelect2FieldWidget)
    creation_types = schema.List(
        title=_(u"Creation content types"),
        description=_(
            u"Allowed content types for creation by citizens "
            u"(by default all content types are allowed)"
        ),
        value_type=schema.Choice(
            title=_(u"Claim content types"), vocabulary="cpskin.citizen.portal_types"
        ),
        required=False,
    )

    form.widget(creation_types=MultiSelect2FieldWidget)
    map_view_types = schema.List(
        title=_(u"Map view content types"),
        description=_(
            u"Visibled content types for map view for citizens "
            u"(by default no content types are allowed)"
        ),
        value_type=schema.Choice(
            title=_(u"Map view content types"),
            vocabulary="plone.app.vocabularies.PortalTypes",
        ),
        required=False,
    )

    form.widget(creation_types=MultiSelect2FieldWidget)
    published_states = schema.List(
        title=_(u"Published states"),
        description=_(u"List of object states that can be assimilate to published"),
        value_type=schema.Choice(
            title=_(u"states"),
            vocabulary="plone.app.vocabularies.WorkflowStates",
        ),
        required=False,
    )

    manager_email = schema.TextLine(
        title=_(u"Email address of persons that manage citizen contents"),
        description=_(
            u"If there are multiple email addresses, separate them with semicolons"
        ),
    )


class SettingsEditForm(RegistryEditForm):
    schema = ISettings
    label = u"CPSkin Citizen settings"


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)
