# -*- coding: utf-8 -*-

from zope.publisher.browser import TestRequest
from plone import api
from cpskin.citizen import testing
from zope.component import getMultiAdapter
from cpskin.citizen.interfaces import ICitizenCreationFolder
from mock import patch


class TestAdapter(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def setUp(self):
        self.request = TestRequest()

    def test_creation_folder_adapter_default(self):
        """ Test CitizenCreationFolderAdapter """
        context = api.portal.get()
        adapter = getMultiAdapter((context, self.request), ICitizenCreationFolder)
        self.assertEqual(context, adapter.get_folder(context, "Document"))

    def test_creation_folder_adapter_root(self):
        """ Test CitizenCreationFolderAdapter """
        from cpskin.citizen import utils

        context = api.portal.get()
        adapter = getMultiAdapter((context, self.request), ICitizenCreationFolder)
        settings = type(
            "settings", (object,), {"proposal_folders": {"Document": "/"}}
        )()
        with patch.object(utils, "get_settings", return_value=settings):
            self.assertEqual(context, adapter.get_folder(context, "Document"))

    def test_creation_folder_adapter_folder(self):
        """ Test CitizenCreationFolderAdapter """
        from cpskin.citizen import utils

        context = api.portal.get()
        adapter = getMultiAdapter((context, self.request), ICitizenCreationFolder)
        settings = type(
            "settings", (object,), {"proposal_folders": {"Document": "documents"}}
        )()
        with patch.object(utils, "get_settings", return_value=settings):
            self.assertEqual(
                context["documents"], adapter.get_folder(context, "Document")
            )

        # with leading /
        settings = type(
            "settings", (object,), {"proposal_folders": {"Document": "/documents"}}
        )()
        with patch.object(utils, "get_settings", return_value=settings):
            self.assertEqual(
                context["documents"], adapter.get_folder(context, "Document")
            )

    def test_creation_folder_adapter_unknown_folder(self):
        """ Test CitizenCreationFolderAdapter """
        from cpskin.citizen import utils

        context = api.portal.get()
        adapter = getMultiAdapter((context, self.request), ICitizenCreationFolder)
        settings = type(
            "settings", (object,), {"proposal_folders": {"Document": "foo"}}
        )()
        with patch.object(utils, "get_settings", return_value=settings):
            self.assertRaisesRegexp(
                KeyError,
                "unknown creation folder: .*",
                adapter.get_folder,
                context,
                "Document",
            )
