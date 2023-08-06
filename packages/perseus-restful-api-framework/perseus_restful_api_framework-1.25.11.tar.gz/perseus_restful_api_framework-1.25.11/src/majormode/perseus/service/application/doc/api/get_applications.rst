====================
``GET /application``
====================

--------
Synopsis
--------

Retrieve extended information about the client applications that the
end user on behalf of this function is called has access to, either
as an individual, either as a member of a team.

========================= ====
Information
========================= ====
Rate Limited?             No
Requires Authentication?  Yes
HTTP Methods              GET
========================= ====

------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/applications

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

None.

---------------------
Response Message Body
---------------------

The platform returns the following JSON structure::

    [
      {
        "account_id": string,
        "api_key": string,
        "app_id": string,
        "name": string,
        "creation_time": timestamp,
        "description": string,
        "logo_url": string,
        "object_status": integer,
        "platform": string,
        "secret_key": string,
        "stage": string,
        "team": {
          "name": string,
          "picture_id": string,
          "picture_url": string,
          "team_id": string
        },
        "update_time": timestamp,
      },
    ]

where:

* ``account_id`` (required): identification of the account of the
  user who registered this client application.

* ``api_key`` (required): the Application Programming Interface
  (API) key, which uniquely identifies the client application.  The
  registered developers of this client application can request a new
  API key if they consider that their API key has been hacked.

* ``app_id`` (required): the identification of the client
  application unique among the platform.

* ``creation_time`` (required): time when the application has been
  registered.

* ``description`` (optional): a short textual description of the
  client application, if any provided.

* ``logo_url`` (optional): Uniform Resource Locator (URL) of the
  logo of the client application, if any provided.

* ``members`` (optional): the list of developers or administrators
  linked to this applications.  Each entry contains the following
  attributes:

  * ``account_id``: identification of a user account.

  * ``fullname``: full name of the user.

  * ``is_administrator``: indicate if the user is an administrator
    of the team this application belongs to.

  * ``picture_id``: identification of the picture of the user
    account.

  * ``picture_url``: Uniform Resource Locator (URL) that specifies
    the location of the picture of this user account, if any defined.
    The client application can use this URL and append the query
    parameter ``size`` to specify a given pixel resolution of the
    user account's picture:

    * ``thumbnail``

    * ``small``

    * ``medium``

    * ``large``

* ``name`` (required): the title of the client application.

* ``object_status`` (required): current status of the application.

* ``platform`` (required): identification of the platform on which
  the client application runs, which can be one of a set of
  pre-defined strings such as:

  * ``android``
  * ``iphone``
  * ``ipad``
  * ``ipod touch``
  * ``blackberry``
  * ``windows 7``
  * ``web mobile``
  * ``desktop``

* ``secret_key`` (required): a string kept secret, which is used to
  authenticate the API key.

* ``stage`` (required): logical name of the environment stage which
  the client application is deployed onto.  Environment stages are
  simplified to the followings:

  * ``sandbox``

  * ``live``

* ``team`` (optional): extended information about the team which
  this client application belongs to, if any:

  * ``name`` (required): name of the team.

  * ``picture_id`` (optional): identification of the picture that
    represents this team, if any defined.

  * ``picture_url`` (optional): Uniform Resource Locator (URL)
    that specifies the location of the picture that represents this
    team, if any defined. The client application can use this URL and
    append the query parameter ``size`` to specify a given pixel
    resolution of the team's picture:

    * ``thumbnail``

    * ``small``

    * ``medium``

    * ``large``

  * ``team_id``: identification of the team.

* ``update_time`` (required): most recent time when some
  information, such as the name or the description of the client
  application, or the API key, has been modified.
