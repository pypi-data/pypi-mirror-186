# -*- coding: utf-8 -*-

from Acquisition import aq_base
from Acquisition import aq_inner
from Products.Five import BrowserView
from plone.app.iterate.interfaces import IWorkingCopy
from plone.app.stagingbehavior.utils import get_relations
from zc.relation.interfaces import ICatalog
from zope.component import getUtility
from zope.interface import noLongerProvides


class CleanupView(BrowserView):
    def __call__(self, *args, **kwargs):
        context = aq_base(aq_inner(self.context))
        relations = get_relations(context)
        ref_catalog = getUtility(ICatalog)
        for relation in relations:
            if relation.from_object is None:
                # Remove the relation from the reference catalog
                ref_catalog.unindex(relation)
                # Remove the interface
                if IWorkingCopy.providedBy(context):
                    noLongerProvides(context, IWorkingCopy)
        self.request.response.redirect(self.context.absolute_url())
