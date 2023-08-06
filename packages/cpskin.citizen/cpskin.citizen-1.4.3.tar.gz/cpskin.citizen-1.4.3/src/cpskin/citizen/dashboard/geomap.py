# -*- coding: utf-8 -*-
from collective.geo.leaflet.interfaces import IGeoMap
from collective.geo.leaflet.geomap import GeoMap as GM
from plone import api
from zope.interface import implementer


@implementer(IGeoMap)
class GeoMap(GM):
    def map_center(self):
        user = api.user.get_current()
        latitude = user.getProperty("latitude", False)
        longitude = user.getProperty("longitude", False)
        if latitude and longitude:
            return {"longitude": str(longitude), "latitude": str(latitude)}
        else:
            return super(GeoMap, self).map_center()

    def geo_settings(self):
        settings = super(GeoMap, self).geo_settings()
        # Update zoom map level
        settings["zoom"] = str(16)
        return settings
