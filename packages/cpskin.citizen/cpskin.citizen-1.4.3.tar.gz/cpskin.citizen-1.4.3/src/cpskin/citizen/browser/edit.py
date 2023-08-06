# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.statusmessages.interfaces import IStatusMessage
from plone import api
from plone.app.stagingbehavior.utils import get_baseline
from plone.app.stagingbehavior.utils import get_working_copy
from plone.dexterity.browser.edit import DefaultEditForm
from plone.dexterity.events import EditFinishedEvent
from plone.dexterity.i18n import MessageFactory as DX_MF
from plone.dexterity.interfaces import IDexterityEditForm
from plone.z3cform import layout
from z3c.form import button
from zope.event import notify
from zope.interface import classImplements

from cpskin.citizen import utils


class EditCitizenForm(DefaultEditForm):
    _allowed_fieldsets = ["address", "contact_details", "schedule", "images"]

    @button.buttonAndHandler(DX_MF(u"Save"), name="save")
    def handleApply(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        current_user = api.user.get_current()
        if utils.can_edit(current_user, self.context):
            self.applyChanges(data)
        else:
            utils.execute_under_unrestricted_user(
                api.portal.get(), self.applyChanges, current_user.id, data
            )
        IStatusMessage(self.request).addStatusMessage(
            DX_MF(u"Changes saved"), "info success"
        )
        self.request.response.redirect(self.nextURL())
        notify(EditFinishedEvent(self.context))

    def update_groups(self):
        self.groups = tuple(
            [g for g in self.groups if g.__name__ in self._allowed_fieldsets]
        )

    def update(self):
        super(EditCitizenForm, self).update()
        self.update_groups()

    def extractData(self):
        self.update_groups()
        return super(EditCitizenForm, self).extractData()


DefaultEditView = layout.wrap_form(EditCitizenForm)
classImplements(DefaultEditView, IDexterityEditForm)


class EditCitizenView(DefaultEditView):
    def update(self):
        original = get_baseline(self.context)
        working_copy = get_working_copy(original)
        if original is None or self.context == original:
            url = "{0}/@@content-checkout".format(self.context.absolute_url())
            if working_copy is not None:
                url = "{0}/@@edit-citizen".format(working_copy.absolute_url())
            self.request.response.redirect(url)
            return
        super(EditCitizenView, self).update()
