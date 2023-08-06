# -*- coding: utf-8 -*-

from cpskin.citizen import testing
from plone import api
from plone.app.testing import login
from plone.app.testing import logout
from plone.locking.interfaces import ILockable


class TestCancelView(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        login(self.portal, "manager")
        self.cancel_document = api.content.create(
            container=self.portal,
            type="Document",
            id="cancel-document",
            title="Cancel",
            citizens=["citizen"],
        )
        logout()
        self._create_checkout()

    def _create_checkout(self, user="citizen"):
        login(self.portal, user)
        view = self.cancel_document.restrictedTraverse("@@content-checkout")
        view.request.form["form.button.Checkout"] = "1"
        view.__call__()
        self.document_draft = self.drafts["cancel-document"]
        logout()

    def tearDown(self):
        login(self.portal, "manager")
        if "cancel-document" in self.drafts:
            api.content.delete(self.drafts["cancel-document"])
        lockable = ILockable(self.cancel_document)
        if lockable.locked():
            lockable.clear_locks()
        api.content.delete(self.cancel_document)
        logout()

    def test_cancel_as_manager_no_submit(self):
        login(self.portal, "manager")
        view = self.document_draft.restrictedTraverse("@@cancel-citizen")
        view.__call__()
        self.assertTrue("cancel-document" in self.drafts)

    def test_cancel_as_manager(self):
        login(self.portal, "manager")
        view = self.document_draft.restrictedTraverse("@@cancel-citizen")
        view.request.form["form.button.Cancel"] = "1"
        view.__call__()
        self.assertFalse("cancel-document" in self.drafts)

    def test_cancel_as_citizen_no_submit(self):
        login(self.portal, "citizen")
        view = self.document_draft.restrictedTraverse("@@cancel-citizen")
        view.__call__()
        self.assertTrue("cancel-document" in self.drafts)

    def test_cancel_as_citizen(self):
        login(self.portal, "citizen")
        view = self.document_draft.restrictedTraverse("@@cancel-citizen")
        view.request.form["form.button.Cancel"] = "1"
        view.__call__()
        self.assertFalse("cancel-document" in self.drafts)
