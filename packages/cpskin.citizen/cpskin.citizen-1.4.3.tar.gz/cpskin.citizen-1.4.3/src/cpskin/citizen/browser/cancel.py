# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.iterate.browser.cancel import Cancel

from cpskin.citizen import utils


class CancelCitizenView(Cancel):
    def __call__(self):
        if "form.button.Cancel" in self.request.form:
            current_user = api.user.get_current()
            if utils.can_edit(current_user, self.context):
                return super(CancelCitizenView, self).__call__()
            else:
                return self._unrestricted_call(current_user)
        else:
            return super(CancelCitizenView, self).__call__()

    def _unrestricted_call(self, current_user):
        return utils.execute_under_unrestricted_user(
            api.portal.get(),
            super(CancelCitizenView, self).__call__,
            current_user.id,
        )
