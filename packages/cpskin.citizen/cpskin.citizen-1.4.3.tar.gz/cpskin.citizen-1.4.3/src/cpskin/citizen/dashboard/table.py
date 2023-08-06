# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from z3c.table.table import Table
from zope.interface import implements

from cpskin.citizen.dashboard import interfaces


class DashboardTable(Table):
    implements(interfaces.IFacetedDashboardTable)

    cssClassEven = u"even"
    cssClassOdd = u"odd"
    cssClasses = {"table": "listing dashboard-listing"}

    batchSize = 20
    startBatchingAt = 30
    results = []

    _ignored_columns = (
        "Title",
        "select_row",
        "Creator",
        "getText",
        "ModificationDate",
        "CreationDate",
        "review_state",
        "actions",
        "pretty_link",
    )

    def setUpColumns(self):
        columns = super(DashboardTable, self).setUpColumns()
        return [c for c in columns if c.__name__ not in self._ignored_columns]


class CitizenContentTable(DashboardTable):
    implements(interfaces.IFacetedDashboardCitizenContentTable)


class CitizenClaimTable(DashboardTable):
    implements(interfaces.IFacetedDashboardCitizenClaimTable)


class AdminContentTable(DashboardTable):
    implements(interfaces.IFacetedDashboardAdminContentTable)


class AdminClaimTable(DashboardTable):
    implements(interfaces.IFacetedDashboardAdminClaimTable)


class CitizenMapTable(Table):
    implements(interfaces.IFacetedDashboardCitizenMapTable)

    batchSize = 20000
