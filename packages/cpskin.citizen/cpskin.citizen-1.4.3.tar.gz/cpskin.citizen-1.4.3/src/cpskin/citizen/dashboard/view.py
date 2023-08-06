# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.eeafaceted.z3ctable.browser.views import FacetedTableView

from cpskin.citizen.dashboard import table


class UserContentTableView(table.CitizenContentTable, FacetedTableView):
    pass


class UserClaimTableView(table.CitizenClaimTable, FacetedTableView):
    pass


class UserMapTableView(table.CitizenMapTable, FacetedTableView):
    pass


class AdminContentTableView(table.AdminContentTable, FacetedTableView):
    pass


class AdminClaimTableView(table.AdminClaimTable, FacetedTableView):
    pass
