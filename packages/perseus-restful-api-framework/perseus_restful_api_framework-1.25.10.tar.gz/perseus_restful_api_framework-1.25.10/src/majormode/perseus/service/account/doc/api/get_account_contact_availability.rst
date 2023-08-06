=======================================
``GET /account/(contact)/availability``
=======================================

--------
Synopsis
--------

Indicate whether the specified contact is available.  In the case it
would have been already registered by a user, indicate whether this
contact has been verified.


------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/account/(contact)/availability?value=...


---------------------
Request Header Fields
---------------------

.. include:: /_include/optional_authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

* ``contact`` (required): name of the contact's property, which can
  be one of a set of pre-defined strings such as:

  * ``email``: e-mail address.

  * ``phone``: phone number in E.164 numbering plan, an ITU-T
    recommendation which defines the international public
    telecommunication numbering plan used in the Public Switched
    Telephone Network (PSTN).


------------------------
Request Query Parameters
------------------------

* ``value`` (required): value of the property representing by a
  string, such as ``+84.01272170781``, the formatted value for a
  telephone number property.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON data::

    {
      "is_available": boolean,
      "is_verified": boolean
    }

where:

* ``is_available``: ``true`` if the specified contact is not
  registered by any existing account; ``false`` otherwise.

* ``is_verified``: ``true`` if the specified contact has been
  registered and verified; ``false`` otherwise.


----------
Exceptions
----------

None.
