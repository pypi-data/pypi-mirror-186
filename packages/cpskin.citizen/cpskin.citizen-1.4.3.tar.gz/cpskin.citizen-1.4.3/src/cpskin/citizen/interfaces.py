# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICpskinCitizenLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICitizenContentSubMenu(Interface):
    pass


class ICitizenProposeContentFolder(Interface):
    pass


class ICitizenCreationFolder(Interface):
    pass


class ICitizenDraftFolder(Interface):
    pass


class ICitizenDashboardFolder(Interface):
    pass


class IFacetedConfig(Interface):
    pass
