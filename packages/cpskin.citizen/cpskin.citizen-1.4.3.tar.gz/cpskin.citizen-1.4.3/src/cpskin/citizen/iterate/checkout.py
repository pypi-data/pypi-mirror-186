# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from Acquisition import aq_inner
from Products.statusmessages.interfaces import IStatusMessage
from plone import api
from plone.app.iterate import PloneMessageFactory as PMF
from plone.app.iterate.browser import checkout
from plone.app.iterate.interfaces import CheckoutException
from plone.app.iterate.interfaces import ICheckinCheckoutPolicy
from zope.component import getMultiAdapter

from cpskin.citizen import utils


class CheckoutView(checkout.Checkout):
    def checkout(self, context):
        """Perform the checkout"""
        control = getMultiAdapter((context, self.request), name=u"iterate_control")
        if not control.checkout_allowed():
            raise CheckoutException(u"Not allowed")

        location = self.request.form.get("checkout_location", None)
        locator = None
        try:
            locator = [
                c["locator"] for c in self.containers() if c["name"] == location
            ][0]
        except IndexError:
            status_message = IStatusMessage(self.request)
            status_message.addStatusMessage(
                PMF("Cannot find checkout location"), type="stop"
            )
            view_url = context.restrictedTraverse("@@plone_context_state").view_url()
            self.request.response.redirect(view_url)
            return

        policy = ICheckinCheckoutPolicy(context)
        wc = policy.checkout(locator())

        # we do this for metadata update side affects which will update lock info
        context.reindexObject("review_state")

        current_user = api.user.get_current()
        if utils.can_edit(current_user, context):
            status_message = IStatusMessage(self.request)
            status_message.addStatusMessage(PMF("Check-out created"), type="info")
            view_url = wc.restrictedTraverse("@@plone_context_state").view_url()
        else:
            view_url = "{0}/@@edit-citizen".format(
                wc.restrictedTraverse("@@plone_context_state").view_url()
            )
        self.request.response.redirect(view_url)

    def __call__(self):
        context = aq_inner(self.context)

        containers = list(self.containers())
        if len(containers) == 1:
            # Special case for when there's only when folder to select
            self.request.form["form.button.Checkout"] = 1
            self.request.form["checkout_location"] = containers[0]["name"]

        # We want to redirect to a specific template, else we might
        # end up downloading a file
        if "form.button.Checkout" in self.request.form:
            self.checkout(context)
        elif "form.button.Cancel" in self.request.form:
            view_url = context.restrictedTraverse("@@plone_context_state").view_url()
            self.request.response.redirect(view_url)
        else:
            return self.index()
