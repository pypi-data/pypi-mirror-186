=====================
``POST /application``
=====================

--------
Synopsis
--------

Register a new application.

========================= ====
Information
========================= ====
Rate Limited?	          No
Requires Authentication?  Yes
Response Formats          JSON
HTTP Methods              POST
========================= ====

------------
Resource URL
------------

http://api.majormode.com/application

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

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
      "stage": string,
      "platform": string,
    }

where:

* ``name`` (required): name of the application. Localization is not supported.

* ``description`` (required): textual description of the application.

* ``stage`` (optional): current status of the application, also known as the `environment stage <http://en.wikipedia.org/wiki/Development_environment>`_, which designs to a specific stage in a release process:

  * ``sandbox``: development environment, also known as *sandbox*.  While in development, all accounts created are not test accounts only.
  * ``live``: production environment, also known as *live*.

* ``platform`` (required): type of the application:

  * ``web``
  * ``desktop``
  * ``mobile``

  If the application qualifies as more than one type, the developer should create a new application for each one.

---------------------
Response Message Body
---------------------

The platform returns the following JSON structure::

    {
      "app_id": string,
      "api_key": string,
      "secret_key": string
    }

where:

* ``app_id`` (required): the identification of the client application unique among the platform.

* ``api_key`` (required): the Application Programming Interface (API) key, which uniquely identifies the client application.  The registered developers of this client application can request a new API key if they consider that their API key has been hacked.

* ``secret_key`` (required): a string kept secret, which is used to authenticate the API key.
