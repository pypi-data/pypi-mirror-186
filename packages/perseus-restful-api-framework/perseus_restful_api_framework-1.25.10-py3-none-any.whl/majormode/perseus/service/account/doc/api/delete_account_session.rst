===========================
``DELETE /account/session``
===========================

--------
Synopsis
--------


------------
Resource URL
------------

http://%(API_DOMAIN_NAME)s/session


---------------------
Request Header Fields
---------------------

* ``X-API-Key`` (required): an Application Programming Interface
  (API) key, sometimes referred to as application ID, which uniquely
  identifies the client application, such as a Web, a desktop, or a
  mobile application, that accesses the service.

* ``X-API-Sig`` (required): signature of the URL corresponding to
  the encryption of the URL with the API secret shared between the
  client application and the platform. This unique signature allows
  the platform to verify that a client application that uses the
  given API key is authorized to do so. If the URL differs in any way
  from that used to generate the signature, the platform will reject
  the request as invalid.

* ``X-Authentication`` (required): access token that identifies the
  authenticated session of a user against the platform. The access
  token is used by the client application to access the platform on
  behalf of the user. An access token MAY limit access to certain
  protected resources, and MAY have a limited lifetime.


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

The platform returns the following simple JSON data to acknowledge the operation::

    { }


----------
Exceptions
----------

The platform MAY raise the following exceptions to indicate that one or several required conditions have not been respected:

* ``IllegalAccessException``: if the specified login session doesn't belong to the specified user.

* ``UndefinedObjectException``: if the specified identification doesn't refer to any user login session registered to the platform.
