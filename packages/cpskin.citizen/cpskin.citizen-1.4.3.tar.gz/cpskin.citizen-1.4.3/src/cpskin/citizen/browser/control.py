# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView
from plone import api

from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess


class CitizenControl(BrowserView):
    def __init__(self, *args, **kwargs):
        super(CitizenControl, self).__init__(*args, **kwargs)
        self.is_anonymous = api.user.is_anonymous()
        self.current_user = api.user.get_current()

    def is_citizen(self):
        """Check if the current user is a citizen"""
        if self.is_anonymous:
            return False
        return utils.is_citizen(self.current_user)

    def is_admin(self):
        """Check if the current user can administrate citizen contents"""
        if self.is_anonymous:
            return False
        allowed_roles = ["Editor", "Manager", "Reviewer", "Site Administrator"]
        user_roles = api.user.get_roles(user=self.current_user)
        return len([r for r in user_roles if r in allowed_roles]) > 0

    def is_citizen_content(self):
        """Check if the current content can be administrated by citizen"""
        return ICitizenAccess.providedBy(self.context)
