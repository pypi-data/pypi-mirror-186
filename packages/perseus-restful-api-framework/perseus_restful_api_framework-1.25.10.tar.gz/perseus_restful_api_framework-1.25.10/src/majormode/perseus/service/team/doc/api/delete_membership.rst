============================================
``DELETE /team/(team_id:string)/membership``
============================================

--------
Synopsis
--------

Withdraw the membership of a user from a team on behalf of this user.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``team_id``: identification of the team the user withdraws his
  membership from.

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

* ``DeletedObjectException``: if the team has been deleted.

* ``DisabledObjectException``: if the team has been disabled.

* ``IllegalAccessException``: if the user on behalf of the member is
  requested to be revoked from the team is not an administrator of
  the team.

* ``InvalidOperationException``: if the specified user account is
  not a member of the team or if the specified user account is the
  agent of the specified team -- his role cannot be revoked expect by
  using the method :doc:``put_master``.

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
