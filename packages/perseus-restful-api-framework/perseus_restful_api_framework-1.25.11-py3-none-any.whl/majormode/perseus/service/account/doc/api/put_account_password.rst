=========================
``PUT /account/password``
=========================

--------
Synopsis
--------

Change the password of the specified user's account with a new
password that this user is providing.

The new password must respect the rules of definition of a password.
It cannot be identical to the old password.  It cannot contains part
of the email address of the user.


------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/account/password

---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

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
      "old_password": string,
      "new_password": string
    }

where:

* ``old_password`` (required): the old password of the user.

* ``new_password`` (required): the new password of the user.

---------------------
Response Message Body
---------------------

None.

----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``IllegalAccessException``: if the old password that is passed along
  with the request is wrong.

* ``InvalidArgumentException``: if the new password doesn't conform to
  the rules of password definition, if the new password contain part
  of the email address of the user, if the new password is identical
  to the old password of the user.
