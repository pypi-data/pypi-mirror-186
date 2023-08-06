================
``GET /account``
================

--------
Synopsis
--------

Return up to 100 users worth of extended information, specified by
their identification.

If a requested user is unknown, suspended, or deleted, then that user
will not be returned in the results list.


------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/account?ids=:id,:id,...

or

http://%(API_DOMAIN_NAME)s/account?emails=:email,:email,...


---------------------
Request Header Fields
---------------------

.. include:: /_include/optional_authenticated_session_header_fields.inc


------------------------
Request Query Parameters
------------------------

* ``ids`` (required, optional): a comma separated list of user
  account identifications, up to 100 are allowed in a single request.
  This parameter is required unless the parameter ``emails`` is
  provided.

* ``emails`` (required, optional): a comma separated list of email
  addresses, up to 100 are allowed in a single request.  This
  parameter is required unless the parameter ``ids`` is provided.

* ``start_time`` (optional): indicate the earliest time, expressed
  in accordance with RFC 3339, to return users account information
  that have been modified since.  If not specified, the function
  returns information about all the specified user accounts.

* ``extended_info`` (optional): request the function to provide
  extended information about these accounts, such as information of
  accounts they might have on some Social Networking Services, which
  require the caller to be connected to these users, or to be
  administrator of the platform.  If not specified, the function
  doesn't return extended information about the users.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns a list of information about the specified user
accounts::

   [
      {
        "account_id": string,
        "name": string,
        "email_address": string,
        "picture_id": string,
        "picture_url": string,
        "locale": string,
        "phone_number": string,
        "is_connected": boolean,
        "creation_time" string,
        "sns": [
          {
            "provider": string,
            "user_id": string,
            "user_name": string
          },
          ...
        ],
        "update_time": string
      },
      ...
    ]

* ``account_id`` (required): identification of the user account.

* ``name`` (required): full name of this user account.

* ``email_address`` (optional): e-mail address of this user account.
  This information might not have been verified.  This attribute is
  return only if the user on behalf of whom this function is called
  is authenticated and if he is the owner of this account or
  connected with this user.

* ``picture_id`` (optional): identification of the user account's
  picture, if any picture defined for this user account.

* ``picture_url`` (optional): Uniform Resource Locator (URL) that
  specifies the location of the picture this user account, if any
  defined.  The client application can use this URL and append the
  query parameter ``size`` to specify a given pixel resolution of the
  user account's picture:

  * ``thumbnail``: 32px by 32px
  * ``small``: 64px by 64px
  * ``medium``: 128px by 128px
  * ``large``: 256px by 256px

* ``locale`` (required): tag respecting RFC 4646, which identifies
  the preferred language of the user, or English by default.  A
  locale is expressed by a ISO 639-3 alpha-3 code element, optionally
  followed by a dash character ``-`` and a ISO 3166-1 alpha-2 code.
  For example: ``eng`` (which denotes a standard English), ``eng-US``
  (which denotes American English).

* ``phone_number`` (optional): phone number of this user.  This
  information might not have been verified.  This attribute is
  returned only if the user on behalf of whom this function is called
  is authenticated and if he is the owner of this account or
  connected with this user.

* ``is_connected`` (required): indicate whether the user account on
  behalf of whom the function is called is authenticated and if he is
  connected to this account.

* ``sns``(optional): a list of Social Networking Service (SNS)
  accounts this user has linked. This attribute is returned only if
  the user on behalf of whom this function is called is authenticated
  and if he is the owner of this account, connected with this user,
  or is an administrator of the platform.

  * ``provider``: code name of the Service Provider, such as, for
    instance the following not exhaustive list:

    * ``facebook``
    * ``foursquare``
    * ``gowalla``
    * ``twitter``
    * ``google``
    * ``yahoo``:

  * ``user_id``: identification of the user on the Social
    Networking Service.

  * ``user_name``: name of the user on this service.

* ``creation_time`` (optional): string representation, expressed in
  accordance with RFC 3339, of the time when this user account has
  been registered against the platform.  This attribute is returned
  only if the user on behalf of whom this function is called is the
  owner of this account or connected with this user.

* ``update_time`` (required): string representation, expressed in
  accordance with RFC 3339, of the time when the information of this
  user account has been updated for the last time.


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

