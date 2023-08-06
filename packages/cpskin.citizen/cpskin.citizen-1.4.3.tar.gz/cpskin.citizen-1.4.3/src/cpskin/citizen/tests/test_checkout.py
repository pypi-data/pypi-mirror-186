# -*- coding: utf-8 -*-

from cpskin.citizen import testing
from cpskin.citizen import utils
from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.locking.interfaces import ILockable
from zope.component import queryAdapter


class TestCheckout(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        login(self.portal, "manager")
        self.doc = api.content.create(
            container=self.portal,
            type="Document",
            id="test-document",
            title="doc",
            citizens=["citizen"],
        )
        self.event = api.content.create(
            container=self.portal,
            type="Event",
            id="test-event",
            title="event",
            citizens=["citizen"],
        )
        self.directory = api.content.create(
            container=self.portal, type="directory", id="directory", title="directory"
        )
        self.organization = api.content.create(
            container=self.directory,
            type="organization",
            id="test-organization",
            title="organization",
            citizens=["citizen"],
        )
        logout()

    def _create_checkout(self, obj, user="citizen"):
        login(self.portal, user)
        view = obj.restrictedTraverse("@@content-checkout")
        view.request.form["form.button.Checkout"] = "1"
        view.__call__()
        logout()

    def _cancel_checkout(self, obj, user="citizen"):
        login(self.portal, user)
        view = obj.restrictedTraverse("@@cancel-citizen")
        view.request.form["form.button.Cancel"] = "1"
        view.__call__()
        logout()

    def tearDown(self):
        login(self.portal, "manager")
        for obj_id in ["test-event", "test-document", "directory"]:
            if obj_id in self.drafts:
                api.content.delete(self.drafts[obj_id])
            lockable = queryAdapter(self.portal[obj_id], ILockable)
            if lockable and lockable.locked():
                lockable.clear_locks()
            api.content.delete(self.portal[obj_id])
        logout()

    def test_checkout_document(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-document"])
        self.assertTrue("test-document" in self.drafts)

        self.assertEqual(
            self.portal["test-document"],
            utils.get_baseline(self.drafts["test-document"]),
        )
        self.assertEqual(
            self.portal["test-document"],
            utils.get_baseline(self.portal["test-document"]),
        )

        self.assertEqual(
            self.drafts["test-document"],
            utils.get_working_copy(self.portal["test-document"]),
        )
        self.assertEqual(
            self.drafts["test-document"],
            utils.get_working_copy(self.drafts["test-document"]),
        )

    def test_checkout_event(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-event"])
        self.assertTrue("test-event" in self.drafts)

        self.assertEqual(
            self.portal["test-event"], utils.get_baseline(self.drafts["test-event"])
        )
        self.assertEqual(
            self.portal["test-event"], utils.get_baseline(self.portal["test-event"])
        )

        self.assertEqual(
            self.drafts["test-event"], utils.get_working_copy(self.portal["test-event"])
        )
        self.assertEqual(
            self.drafts["test-event"], utils.get_working_copy(self.drafts["test-event"])
        )

    def test_checkout_organization(self):
        login(self.portal, "citizen")
        self._create_checkout(self.organization)
        self.assertTrue("copy_of_test-organization" in self.directory)

        self.assertEqual(
            self.organization,
            utils.get_baseline(self.directory["copy_of_test-organization"]),
        )
        self.assertEqual(
            self.organization,
            utils.get_baseline(self.organization),
        )

        self.assertEqual(
            self.directory["copy_of_test-organization"],
            utils.get_working_copy(self.organization),
        )
        self.assertEqual(
            self.directory["copy_of_test-organization"],
            utils.get_working_copy(self.directory["copy_of_test-organization"]),
        )

    def test_cancel_checkout_document(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-document"])
        self.assertTrue("test-document" in self.drafts)
        self._cancel_checkout(self.drafts["test-document"])
        self.assertTrue("test-document" not in self.drafts)
        self.assertIsNone(utils.get_working_copy(self.portal["test-document"]))
        self.assertIsNone(utils.get_baseline(self.portal["test-document"]))

    def test_cancel_checkout_event(self):
        login(self.portal, "citizen")
        self._create_checkout(self.portal["test-event"])
        self.assertTrue("test-event" in self.drafts)
        self._cancel_checkout(self.drafts["test-event"])
        self.assertTrue("test-event" not in self.drafts)
        self.assertIsNone(utils.get_working_copy(self.portal["test-event"]))
        self.assertIsNone(utils.get_baseline(self.portal["test-event"]))

    def test_cancel_checkout_organization(self):
        login(self.portal, "citizen")
        self._create_checkout(self.organization)
        self.assertTrue("copy_of_test-organization" in self.directory)
        self._cancel_checkout(self.directory["copy_of_test-organization"])
        self.assertTrue("copy_of_test-organization" not in self.directory)
        self.assertIsNone(utils.get_working_copy(self.organization))
        self.assertIsNone(utils.get_baseline(self.organization))
