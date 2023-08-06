# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from persistent.dict import PersistentDict
from plone import api
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import logout
from plone.testing import z2
from zope.annotation import IAnnotations

import transaction
import unittest

from cpskin.citizen import ANNOTATION_KEY
from cpskin.citizen.adapter import CitizenCreationFolderAdapter
from cpskin.citizen.browser.settings import ISettings

import cpskin.citizen


class CpskinCitizenLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=cpskin.citizen, name="testing.zcml")
        z2.installProduct(app, "imio.dashboard")
        z2.installProduct(app, "Products.DateRecurringIndex")

    def setUpPloneSite(self, portal):
        applyProfile(portal, "Products.CMFPlone:plone")
        applyProfile(portal, "cpskin.citizen:testing")

        manager = api.user.create(
            email="manager@manager.com", username="manager", password="manager"
        )
        api.user.grant_roles(user=manager, roles=("Manager",))

        citizen = api.user.create(
            email="citizen@citizen.com", username="citizen", password="citizen"
        )
        citizen.setMemberProperties(mapping={"fullname": u"Céline Dupont"})
        newcitizen = api.user.create(
            email="newcitizen@citizen.com", username="newcitizen", password="citizen"
        )
        newcitizen.setMemberProperties(mapping={"fullname": "Jean Dupont"})
        api.group.add_user(groupname="Citizens", user=citizen)
        api.group.add_user(groupname="Citizens", user=newcitizen)

        login(portal, "manager")
        api.content.create(
            type="Document",
            id="citizen-document",
            title="Citizen Document",
            container=portal,
            citizens=["citizen"],
        )
        api.content.create(
            type="Document",
            id="citizens-document",
            title="Citiznes Document éàç",
            container=portal,
            citizens=["citizen", "newcitizen"],
        )
        api.content.create(
            type="Document", id="document", title="Document", container=portal
        )
        document = api.content.create(
            type="Document",
            id="claim-document",
            title="Claim Document",
            container=portal,
        )
        annotations = IAnnotations(document)
        annotations[ANNOTATION_KEY] = PersistentDict()
        annotations[ANNOTATION_KEY]["claim"] = ["citizen"]

        obj = api.content.create(
            type="Folder", id="documents", title="Documents", container=portal
        )
        api.content.transition(obj=obj, transition="publish")

        api.portal.set_registry_record(
            name="creation_types", value=["Document"], interface=ISettings
        )

        logout()
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, "imio.dashboard")
        z2.uninstallProduct(app, "Products.DateRecurringIndex")


CPSKIN_CITIZEN_FIXTURE = CpskinCitizenLayer()


CPSKIN_CITIZEN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CPSKIN_CITIZEN_FIXTURE,), name="CpskinCitizenLayer:IntegrationTesting"
)


CPSKIN_CITIZEN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CPSKIN_CITIZEN_FIXTURE,), name="CpskinCitizenLayer:FunctionalTesting"
)


CPSKIN_CITIZEN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(CPSKIN_CITIZEN_FIXTURE, REMOTE_LIBRARY_BUNDLE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CpskinCitizenLayer:AcceptanceTesting",
)


class BaseTestCase(unittest.TestCase):
    @property
    def portal(self):
        return self.layer["portal"]

    @property
    def citizen_document(self):
        return self.portal["citizen-document"]

    @property
    def citizens_document(self):
        return self.portal["citizens-document"]

    @property
    def claim_document(self):
        return self.portal["claim-document"]

    @property
    def document(self):
        return self.portal["document"]

    @property
    def documents(self):
        return self.portal["documents"]

    @property
    def dashboards(self):
        return self.portal["citizen-dashboard"]

    @property
    def drafts(self):
        return self.portal["citizen-drafts"]


class TestCreationFolderAdapter(CitizenCreationFolderAdapter):
    def get_folder(self, navigation_root, portal_type):
        return navigation_root["documents"]
