# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from imio.actionspanel.browser.views import ActionsPanelView
from plone import api
from plone.app.stagingbehavior.utils import get_working_copy

from cpskin.citizen import utils


class ActionsView(ActionsPanelView):
    def __call__(self, *args, **kwargs):
        self.SECTIONS_TO_RENDER = ("render_citizen_actions",)
        self.working_copy = get_working_copy(aq_inner(self.context))
        return super(ActionsView, self).__call__(*args, **kwargs)

    def render_citizen_actions(self):
        """Render citizen actions"""
        return ViewPageTemplateFile("templates/actions_panel_citizen.pt")(self)

    @property
    def can_edit(self):
        return utils.can_edit_citizen(api.user.get_current(), self.context)

    @property
    def has_draft(self):
        return self.working_copy is not None

    @property
    def draft_url(self):
        return self.working_copy.absolute_url()
