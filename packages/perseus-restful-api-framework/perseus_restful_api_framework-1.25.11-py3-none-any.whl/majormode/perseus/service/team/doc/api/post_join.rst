====================================
``POST /team/(team_id:string)/join``
====================================

--------
Synopsis
--------

Submit a request on behalf of a user to join a team.  This join
request has to be approved by one of the administrators of this team.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

* ``team_id``: identification of the team the user requests to join.


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

* ``UndefinedObjectException``: if the specified identification
  doesn't refer to a team registered against the platform.
