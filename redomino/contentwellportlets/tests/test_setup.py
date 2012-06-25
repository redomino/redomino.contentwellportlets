# Following page 73 of Professional Plone Development by Martin Aspeli
# Requires that the base.py file exists

import unittest
from redomino.contentwellportlets.tests.base import ContentWellPortletsTestCase

class TestSetup(ContentWellPortletsTestCase):
    """
    Check whether product is installed correctly
    """
    
    def afterSetUp(self):
        pass

    def testCSSregistered(self):
        """
        Is our stylesheet registered?
        """
        self.failUnless('++resource++ContentWellPortlets.styles/ContentWellPortlets.css' in self.portal.portal_css.getResourceIds(), 'Cannot find CSS')
        
    def testInterfaceAvailable(self):
        """
        Is our product-specific interface available?
        """
        from plone.browserlayer import utils
        from redomino.contentwellportlets.browser.interfaces import IContentWellPortlets
        self.failUnless(IContentWellPortlets in utils.registered_layers(), 'Cannot find IContentWellPortlets interface')
    
    def testPortletManagers(self):
        """
        Are our portlet managers available? Test by inserting a calendar portlet
        """
        from zope.component import getUtility, getMultiAdapter
        from plone.app.portlets.portlets import calendar
        from plone.portlets.interfaces import IPortletManager
        from plone.portlets.interfaces import IPortletRenderer

        # get the portlet managers we should have created
        managerAbove = getUtility(IPortletManager, name='ContentWellPortlets.AbovePortletManager1',context=self.portal)
        managerBelow = getUtility(IPortletManager, name='ContentWellPortlets.BelowPortletManager1',context=self.portal)
        managerFooter = getUtility(IPortletManager, name='ContentWellPortlets.FooterPortletManager1',context=self.portal)
        
        # try rendering a portlet with it using getMultiAdapter((context, request, view, manager, assignment), Interface)
        renderer = getMultiAdapter((self.folder, self.folder.REQUEST, self.folder.restrictedTraverse('@@plone'), managerAbove, calendar.Assignment()), IPortletRenderer)
        self.failUnless(isinstance(renderer, calendar.Renderer), 'Cannot render portlet above contents')
        
        renderer = getMultiAdapter((self.folder, self.folder.REQUEST, self.folder.restrictedTraverse('@@plone'), managerBelow, calendar.Assignment()), IPortletRenderer)
        self.failUnless(isinstance(renderer, calendar.Renderer), 'Cannot render portlet below contents')
        
        renderer = getMultiAdapter((self.folder, self.folder.REQUEST, self.folder.restrictedTraverse('@@plone'), managerFooter, calendar.Assignment()), IPortletRenderer)
        self.failUnless(isinstance(renderer, calendar.Renderer), 'Cannot render footer portlet contents')
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
