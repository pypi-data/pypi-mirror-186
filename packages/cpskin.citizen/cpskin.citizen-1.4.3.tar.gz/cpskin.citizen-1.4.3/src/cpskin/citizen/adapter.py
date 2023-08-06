# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api

from cpskin.citizen import utils


class CitizenCreationFolderAdapter(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def get_folder(self, navigation_root, portal_type):
        settings = utils.get_settings()
        path = settings.proposal_folders.get(portal_type, "")
        if path.startswith("/"):
            path = path[1:]
        try:
            return navigation_root.restrictedTraverse(str(path))
        except KeyError:
            raise KeyError("unknown creation folder: {0}".format(str(path)))


class CitizenDraftFolderAdapter(object):
    def __init__(self, context):
        self.context = context

    def get_folder(self):
        navigation_root = api.portal.get_navigation_root(self.context)
        return navigation_root["citizen-drafts"]


class CitizenDraftOrganizationAdapter(CitizenDraftFolderAdapter):
    def get_folder(self):
        navigation_root = api.portal.get_navigation_root(self.context)
        return navigation_root["annuaire"]
