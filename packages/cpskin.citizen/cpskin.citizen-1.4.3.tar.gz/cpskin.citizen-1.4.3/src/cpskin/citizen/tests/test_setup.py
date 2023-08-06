# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from cpskin.citizen.testing import CPSKIN_CITIZEN_INTEGRATION_TESTING
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    layer = CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if cpskin.citizen is installed."""
        self.assertTrue(self.installer.isProductInstalled("cpskin.citizen"))

    def test_browserlayer(self):
        """Test that ICpskinCitizenLayer is registered."""
        from cpskin.citizen.interfaces import ICpskinCitizenLayer
        from plone.browserlayer import utils

        self.assertIn(ICpskinCitizenLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    layer = CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")
        self.installer.uninstallProducts(["cpskin.citizen"])

    def test_product_uninstalled(self):
        """Test if cpskin.citizen is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("cpskin.citizen"))
