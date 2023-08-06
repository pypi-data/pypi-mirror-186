# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api

from cpskin.citizen import testing


class TestLocalRole(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def test_role_on_regular_document(self):
        """Test the local roles on a document with no citizens"""
        manager = api.user.get("manager")
        roles = api.user.get_roles(user=manager, obj=self.document)
        self.assertNotIn("Citizen Editor", roles)

        citizen = api.user.get("citizen")
        roles = api.user.get_roles(user=citizen, obj=self.document)
        self.assertNotIn("Citizen Editor", roles)

    def test_role_on_citizen_document(self):
        """Test the local roles on a document with citizens"""
        manager = api.user.get("manager")
        roles = api.user.get_roles(user=manager, obj=self.citizen_document)
        self.assertNotIn("Citizen Editor", roles)

        citizen = api.user.get("citizen")
        roles = api.user.get_roles(user=citizen, obj=self.citizen_document)
        self.assertIn("Citizen Editor", roles)
