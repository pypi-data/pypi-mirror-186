# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.interface import Interface
from eea.facetednavigation.interfaces import IFacetedNavigable


class ICitizenDashboard(IFacetedNavigable):
    """Marker interface for dashboard folder"""


class IAdminDashboard(ICitizenDashboard):
    """Marker interface for admin dashboard folder"""


class ICitizenMyContent(Interface):
    """Marker interface for "My contents" dashboard"""


class ICitizenDashboardQuery(Interface):
    """Utility for citizen dashboard query extra filters"""


class IFacetedDashboardTable(Interface):
    """Marker interface for dashboard table"""


class IFacetedDashboardCitizenContentTable(IFacetedDashboardTable):
    """Citizen faceted content table"""


class IFacetedDashboardCitizenClaimTable(IFacetedDashboardTable):
    """Citizen faceted claim table"""


class IFacetedDashboardCitizenMapTable(IFacetedDashboardTable):
    """Citizen faceted claim table"""


class IFacetedDashboardAdminContentTable(IFacetedDashboardTable):
    """Admin faceted content table"""


class IFacetedDashboardAdminClaimTable(IFacetedDashboardTable):
    """Admin faceted claim table"""
