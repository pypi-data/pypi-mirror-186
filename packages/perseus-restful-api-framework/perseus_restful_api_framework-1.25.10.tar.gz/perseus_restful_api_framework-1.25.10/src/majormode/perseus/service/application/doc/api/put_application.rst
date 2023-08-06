=====================
``PUT /application``
=====================

--------
Synopsis
--------

Update some modifiable properties of the specified client application.

========================= ====
Information
========================= ====
Rate Limited?	          No
Requires Authentication?  Yes
Response Format           JSON
HTTP Methods              PUT
========================= ====

------------
Resource URL
------------

http://api.majormode.com/application/(app_id:string)

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``api_id`` (required): identification of the client application for which some properties are updated.

------------------------
Request Query Parameters
------------------------

None.

--------------------
Request Message Body
--------------------

The request must contains a JSON form that corresponds to the required information::

    {
      "name": string,
      "description": string,
      "platform": string
    }

where:

* ``name`` (required): name of the application. Localization is not supported.

* ``description`` (required): textual description of the application.

* ``platform`` (required): type of the application:

  * ``web``
  * ``desktop``
  * ``mobile``

---------------------
Response Message Body
---------------------

None.

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one or several required conditions have not been respected:

* ``DeletedObjectException``: if the client application has been deleted.

* ``DisabledObjectException``: if the client application has been disabled.

* ``IllegalAccessException``: if the user on behalf of some properties of the client application are modified is not the master administrator or one of the regular administrators of this application.

* ``UndefinedObjectException``: if the specified identification doesn't refer to a client application registered against the platform.
