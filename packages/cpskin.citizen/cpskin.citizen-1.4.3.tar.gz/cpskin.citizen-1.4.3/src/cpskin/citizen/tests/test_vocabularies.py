# -*- coding: utf-8 -*-
"""
cpskin.citizen
--------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from cpskin.citizen import testing


class TestVocabularies(testing.BaseTestCase):
    layer = testing.CPSKIN_CITIZEN_INTEGRATION_TESTING

    def _get_vocabulary_values(self, name):
        vocabulary = getUtility(IVocabularyFactory, name=name)(self.portal)
        return [t.value for t in vocabulary]

    def test_citizen_vocabulary(self):
        """Test 'CitizenVocabulary'"""
        voc = self._get_vocabulary_values("cpskin.citizen.citizens")
        self.assertListEqual(sorted(["citizen", "newcitizen"]), sorted(voc))

    def test_citizen_portal_types_vocabulary(self):
        """Test 'CitizensPortalTypesVocabulary'"""
        voc = self._get_vocabulary_values("cpskin.citizen.portal_types")
        self.assertListEqual(
            sorted(["Document", "News Item", "Event", "organization"]), sorted(voc)
        )

    def test_citizen_creation_types_vocabulary(self):
        """Test 'CitizensAllowedCreationTypesVocabulary'"""
        voc = self._get_vocabulary_values(
            "cpskin.citizen.allowed_creation_portal_types"
        )
        self.assertListEqual(sorted(["Document"]), sorted(voc))
