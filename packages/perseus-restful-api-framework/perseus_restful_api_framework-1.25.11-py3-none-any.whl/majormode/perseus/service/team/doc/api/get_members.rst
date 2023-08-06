=====================================
``GET /team/(team_id:string)/member``
=====================================

--------
Synopsis
--------

Return the list of the members of an team.

.. note::

   only an administrator of an team is allowed to get members of the
   team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``team_id``: identification of the team to return the list of
  members.

------------------------
Request Query Parameters
------------------------

* ``limit`` (optional): constrain the number of members that are
  returned to the specified number.  If not specified, the default
  value is ``20``.  The maximum value is ``100``.

* ``offset`` (optional): require to skip that many members before
  beginning to return memberships.  If not specified, the default
  value is ``0``.

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
        "account_id": string,
        "creation_time": timestamp
        "email_address": string,
        "fullname": string,
        "object_status": integer,
        "picture_id": string,
        "picture_url": string,
        "timezone": integer,
        "update_time": timestamp,
        "username": string
      },
      ...
    ]

where:

* ``account_id`` (required): identification of the account of a
  member.

* ``creation_time`` (required): string representation, expressed in
  accordance with RFC 3339, of the time when the member became member
  of the team.

* ``fullname`` (required): complete full name of the user as given
  by the user himself, i.e., untrusted information.

* ``locale``: tag respecting RFC 4646, which identifies the
  preferred language of the user, or English by default.  A locale is
  expressed by a ISO 639-3 alpha-3 code element, optionally followed
  by a dash character ``-`` and a ISO 3166-1 alpha-2 code. For
  example: ``eng`` (which denotes a standard English), ``eng-US``
  (which denotes American English).

* ``object_status`` (required): current status of the member:

   * ``0``: this user is a member of the team.

   * ``1``: this user is not a member of the team anymore; either
     he has withdrawn his membership, either he has been revoked from
     the team by an administrator.

   * ``2``: the membership of this user has been suspended by an
     administrator.

   * ``3``: this user has been invited to join the team but he
     didn't accept or decline the invitation yet.

   * ``4``: this user has declined the invitation to join the
     team.

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

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``DeletedObjectException``: if the team has been deleted.

* ``DisabledObjectException``: if the team has been disabled.

* ``IllegalAccessException``: if the user on behalf of the request
  is sent is not an administrator of the team.

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
