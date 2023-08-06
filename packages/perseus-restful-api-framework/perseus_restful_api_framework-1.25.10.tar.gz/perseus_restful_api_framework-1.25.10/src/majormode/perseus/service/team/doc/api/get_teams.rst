=============
``GET /team``
=============

--------
Synopsis
--------

Return a list of teams which names match, even partially, the
specified keywords.


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

* ``keywords`` (required): a comma separated list of keywords, up to
  ``16`` are allowed in a single request.

* ``limit`` (optional): constrain the number of teams that are
  returned to the specified number.  If not specified, the default
  value is ``20``. The maximum value is ``100``.

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
        "account_id" string,
        "creation_time": timestamp,
        "description": string,
        "name": string,
        "picture_id": string,
        "picture_url": string,
        "team_id": string,
        "update_time": timestamp
      },
      ...
    ]

where:

* ``account_id`` (required): identification of the account of the
  agent of this team.

* ``creation_time`` (required): string representation, expressed in
  accordance with RFC 3339, of the time when the team has been
  registered.

* ``description`` (optional): a short textual description of the
  team, if any provided.

* ``name`` (required): the name of the team.

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

* ``team_id`` (required): identification of a team the specified
  user is member of.

* ``update_time`` (required): time of the last modification of one
  or more attributes of this photo.

.. note::

   This time should be used by the client application to manage its
   cache of teams and to reduce the average time to access data of
   teams. When the client application needs to read teams'
   attributes, it first checks whether a copy of these data is in its
   cache.  If so, the client application immediately reads from the
   cache, which is much faster than requesting these data from the
   server platform.


----------
Exceptions
----------

None.
