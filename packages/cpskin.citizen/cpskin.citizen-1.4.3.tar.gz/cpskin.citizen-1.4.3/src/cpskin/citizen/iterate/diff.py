# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from plone.app.iterate.browser import diff
from plone.app.iterate.interfaces import IWorkingCopy, IBaseline
from plone.app.stagingbehavior import STAGING_RELATION_NAME
from zc.relation.interfaces import ICatalog
from zope.component import queryUtility
from zope.intid.interfaces import IIntIds


class DiffView(diff.DiffView):
    def __init__(self, context, request):
        self.context = context
        self.request = request
        # if context.portal_type == 'Event':
        #     if not getattr(context, 'location', False):
        #         context.location = None
        catalog = queryUtility(ICatalog)
        intids = queryUtility(IIntIds)
        if IBaseline.providedBy(self.context):
            self.baseline = context
            self.working_copy = (
                catalog.findRelations(
                    dict(
                        from_id=intids.getId(context),
                        from_attribute=STAGING_RELATION_NAME,
                    )
                )
                .next()
                .to_object
            )
        elif IWorkingCopy.providedBy(self.context):
            self.working_copy = context
            self.baseline = (
                catalog.findRelations(
                    dict(
                        to_id=intids.getId(context),
                        from_attribute=STAGING_RELATION_NAME,
                    )
                )
                .next()
                .from_object
            )
        else:
            raise AttributeError("Invalid Context")
