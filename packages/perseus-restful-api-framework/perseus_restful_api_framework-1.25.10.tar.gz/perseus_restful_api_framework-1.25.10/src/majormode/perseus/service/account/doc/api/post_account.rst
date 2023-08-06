=================
``POST /account``
=================

--------
Synopsis
--------



---------------------
Request Header Fields
---------------------

.. include:: /_include/anonymous_session_header_fields.inc


----------------
Request URL Bits
----------------

None.


------------------------
Request Query Parameters
------------------------

* ``auto_sign_in`` (optional): indicate whether the platform is
  requested to sign-in this user once the sign-up procedure completes
  successfully.  If not specified, the platform doesn't automatically
  sign-in the user.

* ``is_enabled`` (optional): indicate whether this user account is
  immediately enabled, or whether it needs to be flagged as pending
  until the user takes some action, such as, for instance, confirming
  his contact information.  By default, the user account is
  automatically enabled.


--------------------
Request Message Body
--------------------

The platform supports two modes for creating a user account:

* an explicit method that consists in providing an email address and
  a password as the credentials of this user for logging into the
  platform;

* an implicit method that consists in providing a set of token
  credentials and use it to access the user's information stored on a
  social networking service against (SNS) the user has registered an
  account against.  This latter process corresponds to the Open
  Authorization (OAuth) flow.


Explicit Method: Email Address and Password
-------------------------------------------

A user can create an account providing an email address and a password
as credentials for logging into the platform.  The client application
that registers the user account MUST provide the following JSON data::

    {
      "contacts": [
        [ name:string, value:string, is_primary:boolean ],
        ...
      ],
      "full_name": string,
      "locale": string,
      "password": string,
      "recaptcha": {
        "private_key": string,
        "challenge": string,
        "response": string
      },
      "username": string,
    }

where:

* ``account_type`` (optional): type of the user account. One of the
  following types:

  * ``standard``: standard user account.  This is the default
    account type.

  * ``test``: user account used for test purpose only.  Such user
    account and associated data might be deleted every 24 hours.

* ``contacts`` (optional): list of properties such as e-mail
  addresses, phone numbers, etc., in respect of the electronic
  business card specification (vCard).  The contact information is
  represented by a list of tuples of the following form::

     [ [ name:string, value:string, is_primary:boolean ], ... ]

  where:

  * ``name`` (optional/required): type of this contact
    information, which can be one of these standard names in respect
    of the electronic business card specification (vCard):

    * ``EMAIL``: e-mail address of the user.  It MUST correspond
      to a valid RFC822 email address.  The email address MUST be
      unique among all the email addresses already registered by
      other users to the platform, as the email address is used by
      the user to authenticate against the platform.  The email
      address is not case-sensitive. The format of email addresses is
      formally defined in
      `RFC 5322 <http://tools.ietf.org/html/rfc5322>`_ (sections
      3.2.3 and 3.4.1) and by
      `RFC 5321 <http://tools.ietf.org/html/rfc5321>`_.  An email
      address is a string of a subset of ASCII characters separated
      into 2 parts by an "``@``" (at sign), a "local-part" and a
      domain, that is, ``local-part@domain``.  The local-part of an
      email address may be up to 64 characters long and the domain
      name may have a maximum of 253 characters.  However, the
      maximum length of a forward or reverse path length of 256
      characters restricts the entire email address to be no more
      than 254 characters.  The local-part of the email address may
      use any of these ASCII characters.

    * ``PHONE``: phone number in E.164 numbering plan, an ITU-T
      recommendation which defines the international public
      telecommunication numbering plan used in the Public Switched
      Telephone Network (PSTN).

  * ``value`` (required): value of this contact information
    representing by a string, such as ``+84.01272170781``, the
    formatted value for a telephone number property.

  * ``is_primary`` (optional): indicate whether this contact
    information is the primary.  By default, the first contact
    information of a given type is the primary.

  .. note::

   This argument is optional if and only if the argument
   ``username`` is provided, otherwise either at least an email
   address or a phone number must be required.

