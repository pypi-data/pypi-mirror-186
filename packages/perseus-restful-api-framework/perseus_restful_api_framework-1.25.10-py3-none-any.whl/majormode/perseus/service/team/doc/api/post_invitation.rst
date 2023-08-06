==========================================
``POST /team/(team_id:string)/invitation``
==========================================

--------
Synopsis
--------

Invite a list of users to join the specified team.  The platform will
eventually send them an invitation, either by an email or an in-app
notification.  Their membership is pending until they accept or
decline the invitation.

.. note::

   only an administrator of the team is allowed to invite members to
   join a team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``team_id``: identification of the team to invite members to join.

------------------------
Request Query Parameters
------------------------

None.

--------------------
Request Message Body
--------------------

The request must contain a list of email addresses or identification
of account of users to invite to the team::

    [ string, ... ]

---------------------
Response Message Body
---------------------

The platform returns the list of email addresses of users that have
been invited to join the team, filtered out from email addresses of
users that are already members of the team, those of users that have
been already invited to join this team but have not yet replied, and
the email addresses of users whose accounts have been deleted::

    [ string, ... ]

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``DeletedObjectException``: if the team has been deleted.

* ``DisabledObjectException``: if the team has been disabled.

* ``IllegalAccessException``: if the user on behalf of whom users
  are invited to join the team is not an administrator of the team.

* ``InvalidArgumentException``: if some email addresses are of a
  wrong format, i.e., not compliant with RFC 2822, or if some account
  identifications are invalid.

* ``InvalidOperationException``: if no invite URL for accepting or
  declining invitation has been defined for this team.

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
