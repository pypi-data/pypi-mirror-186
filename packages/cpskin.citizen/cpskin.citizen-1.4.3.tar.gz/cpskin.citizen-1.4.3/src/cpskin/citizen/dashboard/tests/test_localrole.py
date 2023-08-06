# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.testing import login
from plone.app.testing import logout

from cpskin.citizen import testing


class TestLocalRole(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def test_role_on_admin_dashboard(self):
        """Test the local roles on an admin dashboard"""
        manager = api.user.get("manager")
        roles = api.user.get_roles(user=manager, obj=self.dashboards["admin-content"])
        self.assertNotIn("Reader", roles)

        login(self.portal, "citizen")
        citizen = api.user.get("citizen")
        roles = api.user.get_roles(user=citizen, obj=self.dashboards["admin-content"])
        self.assertNotIn("Reader", roles)
        logout()

    def test_role_on_citizen_dashboard(self):
        """Test the local roles on a citizen dashboard"""
        manager = api.user.get("manager")
        roles = api.user.get_roles(user=manager, obj=self.dashboards["citizen-content"])
        self.assertNotIn("Reader", roles)

        login(self.portal, "citizen")
        citizen = api.user.get("citizen")
        roles = api.user.get_roles(user=citizen, obj=self.dashboards["citizen-content"])
        self.assertIn("Reader", roles)
        logout()
