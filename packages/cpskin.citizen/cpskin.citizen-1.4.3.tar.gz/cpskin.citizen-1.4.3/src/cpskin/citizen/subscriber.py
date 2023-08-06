# -*- coding: utf-8 -*-

from plone import api
from plone.app.stagingbehavior.utils import get_working_copy


def citizen_content_removed(obj, event):
    draft = get_working_copy(obj)
    if draft:
        api.content.remove(obj)
