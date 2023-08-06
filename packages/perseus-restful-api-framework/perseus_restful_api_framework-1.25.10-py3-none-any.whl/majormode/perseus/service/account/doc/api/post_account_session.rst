``POST /account/session``
=========================

Synopsis
--------


Request Header Fields
---------------------

.. include:: /_include/anonymous_session_header_fields.inc


Request Query Parameters
------------------------

None.


Request Message Body
--------------------

The platform supports two modes for sign-in a user account:

* an explicit method that consists in providing an email address and
  a password as the credentials of this user for logging into the
  platform;

* an implicit method that consists in providing a set of token
  credentials and use it to access the user's information stored on a
  social networking service against (SNS) the user has registered an
  account against.  This latter process corresponds to the Open
  Authorization (OAuth) flow.

Explicit Method: Email Address and Password
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user can create an account providing an email address and a password
as credentials for logging into the platform.  The client application
that sign the user account in MUST provide the following JSON data::

    {
      "email_address": string,
      "password": string,
      "auto_sign_in": boolean
    }

where:

* ``email_address`` (required): the email address of the user. Email address is not case sensitive.

* ``password`` (required): the password of the user account. Password is case sensitive.

* ``auto_sign_in`` (optional): indicate whether the platform is
  requested to sign-in this user once the sign-up procedure completes
  successfully.

Implicit Method: Open Authorization (OAuth)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`OAuth (Open Authorization) <http://oauth.net/>`_ is an open standard for authorization.  It allows users to share their private resources (e.g., profile information, photos, videos, contact lists, etc.) stored on one site with another site without having to hand out their credentials, typically username and password.

OAuth allows users to hand out tokens instead of credentials to their data hosted by a given service provider.  Each token grants access to a specific site (e.g., a social networking site) for specific resources (e.g., just some information of the user profile, just photos from a specific album, etc.) and for a defined duration (e.g., the next 2 hours).  This allows a user to grant a third party site access to their information stored with another service provider, without sharing their access permissions or the full extent of their data.

A client application that prefers this method MUST provide the following JSON data::

    {
      "provider_name": string,
      "consumer_key": string,
      "consumer_secret": string,
      "access_token": string,
      "request_token": string,
      "token_secret": string,
      "protocol_version": string,
      "expiration_time": string,
      "auto_sign_in": boolean
    }

* ``provider_name`` (required): code name of the Service Provider, such as, for instance:

  * ``facebook``
  * ``foursquare``
  * ``gowalla``
  * ``twitter``
  * ``google``
  * ``yahoo``

* ``consumer_key`` (required): a value used by the Consumer to identify itself to the Service Provider.

* ``consumer_secret`` (required): a secret used by the Consumer to establish ownership of the Consumer Key.

* ``request_token`` (required): a value used by the Consumer to obtain authorization from the User, and exchanged for an Access Token.

* ``access_token`` (required): a value used by the Consumer to gain access to the Protected Resources on behalf of the User, instead of using the User’s Service Provider credentials.

* ``token_secret`` (required): a secret used by the Consumer to establish ownership of a given Token.

* ``protocol_version`` (required): the version of the OAuth protocol used, such as ``1.0``, ``1.0a``, or ``2.0``.

* ``expiration_time`` (optional): time when the OAuth token expires.

* ``auto_sign_in`` (optional): indicate whether the platform is requested to sign-in this user once the sign-up procedure completes successfully.


Response Message Body
---------------------

The platform returns the following JSON data::

    {
      "account_id": string,
      "app_id": string,
      "expiration_time": string,
      "full_name": string,
      "session_id": string,
      "username": string
    }

where:

* ``account_id`` (required): identification of the account of the user.

* ``app_id`` (required): identification of the client application with which the user is authenticated.

* ``expiration_time`` (required): time when the login session will expire.

* ``full_name`` (optional): complete full name of the user as given by the user himself, i.e., untrusted information, or as determined from from his email address of as for ghost account.

* ``is_verified`` (optional): indicate whether the contact information has been verified, whether it has been grabbed from a trusted Social Networking Service (SNS), or whether through a challenge/response process.  The user should be reminded to confirm his contact information if not already verified, or the user would take the chance to have his account suspended.

* ``is_primary`` (optional): indicate whether this contact information is the primary one for the given contact type (e.g., email address, phone number).

* ``session_id`` (required): identification of the login session of the user.

* ``username`` (optional): also known as screen name or nickname, username is chosen by the end user to identify himself when accessing the platform and communicating with others online.  A username should be totally made-up pseudonym, not reveal the real name of the person. The username is unique across the platform.  A username is not case sensitive.


Exceptions
----------

The platform MAY raise the following exceptions to indicate that one or several required conditions have not been respected:

* ``AccountDeletedException``: if the user account has been deleted.

* ``AccountDisabledException``: if the user account has been disabled.

* ``AuthenticationFailureException``: if the given user name and/or password don't match any user account registered against the platform.
