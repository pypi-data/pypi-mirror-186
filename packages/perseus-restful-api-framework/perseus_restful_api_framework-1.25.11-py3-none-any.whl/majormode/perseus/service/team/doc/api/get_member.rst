==================================================
``GET /team/(team_id:string)/member/(account_id)``
==================================================

--------
Synopsis
--------

Return extended information about the account of a user who belongs to
the specified team.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

* ``account_id``: identification of the account a user who is member
  of the specified team.

* ``team_id``: identification of a team the specified member belongs
  to.


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

The platform returns the following JSON form::


    {
      "account_id": string,
      "creation_time": timestamp,
      "fullname": string,
      "is_administrator": booleans,
      "picture_id": string,
      "picture_url": string,
      "timezone": integer,
      "update_time": timestamp,
      "username": string
    }

where:

* ``account_id`` (required): identification of the account of a
  member.

* ``creation_time`` (required): time when the member became member
  of the team.

* ``fullname`` (required): complete full name of the user as given
  by the user himself, i.e., untrusted information.

* ``is_administrator``: indicate whether the user is an
  administrator of this team.


* ``locale``: tag respecting RFC 4646, which identifies the
  preferred language of the user, or English by default.  A locale is
  expressed by a ISO 639-3 alpha-3 code element, optionally followed
  by a dash character ``-`` and a ISO 3166-1 alpha-2 code. For
  example: ``eng`` (which denotes a standard English), ``eng-US``
  (which denotes American English).

* ``picture_id`` (optional): identification of the user account's
  picture, if any picture defined for this user account.

* ``picture_url`` (optional): Uniform Resource Locator (URL) that
  specifies the location of the user account's picture, if any
  defined.  The client application can use this URL and append the
  query parameter ``size`` to specify a given pixel resolution of the
  user account's picture, such as:

  * ``thumbnail``

  * ``small``

  * ``medium``

  * ``large``

* ``timezone`` (optional): time zone of the default location of the
  user. It is the difference between the time at this location and
  UTC (Universal Time Coordinated).  UTC is also  known as GMT or
  Greenwich Mean Time or Zulu Time.

* ``update_time`` (required): time when the information of this user
  account has been updated for the last time.

* ``username`` (optional): name of the account of the user, if any
  defined.


.. note::

   If the user doesn't belong to the specified team, the platform
   returns nothing.


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``DeletedObjectException``: if the team has been deleted.

* ``DisabledObjectException``: if the team has been disabled.

* ``IllegalAccessException``: if the user on behalf of the request
  is sent is not a member of this team.

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
