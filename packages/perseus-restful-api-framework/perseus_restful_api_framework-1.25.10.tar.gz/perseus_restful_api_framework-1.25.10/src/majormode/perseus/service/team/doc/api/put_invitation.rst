=================================================
``PUT /team/invitation/(invitation_code:string)``
=================================================

--------
Synopsis
--------

Accept or decline on behalf of a user an invitation to join a team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/anonymous_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``invitation_code``: a code representing an invitation sent to a
  user to join a team.

------------------------
Request Query Parameters
------------------------

* ``does_accept`` (required): indicate whether the user accepts or
  declines the invitation to join the team.

--------------------
Request Message Body
--------------------

None.

---------------------
Response Message Body
---------------------

None.

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``DeletedObjectException``: if the team has been deleted.

* ``DisabledObjectException``: if the team has been disabled.

* ``IllegalAccessException``: if the  invitation code is of a wrong
  format, or if the invitation code has been corrupted.

* ``InvalidOperationException``: if the account of the user invited
  to the team is of a wrong type.

* ``UndefinedObjectException``: if the specified code doesn't
  corresponds to any invitation.
