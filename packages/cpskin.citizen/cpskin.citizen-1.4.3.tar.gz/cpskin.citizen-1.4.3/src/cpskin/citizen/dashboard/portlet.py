# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from Acquisition import aq_parent
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope.interface import implements
from zope.security import checkPermission

from cpskin.citizen import utils
from cpskin.citizen.interfaces import ICitizenContentSubMenu
from cpskin.citizen.interfaces import ICitizenDashboardFolder
from cpskin.citizen.dashboard.interfaces import IAdminDashboard


class IDashboardPortlet(IPortletDataProvider):
    """Interface for the dashboard portlet"""


class DashboardPortletAssignment(base.Assignment):
    implements(IDashboardPortlet)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def title(self):
        """Return the title of the portlet in "manage portlets" screen"""
        return "citizen dashboard"


class DashboardPortletRenderer(base.Renderer):
    render = ViewPageTemplateFile("templates/dashboard-portlet.pt")

    def update(self, *args, **kwargs):
        super(DashboardPortletRenderer, self).update(*args, **kwargs)
        self.items = self.get_items()

    @property
    def can_view(self):
        return len(self.items) > 0

    @property
    def base_folder(self):
        context = aq_inner(self.context)
        while not ICitizenDashboardFolder.providedBy(context):
            context = aq_parent(context)
        return context

    def is_citizen(self):
        current_user = api.user.get_current()
        return utils.is_citizen(current_user)

    def is_sub_menu(self, obj):
        return ICitizenContentSubMenu.providedBy(obj)

    def get_admin_dashboards(self):
        return [
            d
            for i, d in self.base_folder.contentItems()
            if IAdminDashboard.providedBy(d) and checkPermission("zope2.View", d)
        ]

    def get_citizen_items(self):
        items = []
        for i, d in self.base_folder.contentItems():
            if IAdminDashboard.providedBy(d):
                continue
            if not checkPermission("zope2.View", d):
                continue
            items.append(d)
        return items

    def get_items(self):
        if api.user.is_anonymous():
            return []
        if self.is_citizen():
            return self.get_citizen_items()
        else:
            return self.get_admin_dashboards()

    def css_class(self, item):
        base = ""
        if self.is_sub_menu(item):
            base = "citizen-content-submenu"
        return "{0} {1}".format(base, item.id)


class DashboardPortletAddForm(base.NullAddForm):
    def create(self):
        return DashboardPortletAssignment()
