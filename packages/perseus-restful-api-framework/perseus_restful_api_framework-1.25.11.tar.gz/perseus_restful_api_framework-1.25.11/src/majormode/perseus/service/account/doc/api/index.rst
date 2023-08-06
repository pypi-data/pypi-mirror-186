=======
Account
=======

.. toctree::
   :hidden:

   delete_session
   get_account_contact_availability
   get_accounts
   post_account
   post_account_password_reset
   post_account_password_reset_request
   post_session
   put_account_avatar
   put_account_fullname
   put_account_password


------------
Introduction
------------

A user account, or account for short, is a virtual representation of a
user who can be either a physical person, which is the common case,
or a virtual individual such as a botnet, similar to a non-player
character (NPC) in electronic games.

A user account allows a user to authenticate to system services and be
granted authorization to access them.  However, authentication does
not imply authorization.  To log in to an account, a user is
typically required to authenticate oneself with a password or other
credentials for the purposes of accounting, security, logging, and
resource management.


-----------------
Basic Information
-----------------

A user account is defined by a minimal set of information::

    {
      "id": string,
      "fullname": string,
      "email_address": string,
      "password": string,
      "locale": string,
      "picture": string,
      "gender": string
    }

where:

* ``id`` (required): the unique identification of this account.

* ``fullname`` (required): the complete full name of the user.

* ``email_address`` (required): the electronic mail address that the
  user gave when he registered this account.  It MUST correspond to
  valid RFC822 email address.  This email address is unique among the
  platform.  The case is insensitive.

* ``password`` (optional): the password that allows the user to log
  in  to this account and access to the platform resources.  The
  minimal size required of a password is 4 characters.

* ``picture`` (optional): the graphical representation of the user
  for this account, also known as the avatar of the user.  An avatar
  is defined by a unique identification.


------------
User Picture
------------

A user picture, or avatar, is either manually uploaded by the user
from his computer or his mobile device to the platform, either
downloaded by the platform from a Uniform Resource Locator (URL)
that, for instance, refers to the picture of this user on a given
Social Networking Service (SNS), such as Facebook, Twitter, Google,
Yahoo!, etc.

The platform supports the following image file formats for the
original input picture of the user:

* `Joint Photographic Experts Group <http://www.jpeg.org/jpeg/index.html>`_
  (JPEG)
* `Portable Network Graphics <http://www.w3.org/TR/PNG/>`_ (PNG)
* `Tagged Image File Format <http://partners.adobe.com/public/developer/tiff/index.html>`_
  (TIFF)

The platform generates multiple pixel resolutions and scaled-down JPEG
raster images from the original input picture of the user.  A given
generated pixel resolution is denoted by the following tuple::

   (width, height, logical image size)

where:

* ``width``: positive integer corresponding to the number of pixel
  columns of the image

* ``height``: positive integer corresponding to the number of pixel
  rows

* ``logical image  size``: string representation of the image size:

  * ``thumbnail``: 32px by 32px
  * ``small``: 64px by 64px
  * ``medium``: 128px by 128px
  * ``large``: 256px by 256px

The multiple pixel resolutions image files of the user avatar are
stored into either the local Network File System (NFS) -- referring
to the distributed file system, not the protocol -- of the platform,
or an external Content Delivery Network (CDN), such as Amazon Simple
Storage Service (S3). A client application can fetch the user picture
from the following URL:

  http://cdn.%(API_DOMAIN_NAME)s/account/(account_id)/picture?size=(size)

where:

* ``user_id`` (required) : identification of the user account.
* ``size`` (optional): string representation of the logical image
  size. If this HTTP query parameter is not defined, the size of the
  image file that is returned by default is of ``medium``.


--------------------------
Social Networking Services
--------------------------

Social networking services (SNS), such as Facebook, Twitter, Google,
Yahoo!, are widely used worldwide. It's quite common that a user
already has an account on one or several of these platforms.

The user has the choice either to create a new account against the
platform, following a classic sign-up flow, either to sign-in with
the account he has registered against an SNS, which implicitly signs
the user up against the platform. The platform currently supports the
following SNS list:

* Facebook
* Foursquare
* Google
* Gowalla
* Linked-in
* Yahoo!

This last flow, that corresponds to sign-in with an SNS account, is
referred as *account linking*.

Represent OAuth credentials of user, provided by a client application
(the Consumer), to grant the platform access to the user's
information stored with a Social Networking Service (SNS).

Basically, the Consumer delegates its privileges to the platform.


Represent user accounts registered against 3rd party Social
 * Networking Services (SNS).

-------------
User Settings
-------------

Represent a collection of personal data and settings, also known as
properties, associated to a specific user account.

Section ``privacy.default``
---------------------------

============ ========== ========== ===========
Property     Type       Default    Description
============ ========== ========== ===========
``checkins`` ``string`` ``public`` Privacy level values for checkins. If there are not checkin settings for a certain spot yet, this value will be used as a default value for checkins. Will be overruled by specific checkin settings for a spot on the first checkin.

``photos``   ``string`` ``public`` Privacy level values for photos. Default privacy level for uploading photos.
============ ========== ========== ===========


Section ``notification``
------------------------

============================= =========== ========== ===========
Property                      Type        Default    Description
============================= =========== ========== ===========
``on_contact_added``          ``boolean`` ``true``
``on_contact_avatar_updated`` ``boolean`` ``true``
============================= =========== ========== ===========

Section ``general``
-------------------

==================== =========== ========= ===========
Property             Type        Default   Description
==================== =========== ========= ===========
``vibrate``          ``boolean`` ``false`` Global switch to turn vibration on and off.

``automatic_update`` ``boolean`` ``true``  Property only accessible in releases of the mobile application built for environment stages but production. For the latter, the automatic update of the application is handled by the market place of the phone platform (Android Marketplace or Apple Store).
==================== =========== ========= ===========


Section ``checkin``
-------------------

============= =========== ========= ===========
Property      Type        Default   Description
============= =========== ========= ===========
``prompt``    ``boolean`` ``false`` Switch to turn prompted checkins on and off (only applies to Android). If off, the user will not be prompted.

``automatic`` ``boolean`` ``false`` Switch to turn automatic checkins on and off (only applies to Android). If off, the user will not be checked in automatically and will not see any options related to auto checkins anywhere on the UI.
============= =========== ========= ===========


---------
Resources
---------

* :doc:`delete_session`: delete the login session, which, as a side
  effect, signs the user account out.

* :doc:`get_account_contact_availability`: indicate whether the
  specified contact is available.  In the case it would have been
  already registered by a user, indicate whether this contact has
  been verified.

* :doc:`get_account_username_availability`: indicate whether the
  specified username is available or not.

* :doc:`get_accounts`: return up to 100 users worth of extended
  information, specified by their identification.

* :doc:`post_account`: sign-up a user against the platform.

* :doc:`post_account_password_reset_request`: request the platform
  to initiate the process to help the user in resetting his password
  that he has forgotten.

* :doc:`post_account_password_reset`: change the password of the
  specified account of a user who forgot his password and who
  requested the platform to reset.

* :doc:`post_session`: create a login session that corresponds to
  the period of activity between a user sign-in and sign-out of the
  platform.

* :doc:`put_account_avatar`: upload a graphical representation of the
  authenticated user, also known as his avatar.

* :doc:`put_account_fullname`: Update the complete fullname of the
  authenticated user.

* :doc:`put_account_password`: change the password of the specified
  user's account with a new password that this user is providing.
