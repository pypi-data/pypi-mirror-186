# -*- coding: utf-8 -*-
from cpskin.citizen import _
from plone.app.users.browser.personalpreferences import UserDataPanelAdapter
from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope.interface import implements
from zope import schema


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    street = schema.TextLine(
        title=_(u"Street", default=u"Rue"),
        description=_(
            u"help_street_description",
            default=u"Indiquez le nom de votre rue, cette adresse sera utilisée dans le site pour géolocaliser ce qu'il se passe autour de chez vous.",
        ),
        required=False,
    )

    number = schema.TextLine(title=_(u"Number", default=u"Numéro"), required=False)

    zip_code = schema.TextLine(
        title=_(u"Post Code", default=u"Code postal"), required=False
    )

    location = schema.TextLine(title=_(u"City", default=u"Ville"), required=False)

    latitude = schema.TextLine(
        title=_(u"Latitude", default=u"Latitude"),
        description=_(
            u"help_latitude_coordinates",
            default=u"Coordinates (latitude) of your living place",
        ),
        required=False,
    )

    longitude = schema.TextLine(
        title=_(u"Longitude", default=u"Longitude"),
        description=_(
            u"help_longitude_coordinates",
            default=u"Coordinates (longitude) of your living place",
        ),
        required=False,
    )


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """

    def _set_property(self, key, value):
        return self.context.setMemberProperties(
            {key: value and value.encode("utf-8") or value}
        )

    def _get_property(self, key):
        return self.context.getProperty(key, "").decode("utf-8")

    @property
    def street(self):
        return self._get_property("street")

    @street.setter
    def street(self, value):
        return self._set_property("street", value)

    @property
    def number(self):
        return self._get_property("number")

    @number.setter
    def number(self, value):
        return self._set_property("number", value)

    @property
    def zip_code(self):
        return self._get_property("zip_code")

    @zip_code.setter
    def zip_code(self, value):
        return self._set_property("zip_code", value)

    @property
    def location(self):
        return self._get_property("location")

    @location.setter
    def location(self, value):
        return self._set_property("location", value)

    @property
    def latitude(self):
        return self._get_property("latitude")

    @latitude.setter
    def latitude(self, value):
        return self._set_property("latitude", value)

    @property
    def longitude(self):
        return self._get_property("longitude")

    @longitude.setter
    def longitude(self, value):
        return self._set_property("longitude", value)
