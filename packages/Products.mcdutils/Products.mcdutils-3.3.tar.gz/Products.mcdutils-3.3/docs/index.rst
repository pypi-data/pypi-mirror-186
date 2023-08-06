.. _index:

Documentation for Products.mcdutils
===================================
The `Products.mcdutils` product supplies a replacement for the ZODB-based
session data container supplied by the `Transience` product, shipped with
the Zope core prior to Zope 4 and available as a separate package after that.
Rather than using a ZODB storage as the backing store for session data, as
`Transience` does, `Products.mcdutils` stores session data in a cluster of
one or more `memcached` servers.



API documentation
-----------------
Programming interfaces provided by :mod:`Products.mcdutils`.

.. toctree::
   :maxdepth: 2

   api


Narrative documentation
-----------------------
Narrative documentation explaining how to use :mod:`Products.mcdutils`.

.. toctree::
    :maxdepth: 2

    installation
    development
    usage_zmi
    resources
    changes


Indices and tables
------------------
* :ref:`genindex`
* :ref:`search`
* :ref:`glossary`

