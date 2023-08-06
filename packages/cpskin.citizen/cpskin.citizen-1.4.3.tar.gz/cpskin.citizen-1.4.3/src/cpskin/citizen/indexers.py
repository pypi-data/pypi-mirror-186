# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from collective.geo.geographer.interfaces import IGeoreferenced
from cpskin.citizen import utils
from cpskin.citizen.behavior import ICitizenAccess
from cpskin.citizen.utils import get_baseline
from cpskin.citizen.utils import get_working_copy
from plone.app.iterate.interfaces import IWorkingCopy
from plone.indexer import indexer
from zope.component import queryAdapter
from zope.interface import Interface


@indexer(ICitizenAccess)
def citizens_indexer(obj):
    if obj != get_working_copy(obj):
        return obj.citizens


@indexer(ICitizenAccess)
def validation_required_indexer(obj):
    return utils.validation_required(obj)


@indexer(ICitizenAccess)
def citizen_claim_indexer(obj):
    if obj != get_working_copy(obj):
        return utils.get_claim_users(obj)


@indexer(ICitizenAccess)
def is_draft(obj):
    return IWorkingCopy.providedBy(obj)


@indexer(ICitizenAccess)
def has_claim(obj):
    return utils.has_claim(obj)


@indexer(Interface)
def is_geolocated(obj):
    geo_adapter = queryAdapter(obj, IGeoreferenced)
    if geo_adapter:
        return geo_adapter.geo.get("coordinates") is not None
    return False


@indexer(ICitizenAccess)
def is_citizen_content(obj):
    if obj != get_working_copy(obj) and obj.citizens:
        return True
    try:
        baseline = get_baseline(obj)
        if getattr(baseline, "citizens", None):
            return True
    except KeyError:
        # This happen when a link is broken
        pass
    return utils.has_claim(obj)


@indexer(ICitizenAccess)
def citizen_action(obj):
    if utils.has_claim(obj) is True:
        return "allow-management"
    if utils.validation_required(obj) is True:
        return "awaiting-for-approval"
