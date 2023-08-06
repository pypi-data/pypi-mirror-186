=============
``GET /team``
=============

--------
Synopsis
--------

Return a list of teams the authenticated user is member of.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

None.


------------------------
Request Query Parameters
------------------------

* ``limit``: constrain the number of teams that are returned to the
  specified number.  If not specified, the default value is ``20``.
  The maximum value is ``100``.

* ``offset`` (optional): require to skip that many teams before
  beginning to return teams.  If not specified, the default value is
  ``0``.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON form::

    [
      {
        "team_id": string,
        "name": string,
        "description": string,
        "account_id" string,
        "picture_id": string,
        "picture_url": string,
        "creation_time": timestamp
      },
      ...
    ]

where:

* ``team_id`` (required): identification of a team the specified
  user is member of.

* ``name`` (required): the name of the team.

* ``description`` (optional): a short textual description of the
  team, if any provided.

* ``account_id`` (required): identification of the account of the
  agent of this team.

* ``picture_id`` (optional): identification of the picture that
  represents the team, if any picture defined.

* ``picture_url`` (optional): Uniform Resource Locator (URL) that
  specifies the location of the picture representing the team, if any
  defined. The client application can use this URL and append the
  query parameter ``size`` to specify a given pixel resolution of the
  user account's picture:

  * ``thumbnail``

  * ``small``

  * ``medium``

  * ``large``

* ``creation_time`` (required): string representation, expressed in
  accordance with RFC 3339, of the time when the team has been
  registered.


----------
Exceptions
----------

None.
