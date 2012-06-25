Overview
========

* This product enables you to put portlets in places other than right and left
  columns, specifically:
  
  * Underneath global nav but above portal-columns so it spans the width of the page
  * above the main heading (h1) of the page
  * at the base of the page, above the footer
  * in the footer well
  
  In each area, you can add up to three columns of portlets. 

* You should use CSS (in the custom folder in portal_skins, or in your own
  theme product) to configure how these portlets should appear relative to
  each other and to the content.

* This may allow you to create distinctive layouts for pages, folders etc
  without having to write new zope page templates

To install the product
======================
* See docs/INSTALL.TXT for instructions


To add portlets above the content
=================================
1. Log into your Plone site as a Manager (or someone else with the "Portlets:
   Manage portlets" permission)
2. Go to the place in your site where you want portlets. For example:
   * If you want portlets on your home page only, go to http://yourSiteURL/front-page
   * If you want portlets on your entire site, go to http://yourSiteURL
3. Bring up a management page by either
   (a) Clicking the "add, edit or remove portlets link" [*]_; or
   (b) Adding "/@@manage-portletsabovecontent" to the end of the URL and hitting "return"
4. You should see a management page entitled "Manage Portlets Above Content"
   This gives you the option to add portlets in one or more of three columns: A, B and C
   You can add as many portlets in each column as you like
   Other commands (reordering, hiding, blocking portlets) are the same as for
   the right and left columns

.. [*] Note: if you are in a folder that has a default page, this will take
       you to a screen where you can add portlets to that page. If you want to add
       portlets to all the pages in the folder, make sure you are on the folder
       rather than the default page (e.g. by clicking the "contents" tab) before
       clicking the link.

To add portlets below the content
=================================
Follow the above instructions, but instead of clicking the "add, edit or
remove portlets above content" link or adding /@@manage-portletsabovecontent
to the URL:

 (a) Click the "add, edit or remove portlets below the content" link; or
 (b) Add /@@manage-portletsbelowcontent to the end of the URL


Technical details
=================

* The product adds two new viewlets; within each of these are three portlet
  managers (specified in portlets.xml) For details of exactly which viewlet
  managers these viewlets slot into:
  
  * see configure.zcml in Products/ContentWellPortlets/browser
  * or install the product, go to your Plone site and add /@@manage-viewlets to the URL
