from plone.app.testing import *


class MyLayer(PloneSandboxLayer):
#    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.contentrules.imaging
        self.loadZCML(package=collective.contentrules.imaging)

FIXTURE = MyLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                       name="collective.contentrules.imaging:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                       name="collective.contentrules.imaging:Functional")
