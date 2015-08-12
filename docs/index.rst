.. eduextractor documentation master file, created by
   sphinx-quickstart on Mon Aug 10 17:16:14 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to eduextractor's documentation!
========================================

Contents:

.. toctree::
   :maxdepth: 2

Eduextractor is a python package designed to help extract and transform data that is related to education vendors in the United States. It is part of the [OpenEduConnect](http://openeduconnect.org) stack. 

Currently, eduextractor supports two backend to load data from. Powerschool and the NWEA Map exam. More sources are coming soon. 

To install, simply run `pip install eduextractor`. To configure, you'll need a file at `~/eduextractor.yml` that contains login creditials for the various backends. Here is a sample: 

.. code-block:: guess
nwea_map:
  url: your_nwea_map_site.org 
  username: your_user_name
  secret: your_password
  dest: '/path/to/dump/the/files/'


powerschool:
  frontend:
    username: username_for_ps_frontend 
    password: pw_for_ps_frontend
    url: your_powerschool_url
    postfix: /admin 
  admin:
    username: custom_content_username
    password: custom_content_password
    postfix: /powerschool-sys-mgmt

Once that is configured, run `eduextractor` on the command line with the various options to extract your data. 


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

