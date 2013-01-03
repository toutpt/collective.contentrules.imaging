from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-collective.contentrules.imaging:default'


def common(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