* ``full_name`` (optional): the proper name that identifies the user.
  A name is made up of several parts, which order can be significant
  and largely depends on culture. The order *family-name given-name*
  is commonly known as the Eastern order and is used in Hungary,
  parts of Africa, and East Asia (for example in mainland China,
  Japan, Korea, Malaysian Chinese, Singapore, Taiwan, and Vietnam).
  The order *given-name family-name* is commonly known as the Western
  order and is usually used in most European countries and in
  countries that have cultures predominantly influenced by Western
  Europe (North and South America and Australia and New Zealand).

* ``password`` (required): the password of the user account. A
  password is case sensitive.  The minimal length of a password is 6
  characters, while the maximum length is 18 characters. A password
  may use any letters from ``a`` to ``z``, and ``A`` to ``Z``, any
  digits from ``0`` to ``9``, any punctuation and other characters.

* ``recaptcha`` (optional): the user account creation is protected
  by a CAPTCHA challenge to avoid spammer to automatically create
  user account.  The basis of the Completely Automated Public Turing
  Test To Tell Computers and Humans Apart (CAPTCHA) system is to
  prevent automated access to a system by computer programs or
  "bots". `reCAPTCHA <http://www.google.com/recaptcha>`_ is a free
  CAPTCHA service that protects against spam, malicious registrations
  and other forms of attacks where computers try to disguise
  themselves as a human.

  The client application that registers an account on behalf of a
  user MUST
  `integrate reCAPTACH <http://code.google.com/apis/recaptcha/intro.html>`_
  and
  `display the reCAPTCHA image <http://code.google.com/apis/recaptcha/docs/display.html>`_
  that the user has to identify.

  * ``private_key`` (required): the private key that was used when
    requesting the reCAPTCHA challenge/response.

  * ``challenge`` (required): the token that identifies the
    challenge that reCAPTCHA gave to the user.

  * ``response`` (required): the response that the user provided.

  .. note::

     CAPTCHA challenge is only mandatory for the staging and
     production environment stages; it is not required for the other
     environments stages such as, for instance, development and
     integration stages.

* ``username`` (optional/required): a name used to gain access to a
  the platform.  The username MUST be unique among all the usernames
  already registered by other users to the platform.  This argument
  is optional if and only if contact information has been passed.


Implicit Method: Open Authorization (OAuth)
-------------------------------------------

`OAuth (Open Authorization) <http://oauth.net/>`_ is an open standard
for authorization.  It allows users to share their private resources
(e.g., profile information, photos, videos, contact lists, etc.)
stored on one site with another site without having to hand out their
credentials, typically username and password.

OAuth allows users to hand out tokens instead of credentials to their
data hosted by a given service provider.  Each token grants access to
a specific site (e.g., a social networking site) for specific
resources (e.g., just some information of the user profile, just
photos from a specific album, etc.) and for a defined duration (e.g.,
the next 2 hours).  This allows a user to grant a third party site
access to their information stored with another service provider,
without sharing their access permissions or the full extent of their
data.

Instead of requesting the user to explicitly create an account against
the platform, providing an email address and a password, the client
application can process the user account creation by following the
standard
`OAuth 2.0 Authorization Framework <http://tools.ietf.org/html/rfc6749>`_::

    +--------+                               +---------------+
    |        |--(A)- Authorization Request ->|   Resource    |
    |        |                               |     Owner     |
    |        |<-(B)-- Authorization Grant ---|               |
    |        |                               +---------------+
    |        |
    |        |                               +---------------+
    |        |--(C)-- Authorization Grant -->| Authorization |
    | Client |                               |     Server    |
    |        |<-(D)----- Access Token -------|               |
    |        |                               +---------------+
    |        |
    |        |                               +---------------+
    |        |--(E)----- Access Token ------>|    Resource   |
    |        |                               |     Server    |
    |        |<-(F)--- Protected Resource ---|               |
    +--------+                               +---------------+

A client application that prefers this method MUST provide the
following JSON data::

    {
      "access_token": string,
      "oauth_consumer_key": string,
      "oauth_consumer_secret": string,
      "locale": string,
      "provider_name": string,
      "expiration_time": string,
      "user_id": string
    }

where:

* ``access_token`` (required): a value used by the Consumer to gain
  access to the Protected Resources on behalf of the User, instead of
  using the User’s Service Provider credentials.

