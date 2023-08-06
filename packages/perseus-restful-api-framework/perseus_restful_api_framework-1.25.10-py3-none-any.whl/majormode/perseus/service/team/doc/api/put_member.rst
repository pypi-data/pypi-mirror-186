=========================================================
``PUT /team/(team_id:string)/member/(account_id:string)``
=========================================================

--------
Synopsis
--------

Update the role of a member of an team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``account_id``: identification of the account of the user to
  change his role in the team.

* ``team_id``: identification of the team to promote the specified
  account as the new master administrator.

------------------------
Request Query Parameters
------------------------

None.

--------------------
Request Message Body
--------------------

The request must contains a JSON form that corresponds to the required
information::

    {
      "is_administrator": boolean
    }

where:

* ``is_administrator`` (required): indicate whether the specified
  user account is an administrator of the team.

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

* ``IllegalAccessException``: if the user on behalf of the role of
  the specified member is updated is not an administrator of the team.

* ``InvalidOperationException``: if the specified user account is
  not a member of the team, if his current role is already this
  passed to the function, or if the specified user account is the
  master administrator of the team (his role cannot be changed except
  by using the request :doc:`put_master`).

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
