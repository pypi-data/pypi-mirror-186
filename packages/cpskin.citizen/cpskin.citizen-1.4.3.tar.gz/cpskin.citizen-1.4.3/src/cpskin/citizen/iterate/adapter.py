# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api

from cpskin.citizen import _
from cpskin.citizen import utils


class DraftFolderLocator(object):

    title = _(u"Citizen draft folder")

    def __init__(self, context):
        self.context = context

    @property
    def available(self):
        """Ensure that the current user is a citizen"""
        current_user = api.user.get_current()
        return utils.can_edit_citizen(current_user, self.context)

    def __call__(self):
        return utils.get_draft_folder(self.context)
