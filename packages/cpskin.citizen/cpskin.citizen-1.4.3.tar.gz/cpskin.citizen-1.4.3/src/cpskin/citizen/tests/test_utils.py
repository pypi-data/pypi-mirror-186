# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.CMFCore.exceptions import AccessControl_Unauthorized
from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.publisher.browser import TestRequest

from cpskin.citizen import testing
from cpskin.citizen import utils
from cpskin.citizen.browser.settings import ISettings


class TestUtils(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        self.request = TestRequest()

    def tearDown(self):
        api.portal.set_registry_record(
            name="creation_types", value=["Document"], interface=ISettings
        )

    def test_citizen_access_portal_types(self):
        """Test 'citizen_access_portal_types' function"""
        types = utils.citizen_access_portal_types()
        self.assertListEqual(
            sorted(["Document", "News Item", "Event", "organization"]), sorted(types)
        )

    def test_cls_fullpath(self):
        """Test 'cls_fullpath' function"""
        from cpskin.citizen.interfaces import ICpskinCitizenLayer

        self.assertEqual(
            u"cpskin.citizen.interfaces.ICpskinCitizenLayer",
            utils.cls_fullpath(ICpskinCitizenLayer),
        )

    def test_can_edit_as_anonymous(self):
        """Ensure that anonymous user doesn't have edit permissions"""
        logout()
        self.assertTrue(api.user.is_anonymous())
        user = api.user.get_current()
        self.assertFalse(utils.can_edit(user, self.citizen_document))

    def test_can_edit_as_manager(self):
        """Ensure that manager users have edit permissions"""
        user = api.user.get("manager")
        self.assertTrue(utils.can_edit(user, self.citizen_document))
        logout()

    def test_can_edit_as_citizen(self):
        """Ensure that citizen users doesn't have edit permissions"""
        user = api.user.get("citizen")
        self.assertFalse(utils.can_edit(user, self.citizen_document))
        logout()

    def test_execute_under_unrestricted_user(self):
        """Test the 'execute_under_unrestricted_user' function"""
        login(self.portal, "citizen")
        kwargs = {
            "type": "Document",
            "container": self.portal,
            "id": "test-document",
            "title": "Test Document",
        }
        self.assertRaises(AccessControl_Unauthorized, api.content.create, **kwargs)
        self.assertIsNone(self.portal.get("test-document"))
        utils.execute_under_unrestricted_user(
            self.portal, api.content.create, "citizen", **kwargs
        )
        self.assertIsNotNone(self.portal.get("test-document"))

    def test_can_edit_citizen_as_anonymous(self):
        """Ensure that an anonymous user cannot edit citizen content"""
        logout()
        self.assertTrue(api.user.is_anonymous())
        user = api.user.get_current()
        self.assertFalse(utils.can_edit_citizen(user, self.citizen_document))

    def test_can_edit_citizen_as_manager(self):
        """Ensure that a manager user can edit citizen content"""
        user = api.user.get("manager")
        self.assertTrue(utils.can_edit_citizen(user, self.citizen_document))

    def test_can_edit_citizen_as_citizen(self):
        """
        Ensure that a citizen user can edit a content that he have access and
        cannot edit content that he doesn't have access
        """
        user = api.user.get("citizen")
        self.assertTrue(utils.can_edit_citizen(user, self.citizen_document))
        self.assertFalse(utils.can_edit_citizen(user, self.document))

    def test_is_citizen(self):
        """Test 'is_citizen' function"""
        manager = api.user.get("manager")
        self.assertFalse(utils.is_citizen(manager))
        citizen = api.user.get("citizen")
        self.assertTrue(utils.is_citizen(citizen))
        logout()
        anonymous = api.user.get_current()
        self.assertFalse(utils.is_citizen(anonymous))

    def test_can_claim(self):
        """Test 'can_claim' function"""
        user = api.user.get("citizen")
        self.assertTrue(utils.can_claim(user, self.document))
        self.assertFalse(utils.can_claim(user, self.citizen_document))

    def test_have_claimed(self):
        """Test 'have_claimed' function"""
        user = api.user.get("citizen")
        self.assertTrue(utils.have_claimed(user, self.claim_document))
        self.assertFalse(utils.have_claimed(user, self.document))

    def test_get_claim_user(self):
        """Test 'get_claim_users' function"""
        self.assertEqual(["citizen"], utils.get_claim_users(self.claim_document))
        self.assertEqual([], utils.get_claim_users(self.document))

    def test_get_draft_folder(self):
        """Test 'get_draft_folder' function"""
        self.assertEqual(
            self.portal["citizen-drafts"], utils.get_draft_folder(self.document)
        )

    def test_get_settings(self):
        """Test 'get_settings' function"""
        settings = utils.get_settings()
        self.assertEqual(["Document"], settings.creation_types)

    def test_get_creation_folder_default(self):
        """Test 'get_creation_folder' function default"""
        self.assertEqual(
            self.portal, utils.get_creation_folder(self.portal, self.request, "foo")
        )

    def test_get_creation_folder_custom_adapter(self):
        """Test 'get_creation_folder' function for a custom adapter"""
        self.assertEqual(
            self.portal["documents"],
            utils.get_creation_folder(self.portal, self.request, "Document"),
        )

    def test_get_annotations(self):
        """Test 'get_annotations' function"""
        annotations = utils.get_annotations(self.claim_document)
        self.assertEqual(["citizen"], annotations["claim"])

    def test_get_allowed_creation_types(self):
        self.assertEqual(["Document"], utils.get_allowed_creation_types())
        registry = getUtility(IRegistry).forInterface(ISettings)
        registry.creation_types = None
        registry_values = api.portal.get_registry_record(
            name="creation_types", interface=ISettings
        )
        self.assertEqual(None, registry_values)
        self.assertListEqual(
            sorted(["Document", "News Item", "Event", "organization"]),
            sorted(utils.get_allowed_creation_types()),
        )
