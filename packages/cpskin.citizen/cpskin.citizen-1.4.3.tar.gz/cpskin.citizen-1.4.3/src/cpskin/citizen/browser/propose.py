# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from datetime import datetime
from plone import api
from plone.z3cform.layout import FormWrapper
from z3c.form import button
from z3c.form import field
from z3c.form.browser.radio import RadioFieldWidget
from z3c.form.form import Form
from zExceptions import Unauthorized
from zope import schema
from zope.interface import Interface
from zope.schema.vocabulary import getVocabularyRegistry

from cpskin.citizen import _
from cpskin.citizen import utils


class IProposeCitizenContent(Interface):

    type = schema.Choice(
        title=_(u"Portal Type"),
        vocabulary="cpskin.citizen.allowed_creation_portal_types",
        required=True,
    )

    title = schema.TextLine(title=_(u"Title"), required=True)


class ProposeCitizenForm(Form):
    fields = field.Fields(IProposeCitizenContent)
    action = "@@propose-citizen"
    ignoreContext = True
    fields["type"].widgetFactory = RadioFieldWidget

    @button.buttonAndHandler(_(u"Confirm"))
    def handleApply(self, action):
        self.current_user = api.user.get_current()
        data, errors = self.extractData()
        if errors or self.is_citizen is False:
            raise Unauthorized(u"Cannot propose a content")
        container = utils.get_creation_folder(
            self.context, self.request, data.get("type")
        )
        fields = self.get_required_fields(data.get("type"))
        vr = getVocabularyRegistry()
        default_values = {}
        for k, f in fields:
            if isinstance(f.field, schema.Datetime):
                default_values[k] = datetime.now()
            elif isinstance(f.field, schema.Choice):
                voc = vr.get(container, f.field.vocabularyName)
                default_values[k] = voc.by_value.values()[0].value
        data.update(default_values)
        content = self.create_original(container, **data)
        self.create_draft(content)
        return

    @property
    def is_citizen(self):
        if api.user.is_anonymous() is True:
            return False
        return utils.is_citizen(self.current_user)

    def create_original(self, container, **kwargs):
        content = utils.execute_under_unrestricted_user(
            api.portal.get(), api.content.create, "admin", container=container, **kwargs
        )
        content.citizens = [self.current_user.id]
        return content

    def create_draft(self, content):
        url = "{0}/@@edit-citizen".format(content.absolute_url())
        self.request.response.redirect(url)

    def get_required_fields(self, portal_type):
        ignored_fields = ("title",)

        fields = utils.get_required_fields(portal_type)
        fields = [
            (k, f)
            for k, f in fields
            if f.field.default is None and k not in ignored_fields
        ]
        return fields


class ProposeCitizenView(FormWrapper):
    form = ProposeCitizenForm

    def links(self):
        """Return the creation folders links"""
        folders = [
            utils.get_creation_folder(self.context, self.request, e)
            for e in utils.get_allowed_creation_types()
        ]
        return [{"href": p.absolute_url(), "title": p.Title()} for p in folders]
