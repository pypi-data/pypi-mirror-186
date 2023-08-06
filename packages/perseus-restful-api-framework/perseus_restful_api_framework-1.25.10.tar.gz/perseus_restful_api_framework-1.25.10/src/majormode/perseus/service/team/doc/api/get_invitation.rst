=========================================
``GET /team/(team_id:string)/invitation``
=========================================

--------
Synopsis
--------

Return the list of invitations that have been sent to users to join
the specified team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``team_id``: identification of the team to return the list of
  invitations that have been sent to some users to join this team..

------------------------
Request Query Parameters
------------------------

* ``limit`` (optional): constrain the number of member requests that
  are returned to the specified number.  If not specified, the
  default value is ``20``.  The maximum value is ``100``.

* ``offset`` (optional): require to skip that many member requests
  before beginning to return membership requests.  If not specified,
  the default value is ``0``.

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
        "invitation_id": string,
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

* ``invitation_id`` (required): identification of the invitation
  sent to this user to join the team.

* ``locale`` (required): tag respecting RFC 4646, which identifies
  the preferred language of the user, or English by default.  A
  locale is expressed by a ISO 639-3 alpha-3 code element, optionally
  followed by a dash character ``-`` and a ISO 3166-1 alpha-2 code.
  For example: ``eng`` (which denotes a standard English), ``eng-US``
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

* ``update_time`` (required): string representation, expressed in
  accordance with RFC 3339, of the time of the last modification of
  the attributes of the member's account.

* ``username`` (optional): name of the account of the user, if any
  defined.

----------
Exceptions
----------

None.
