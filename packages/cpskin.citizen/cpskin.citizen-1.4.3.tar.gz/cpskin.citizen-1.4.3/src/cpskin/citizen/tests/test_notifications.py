# -*- coding: utf-8 -*-

from cpskin.citizen import testing
from cpskin.citizen import notification
from mock import patch
from plone import api


class TestNotification(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        self.citizen = api.user.get(userid="citizen")

    def tearDown(self):
        api.portal.set_registry_record(
            "cpskin.citizen.browser.settings.ISettings.manager_email", u""
        )

    def test_get_recipient(self):
        self.assertEqual("citizen@citizen.com", notification._get_recipient("citizen"))

    def test_get_missing_recipient(self):
        """ Test a special usecase where the citizen user does not exist anymore """
        self.assertIsNone(notification._get_recipient("foo"))

    def test_notify_content_validated_single_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_validated(self.citizen_document)
            self.assertTrue(mock.called)
            self.assertEqual(1, mock.call_count)

    def test_notify_content_validated_multi_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_validated(self.citizens_document)
            self.assertTrue(mock.called)
            self.assertEqual(2, mock.call_count)

    def test_notify_content_validated_no_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_validated(self.claim_document)
            self.assertFalse(mock.called)

    def test_notify_content_refused_single_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_refused(self.citizen_document)
            self.assertTrue(mock.called)
            self.assertEqual(1, mock.call_count)

    def test_notify_content_refused_multi_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_refused(self.citizens_document)
            self.assertTrue(mock.called)
            self.assertEqual(2, mock.call_count)

    def test_notify_content_refused_no_citizen(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_refused(self.claim_document)
            self.assertFalse(mock.called)

    def test_notify_content_awaiting_validation(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_awaiting_validation(
                self.citizens_document, self.citizen
            )
            self.assertTrue(mock.called)
            self.assertEqual(1, mock.call_count)

    def test_notify_content_awaiting_validation_with_recipients(self):
        api.portal.set_registry_record(
            "cpskin.citizen.browser.settings.ISettings.manager_email", u"foo@bar.com"
        )
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_awaiting_validation(
                self.citizens_document, self.citizen
            )
            self.assertTrue(mock.called)
            self.assertEqual(2, mock.call_count)

    def test_notify_content_awaiting_access(self):
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_awaiting_access(
                self.citizens_document, self.citizen
            )
            self.assertTrue(mock.called)
            self.assertEqual(1, mock.call_count)

    def test_notify_content_awaiting_access_with_recipients(self):
        api.portal.set_registry_record(
            "cpskin.citizen.browser.settings.ISettings.manager_email",
            u"foo@bar.com;bar@foo.com",
        )
        with patch.object(api.portal, "send_email", return_value=None) as mock:
            notification.notify_content_awaiting_access(
                self.citizens_document, self.citizen
            )
            self.assertTrue(mock.called)
            self.assertEqual(3, mock.call_count)
