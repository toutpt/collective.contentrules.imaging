import transaction
import unittest2 as unittest
from collective.contentrules.imaging import testing
from plone import api
from urllib import urlopen
from StringIO import StringIO


class UnitTestCase(unittest.TestCase):

    def setUp(self):
        pass


class IntegrationTestCase(unittest.TestCase):

    layer = testing.INTEGRATION

    def login(self):
        testing.login(self.portal, testing.TEST_USER_NAME)

    def logout(self):
        testing.logout()

    def setRole(self, role):
        if role:
            testing.setRoles(self.portal, testing.TEST_USER_ID, [role])

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        self.login()
        self.setRole('Manager')
        self.folder = api.content.create(type='Folder',
                                         title='test folder',
                                         container=self.portal)

    def getImage(self, size='680'):
        data = urlopen('http://dummyimage.com/%s' % size).read()
        return data

    def assertImage(self, data, format, size):
        import PIL.Image
        image = PIL.Image.open(StringIO(data))
        self.assertEqual(image.format, format)
        self.assertEqual(image.size, size)

    def getScales(self, image):
        from plone.scale.storage import AnnotationStorage
        storage = AnnotationStorage(image)
        return storage.storage

    def createImage(self, container, size):
        data = self.getImage(size)
        image = container[container.invokeFactory('Image',
                                                  id='foo',
                                                  image=data)]
        return image


class FunctionalTestCase(IntegrationTestCase):

    layer = testing.FUNCTIONAL

    def setUp(self):
        #we must commit the transaction
        transaction.commit()
