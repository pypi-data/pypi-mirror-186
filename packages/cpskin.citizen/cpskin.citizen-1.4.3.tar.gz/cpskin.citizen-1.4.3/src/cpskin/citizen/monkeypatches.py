# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api


def afterMemberAdd(self, member, id, password, properties):
    """
    Called by portal_registration.addMember() after a member
    has been added successfully
    """
    if not api.group.get(groupname="Citizens"):
        return
    # if this is an auto registration, not an administrator action
    if api.user.is_anonymous():
        api.group.add_user(groupname="Citizens", user=member)
