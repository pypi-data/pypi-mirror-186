======================================
``GET /account/username/availability``
======================================

--------
Synopsis
--------

Indicate whether the specified username is available or not.


------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/account/username/availability?value=...


---------------------
Request Header Fields
---------------------

.. include:: /_include/optional_authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

None.


------------------------
Request Query Parameters
------------------------

* ``value`` (required): a username to check whether it is already
  registered by an existing user or not.  A username is unique across
  the platform.  A username is not case sensitive.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON data::

    {
      "data": boolean
    }

where:

* ``data``: ``true`` if the username is not registered by any
  existing account; ``false`` otherwise.


----------
Exceptions
----------

None.
