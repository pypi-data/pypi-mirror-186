# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from zope.interface import implements

from cpskin.citizen.dashboard.interfaces import ICitizenDashboardQuery


class DefaultQueryFilters(object):
    implements(ICitizenDashboardQuery)

    def apply_filters(self, query):
        query["is_draft"] = False
        query["object_provides"] = u"cpskin.citizen.behavior.ICitizenAccess"
        return query


class AdminContentQueryFilters(object):
    implements(ICitizenDashboardQuery)

    def apply_filters(self, query):
        query["object_provides"] = u"cpskin.citizen.behavior.ICitizenAccess"
        query["is_citizen_content"] = True
        return query


class CitizenContentQueryFilters(DefaultQueryFilters):
    def apply_filters(self, query):
        current_user = api.user.get_current()
        query = super(CitizenContentQueryFilters, self).apply_filters(query)
        query["citizens"] = current_user.id
        return query


class CitizenClaimQueryFilters(DefaultQueryFilters):
    def apply_filters(self, query):
        current_user = api.user.get_current()
        query = super(CitizenClaimQueryFilters, self).apply_filters(query)
        query["citizen_claim"] = current_user.id
        return query


class CitizenMapQueryFilters(DefaultQueryFilters):
    def apply_filters(self, query):
        citizen_map_portal_types = api.portal.get_registry_record(
            "cpskin.citizen.browser.settings.ISettings.map_view_types"
        )
        if citizen_map_portal_types and "portal_type" not in query:
            query["portal_type"] = citizen_map_portal_types
        query["is_geolocated"] = True
        return query
