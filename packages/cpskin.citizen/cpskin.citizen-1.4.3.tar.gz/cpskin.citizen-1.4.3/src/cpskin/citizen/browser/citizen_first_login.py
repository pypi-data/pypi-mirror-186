# -*- coding: utf-8 -*-
from cpskin.citizen.utils import is_citizen
from plone import api

import geocoder
import logging

logger = logging.getLogger("cpskin.citizen get lat lng")


def create_lat_lon(event):
    user = event.object
    if not is_citizen(user):
        return
    if user.getProperty("latitude", False):
        return
    geocode = get_lat_lng_from_address(
        user.getProperty("street"),
        user.getProperty("number"),
        user.getProperty("zip_code"),
        user.getProperty("location"),
    )
    # Use geocode.ok to avoid UnicodeDecodeError
    if getattr(geocode, "ok", False) is True:
        username = user.getUserName()
        member = api.user.get(username=username)
        member.setMemberProperties(mapping={"latitude": str(geocode.lat)})
        member.setMemberProperties(mapping={"longitude": str(geocode.lng)})


def get_lat_lng_from_address(street, number, zip_code, city):
    if street is None or city is None:
        return
    if street is not None and city is not None:
        address = "{} {} {} {}".format(number, street, zip_code, city)
        return geocoder.google(address)
