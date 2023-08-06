==================================================
``DELETE /team/invitation/(invitation_id:string)``
==================================================

--------
Synopsis
--------

Cancel an invitation that has been sent to a user to join a team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``invitation_id``: the identification of the invitation to be
  canceled.

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

None.

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``IllegalAccessException``: if the user on behalf of the operation
  is performed is not an administrator of the team from which the
  invitation has been issued.

* ``UndefinedObjectException``: if no invitation corresponds to the
  specified identification.
