# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from plone.app.iterate.browser import checkin
from plone.app.iterate.interfaces import CheckinException
from zope.component import getMultiAdapter

from cpskin.citizen import utils


class CheckinView(checkin.Checkin):
    def __call__(self):
        context = aq_inner(self.context)

        if "form.button.Checkin" in self.request.form:
            control = getMultiAdapter((context, self.request), name=u"iterate_control")
            if not control.checkin_allowed():
                raise CheckinException(u"Not a checkout")
            annotations = utils.get_annotations(context)
            annotations["comment"] = None
            annotations["validation_required"] = False
        return super(CheckinView, self).__call__()
