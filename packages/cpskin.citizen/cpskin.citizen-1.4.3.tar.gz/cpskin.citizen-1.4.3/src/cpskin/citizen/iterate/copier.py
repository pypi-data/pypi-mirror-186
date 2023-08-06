# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone import api
from plone.app.stagingbehavior import copier
from zExceptions import Unauthorized

from cpskin.citizen import utils


class ContentCopierAdapter(copier.ContentCopier):
    def copyTo(self, container):
        current_user = api.user.get_current()
        if utils.can_edit(current_user, self.context):
            return super(ContentCopierAdapter, self).copyTo(container)
        if utils.can_edit_citizen(current_user, self.context):
            elements = utils.execute_under_unrestricted_user(
                api.portal.get(),
                super(ContentCopierAdapter, self).copyTo,
                "admin",
                container,
            )
            elements[0].creators = (current_user.id,)
            return elements
        raise Unauthorized(u"Cannot edit this content")
