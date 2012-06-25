from zope.interface import Interface
from plone.portlets.interfaces import IPortletManager
from plone.app.portlets.interfaces import IColumn

class IContentWellPortlets(Interface):
    """
    A layer specific to this product. Is registered using browserlayer.xml
    """

class IContentWellPortletManager(IPortletManager, IColumn):
    """
    Superclass used by our adapter
    The IColumn bit means that we can add all the portlets available to 
     the right-hand and left-hand column portlet managers
    """
class IHeaderPortlets(IContentWellPortletManager):
     """
     For the portlet manager above the content area.
     """
    
class IPortletsAboveContent(IContentWellPortletManager):
     """
     For the portlet manager above the content area.
     """

class IPortletsBelowContent(IContentWellPortletManager):
     """
     For the portlet manager below the content area.
     """

class IFooterPortlets(IContentWellPortletManager):
     """
     For the portlet manager in the footer area.
     """
