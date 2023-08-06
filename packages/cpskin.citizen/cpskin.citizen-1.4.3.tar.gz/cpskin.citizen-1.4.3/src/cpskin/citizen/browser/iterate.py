# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Products.Five import BrowserView
from cpskin.citizen import notification
from cpskin.citizen import utils
from plone.app.iterate.browser.checkin import Checkin


class ReturnView(BrowserView):
    def __call__(self):
        view_url = self.context.absolute_url()
        form = self.request.form
        if "form.button.Confirm" in form:
            annotations = utils.get_annotations(self.context)
            annotations["validation_required"] = False
            annotations["comment"] = form.get("return_message", u"")
            self.context.reindexObject()
            notification.notify_content_refused(self.context)
            self.request.response.redirect(view_url)
        elif "form.button.Cancel" in form:
            self.request.response.redirect(view_url)
        return self.index()


class CheckinView(Checkin):
    def __call__(self):
        result = super(CheckinView, self).__call__()
        notification.notify_content_validated(self.context)
        return result
