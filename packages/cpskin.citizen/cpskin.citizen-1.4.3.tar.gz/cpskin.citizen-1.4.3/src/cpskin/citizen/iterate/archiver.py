# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.iterate import archiver
from zExceptions import Unauthorized

from cpskin.citizen import utils


class ContentArchiverAdapter(archiver.ContentArchiver):
    def save(self, checkin_message):
        current_user = api.user.get_current()
        if utils.can_edit(current_user, self.context):
            return self.repository.save(self.context, checkin_message)
        if utils.can_edit_citizen(current_user, self.context):
            return utils.execute_under_unrestricted_user(
                api.portal.get(),
                self.repository.save,
                current_user.id,
                self.context,
                checkin_message,
            )
        raise Unauthorized(u"Cannot edit this content")
