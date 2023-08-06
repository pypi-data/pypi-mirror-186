# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from borg.localrole.interfaces import ILocalRoleProvider
from zope.interface import implements
from plone import api

from cpskin.citizen import utils
from cpskin.citizen.dashboard.interfaces import IAdminDashboard


class DashboardLocalRoleAdapter(object):
    implements(ILocalRoleProvider)

    def __init__(self, context):
        self.context = context
        current_user = api.user.get_current()
        self.is_citizen = utils.is_citizen(current_user)

    def getRoles(self, principal):
        """Grant permission for principal"""
        if IAdminDashboard.providedBy(self.context) or not self.is_citizen:
            return []
        return ("Reader",)

    def getAllRoles(self):
        """Grant permissions"""
        if IAdminDashboard.providedBy(self.context) or not self.is_citizen:
            yield ("", ("",))
            raise StopIteration
        yield ("Citizens", "Reader")
