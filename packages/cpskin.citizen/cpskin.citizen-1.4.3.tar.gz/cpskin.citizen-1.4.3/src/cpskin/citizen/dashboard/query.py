# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from eea.facetednavigation.browser.app.query import FacetedQueryHandler
from zope.component import getUtility
from zope.component import queryUtility

from cpskin.citizen.dashboard.interfaces import ICitizenDashboardQuery


class DashboardQueryHandler(FacetedQueryHandler):
    def criteria(self, *args, **kwargs):
        query = super(DashboardQueryHandler, self).criteria(*args, **kwargs)
        utility = queryUtility(ICitizenDashboardQuery, name=self.context.id)
        if utility is None:
            utility = getUtility(ICitizenDashboardQuery, name="default")
        return utility.apply_filters(query)

    def table_view(self):
        view_name = "@@{0}-table-view".format(self.context.id)
        return self.context.restrictedTraverse(view_name)
