# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from borg.localrole.interfaces import ILocalRoleProvider
from zope.interface import implements


class LocalRoleAdapter(object):
    implements(ILocalRoleProvider)

    def __init__(self, context):
        self.context = context

    def getRoles(self, principal):
        """Grant permission for principal"""
        citizens = getattr(self.context, "citizens", []) or []
        if principal in citizens:
            return ("Reader", "Citizen Editor")
        return []

    def getAllRoles(self):
        """Grant permissions"""
        if not getattr(self.context, "citizens", None):
            yield ("", ("",))
            raise StopIteration
        else:
            permissions = ("Reader", "Citizen Editor")
            for citizen in self.context.citizens:
                yield (citizen, permissions)
