=======================
``PUT /account/avatar``
=======================

--------
Synopsis
--------

Upload a new graphical representation of the authenticated user, also
known as his avatar.

For safety and security reasons, all meta data are removed from the image file prior to the availability of this photo on the server platform.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc

* ``Content-Type``: the content type ``multipart/form-data`` MUST be used.  The MIME multipart data stream MUST conform to `RFC 2388 <http://www.ietf.org/rfc/rfc2388.txt>`_.

  One or more files can be uploaded as part of MIME data stream. The field name of the ``Content-Disposition`` header that qualifies each entry has no importance, nor does the original name of the file has.

  For instance, using the command line cURL::

    curl -XPUT "http://%(API_DOMAIN_NAME)s/account/avatar" \
         -F foo=@"~/IMG1224.jpg" \
         -F bar=@"~/IMG1298.jpg" \
         -H 'X-Authentication: f31aa1c2-f1bd-11e1-abf1-109adda98fe0' \
         -H 'X-API-Key: bbd734b8791111e487e6c80aa9c8e9fb' \
         -H 'X-API-Sig: 3706c4d77fcd8e99b5f1e5d22d7d7623786ce419'


----------------
Request URL Bits
----------------

None.


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

The platform returns the following JSON structure::

    {
      "account_id": string,
      "file_name": string,
      "picture_id": string,
      "picture_url": string,
      "update_time: timestamp
    }

where:

* ``account_id`` (required): identification of the user's account.

* ``file_name`` (required): the original local file name as the ``filename`` parameter of the ``Content-Disposition`` header.

* ``picture_id`` (required): identification of the new avatar of the user's account.

* ``picture_url`` (required): Uniform Resource Locator (URL) that specifies the location of the new avatar of the user's account.  The client application can use this URL and append the query parameter ``size`` to specify a given pixel resolution of the photo, such as ``thumbnail``, ``small``, ``medium``, or ``large``.

* ``update_time`` (required): time of the most recent modification of the properties of this photo.  This information should be stored by the client application to manage its cache of user accounts.


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one or several required conditions have not been respected:

* ``DeletedObjectException``: if the user's account has been deleted.

* ``DisabledObjectException``: if the user's account has been
  disabled.

* ``InvalidOperationException``: if the format of the uploaded image is not supported.

* ``UndefinedObjectException``: if the specified identification doesn't refer to a user account registered to the platform.
