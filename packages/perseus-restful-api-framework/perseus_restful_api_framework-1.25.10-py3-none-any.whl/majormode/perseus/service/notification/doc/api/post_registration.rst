``POST /notification/registration``
===================================

Synopsis
--------

Register a device for receiving push notification messages from the platform.


Request Header Fields
---------------------

.. include:: /_include/optional_authenticated_session_header_fields.inc


Request URL Bits
----------------

None.


Request Query Parameters
------------------------

None.


Request Message Body
--------------------

The request must contains a JSON form of the following structure::

    {
      "device_id": string,
      "device_platform": string,
      "device_token": string,
      "locale": string,
      "topics": [ string, ... ],
      "utc_offset": integer
    }

where:

* ``device_id`` (required): identification of the device, which depends on the device platform:

  * Android: International Mobile Equipment Identity (IMEI) number of the device.

  * iOS: unique identifier of the iOS device, previously the Unique Device Identifier (UDID) of the device, which is a 40-character string that is tied to this specific Apple device. It could be a SecureUDID, which is an open-source sandboxed UDID solution aimed at solving the main privacy issues that caused Apple to deprecate UDIDs.

* ``device_platform`` (required): indicate the platform of the end user's mobile device:

  * ``ios``: Apple iOS

  * ``android``: Google Android

  * ``windows``: Windows Phone

  .. warning:: The server platform doesn't currently support the `Microsoft Push Notification Service (MPN) <http://msdn.microsoft.com/en-us/library/ff402537(v=vs.92).aspx>`_.

* ``device_token`` (required): token that identifies the device by the push notification provider of the device platform.

  * Android: token identifying the device to push the notification to, i.e., the registration ID.  A device token is an opaque identifier of a device that Android Google Cloud Messaging (GCM) gives to the device when it first connects with it.  The device shares the device token with its provider. The device token is analogous to a phone number; it contains information that enables GCM to locate the device on which the client application is installed.  GCM also uses it to authenticate the routing of a notification.

  * iOS: token identifying the iOS device to push the notification to.  A device token is an opaque identifier of a device that APNs gives to the device when it first connects with it.  The device shares the device token with its provider. Thereafter, this token accompanies each notification from the provider.  The device token is analogous to a phone number; it contains information that enables APNs to locate the device on which the client application is installed. APNs also uses it to authenticate the routing of a notification.  A device token is not the same thing as the device UDID returned by the ``uniqueIdentifier`` property of ``UIDevice``.

* ``locale`` (optional): represent the language that the end user prefers receiving new content in.  A locale corresponds to a tag respecting RFC 4646, expressed by a ISO 639-3 alpha-3 code element, optionally followed by a dash character ``-`` and a ISO 3166-1 alpha-2 code.  For example: "eng" (which denotes a standard English), "eng-US" (which denotes an American English).

  If this argument is not specified, the locale corresponds to the preferred language that the user has defined in his profile.

* ``topics`` (optional): a list of keywords representing topics the end user is interested in to be pushed new content whenever related to one of those topics.  The list of supported keywords is specific to the publisher service of the client application and as such the developer of the client application has to refer to the technical documentation of the publisher service.

* ``utc_offset`` (optional): difference between the location of the device and UTC (Universal Time Coordinated).  UTC is also known as GMT or Greenwich Mean Time or Zulu Time.



Response Message Body
---------------------

None.


Examples
--------

The following command registers the Apple device token ``fe66489f304dc75b8d6e8200dff8a456e8daeacec428b427e9518741c92c6660`` against the platform for the application identified with the API key ``b89c1156-1fe6-11e1-b608-109adda98fe0`` for content related to ``entertainment``, ``international``, and ``sports``, with a preference for the French language of France::

    curl -XPOST "http://api.example.com/notification/registration" \
         -H "X-API-Key: b89c1156-1fe6-11e1-b608-109adda98fe0" \
         -H "X-API-Sig: 3a5ece8164238d20f96dbbf5cbabd813" \
         -H "X-Authentication: bf13d1ba-2bba-11e1-a314-109adda98fe0" \
         -H "Content-Type: application/json" \
         -d '{
               "device_id": "2b6f0cc904d137be2e1730235f5664094b831186",
               "device_platform": "ios",
               "device_token": "fe66489f304dc75b8d6e8200dff8a456e8daeacec428b427e9518741c92c6660",
               "locale": "fra-FR",
               "topics": [ "entertainment", "international", "sports" ]
             }'


Exceptions
----------

The platform MAY raise the following exceptions to indicate that one or several required conditions have not been respected:

