========================================================
``PUT /team/(team_id:string)/agent/(account_id:string)``
========================================================

--------
Synopsis
--------

Promote an administrator as the new agent of the team.

The person that is assigned as the new agent must have the legal
authority to bind the company/organization to the platform legal
agreements.

.. note::

   Only the current agent of this team can promote another
   administrator of the team to become the agent of this team.

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

----------------
Request URL Bits
----------------

* ``account_id``: identification of the account of the user who is
  promoted as the new agent of the team.  This user MUST have the
  role of administrator.

* ``team_id``: identification of the team to promote the specified
  account as the new agent.

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

* ``DeletedObjectException``: if the team has been deleted, or if
  the specified account to be promoted as the new agent of the team
  has been deleted.

* ``DisabledObjectException``: if the team has been disabled, or if
  the specified account to be promoted as the new agent of the team
  has been disabled.

* ``IllegalAccessException``: if the account of the user on behalf
  of the request is sent is not the current agent of the team.

* ``InvalidOperationException``: if the promoted user account is
  already the agent of the team, or if the specified account to be
  promoted as the new agent is not an administrator of the team.

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
