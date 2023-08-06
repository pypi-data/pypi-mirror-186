# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from plone import api
from plone.app.stagingbehavior.browser import control

from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess


class DefaultControl(control.Control):
    def return_allowed(self):
        return False


class Control(control.Control):
    def checkout_allowed(self):
        """ Check if a checkout is allowed """
        context = aq_inner(self.context)
        if super(Control, self).checkout_allowed() is False:
            return False
        if ICitizenAccess.providedBy(context):
            current_user = api.user.get_current()
            if utils.is_citizen(current_user):
                return utils.can_edit_citizen(current_user, context)
        return True

    def cancel_allowed(self):
        """Check if a checkout cancel is allowed"""
        context = aq_inner(self.context)
        if ICitizenAccess.providedBy(context):
            current_user = api.user.get_current()
            if utils.is_citizen(current_user):
                return utils.can_edit_citizen(current_user, context)
        return self.return_allowed()

    def return_allowed(self):
        """Check if a return checkout is allowed"""
        return super(Control, self).cancel_allowed()
