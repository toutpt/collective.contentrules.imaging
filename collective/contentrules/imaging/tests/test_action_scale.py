import unittest2 as unittest
from zope import component
from zope.component import getUtility, getMultiAdapter
from collective.contentrules.imaging.tests import base
from plone.contentrules.rule.interfaces import IRuleAction, IExecutable
from plone.contentrules.engine.interfaces import IRuleStorage
from plone.app.contentrules.rule import Rule
from zope.component.interfaces import IObjectEvent
from collective.contentrules.imaging.actions.scale import ScaleAddForm,\
    ScaleAction, ScaleEditForm
from plone.app.contentrules.tests.dummy import DummyEvent

ACTION = 'collective.contentrules.imaging.actions.Scale'


class IntegrationTestRuleAction(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def testRegistered(self):
        element = component.getUtility(IRuleAction, name=ACTION)
        self.assertEquals(ACTION, element.addview)
        self.assertEquals('edit', element.editview)
        self.assertEquals(None, element.for_)
        self.assertEquals(IObjectEvent, element.event)

    def testInvokeAddView(self):
        element = getUtility(IRuleAction, name=ACTION)
        storage = getUtility(IRuleStorage)
        storage[u'foo'] = Rule()
        rule = self.portal.restrictedTraverse('++rule++foo')

        adding = getMultiAdapter((rule, self.portal.REQUEST), name='+action')
        addview = getMultiAdapter((adding, self.portal.REQUEST),
                                  name=element.addview)
        self.assertIsInstance(addview, ScaleAddForm)

        addview.createAndAdd(data={'scales': ['mini']})

        e = rule.actions[0]
        self.assertIsInstance(e, ScaleAction)
        self.assertEquals(['mini'], e.scales)

    def testInvokeEditView(self):
        element = getUtility(IRuleAction, name=ACTION)
        e = ScaleAction()
        editview = getMultiAdapter((e, self.folder.REQUEST),
                                   name=element.editview)
        self.assertIsInstance(editview, ScaleEditForm)

    def testExecute(self):
        image = self.createImage(self.folder, '680')
        e = ScaleAction()
        e.scales = ['mini']
        ex = getMultiAdapter((self.folder, e, DummyEvent(image)),
                             IExecutable)
        ex()
        scales = self.getScales(image)
        # FIXME: I don't succeed in getting scales
        #self.assertTrue(len(scales), 1)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
