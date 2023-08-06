# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from cpskin.citizen import security
from cpskin.citizen import utils
from plone import api
from plone.app.iterate.interfaces import IWorkingCopy


class CitizenSecurityMigrateView(BrowserView):
    def migrate(self):
        return security.ManageSecurity(self.request).migrate()


class CitizenFixBrokenLinks(BrowserView):
    def migrate(self):
        query = {
            "portal_type": utils.citizen_access_portal_types(),
            "provides": {"not": IWorkingCopy},
        }
        brains = [b for b in api.content.find(**query) if b.citizens]
        return self._migrate(brains)

    def _migrate(self, brains):
        result = []
        for brain in brains:
            obj = brain.getObject()
            try:
                utils.get_wc(obj)
            except KeyError as e:
                if "copy_of" in e.__str__():
                    utils.remove_relation(obj)
                    result.append(brain.getURL())
        return result
