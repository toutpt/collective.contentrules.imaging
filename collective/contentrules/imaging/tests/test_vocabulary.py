import unittest2 as unittest
from zope import component
from collective.contentrules.imaging.tests import base
from zope.schema.interfaces import IVocabularyFactory


class IntegrationTestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_scales_vocabulary(self):
        name = "collective.contentrules.imaging.vocabularies.Scales"
        factory = component.queryUtility(IVocabularyFactory, name)
        vocab = factory(self.portal)
        self.assertEqual(len(vocab), 7)
        self.assertEqual(vocab.getTerm('mini').title, u'mini')
        self.assertEqual(vocab.getTerm('mini').token, 'mini')
        self.assertEqual(vocab.getTerm('mini').value, 'mini')


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