* ``expiration_time`` (optional): time when the OAuth token expires.

* ``oauth_consumer_key`` (required): a value used by the Consumer to
  identify itself to the Service Provider.

* ``oauth_consumer_secret`` (required): a secret used by the
  Consumer to establish ownership of the Consumer Key.

* ``locale`` (optional): a local that references the preferred
  language of the user.  A locale is expressed by a ISO 639-3 alpha-3
  code element, optionally followed by a dash character "-" and a ISO
  3166-1 alpha-2 code.  For example: "eng" (which denotes a standard
  English), "eng-US" (which denotes an American English).

* ``provider_name`` (required): code name of the Service Provider,
  such as, for instance:

  * ``facebook``
  * ``foursquare``
  * ``gowalla``
  * ``twitter``
  * ``google``
  * ``yahoo``

* ``user_id`` (required): identification of the 3rd party user
  account on the Service Provider.

.. note::

   A client application that integrates Facebook needs to request
   the end user for the following permissions as part of the
   ``scope`` value: ``user_about_me``, ``email``, ``user_photos``,
   ``user_checkins``, ``offline_access``, and ``publish_stream``.

   * ``email``: provides access to the user's primary email
     address in the email property. Do not spam users. Your use of
     email must comply both with
     `Facebook policies <http://www.facebook.com/terms.php>`_ and
     with the
     `CAN-SPAM Act <http://business.ftc.gov/documents/bus61-can-spam-act-compliance-guide-business>`_.

   * ``offline_access``: enables your app to perform authorized
     requests on behalf of the user at any time. By default, most
     access tokens expire after a short time period to ensure
     applications only make requests on behalf of the user when the
     are actively using the application. This permission makes the
     access token returned by our OAuth endpoint long-lived.

   * ``publish_stream``: enables your app to post content,
     comments, and likes to a user's stream and to the streams of the
     user's friends. With this permission, you can publish content to
     a user's feed at any time, without requiring offline_access.
     However, please note that Facebook recommends a user-initiated
     sharing model.

   * ``user_about_me``: provides access to the "About Me" section
     of the profile in the about property.

   * ``user_checkins``: provides read access to the authorized
     user's check-ins or a friend's check-ins that the user can see.

   * ``user_photos``: provides access to the photos the user has
     uploaded.

   For more information about Facebook access tokens and
   permissions, refer to:

   * `Permission <http://developers.facebook.com/docs/reference/api/permissions/>`_;
     Facebook Developers Documentation;

   * `Facebook Graph API — getting access tokens <http://benbiddington.wordpress.com/2010/04/23/facebook-graph-api-getting-access-tokens/>`_;
     Ben Biddington; 2010-04-23;

.. note::

   A client application that integrates Google needs to request the
   end user for the following permissions as part of the ``scope``
   value: ``http://www.google.com/m8/feeds/`` and
   ``http://www-opensocial.googleusercontent.com/api/people``. For
   more information about Google access tokens and permissions, refer
   to:

   * `Authentication and Authorization in the Google Data Protocol <http://code.google.com/apis/gdata/docs/auth/overview.html>`_;
     Google Data Protocol;


---------------------
Response Message Body
---------------------

The platform returns the following JSON structure without particular
order::

    {
      "account_id": string,
      "creation_time": timestamp,
      "expiration_time": timestamp,
      "session_id": string,
    }

where:

* ``account_id`` (required): identification of the account of the
  user.

* ``creation_time`` (required): time when this account has been
  registered.  This information should be stored by the client
  application to manage its cache of accounts.

* ``expiration_time`` (optional): time when the login session will
  expire.  This information is provided if the client application
  requires the platform to automatically sign-in the user (cf. query
  parameter ``auto_sigin``).

* ``session_id`` (optional): identification of the login session of
  the user.  This information is provided if the client application
  requires the platform to automatically sign-in the user (cf. query
  parameter ``auto_sigin``).


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one
or several required conditions have not been respected:

* ``ContactAlreadyUsedException``: if the specified contact is already
  registered with an existing user account.

* ``IllegalAccessException``: if the reCAPTCHA challenge/response
  failed.

* ``InvalidArgumentException``: if the specified email address or
  password doesn't respect the required format.
