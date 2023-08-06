=============================
``GET /notification/message``
=============================

--------
Synopsis
--------

Return a list of notifications that have been sent to the specified
user's account.


---------------------
Request Header Fields
---------------------

.. include:: /_include/optional_authenticated_session_header_fields


----------------
Request URL Bits
----------------

None.


------------------------
Request Query Parameters
------------------------

* ``end_time`` (optional): indicate the latest time to return a
  notification.

* ``include_read`` (optional): indicate whether to include
  notifications that have already been read.  By default,
  notifications a user has read are not included.

* ``limit`` (optional): constrain the number of records that are
  returned to the specified number.  Default value is ``20``. Maximum
  value is ``100``.

* ``mark_read`` (optional): indicate whether to mark read every
  notification that this functions returns.  By default, the function
  marks as read notifications that are returned.

* ``offset`` (optional): require to skip that many records before
  beginning to return records to the client.  Default value is ``0``.
  If both ``offset`` and ``limit`` are specified, then ``offset``
  records are skipped before starting to count the limit records that
  are returned.

* ``recipient_id`` (optional): identification of a recipient, other
  than an authenticated account.  This recipient can be a device
  identified with an International Mobile Equipment Identity (IMEI),
  or any alphanumeric string.

* ``sort_order`` (optional): ``ascending`` sorts notifications by
  ascending time of creation, while ``descending`` sorts
  notifications by descending time of creation.

* ``start_time`` (optional): indicate the earliest time to return a
  notification. If not specified, the function returns all available
  prior notifications.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON form::

    [
      {
        "creation_time": timestamp,
        "is_read": boolean,
        "notification_id": string,
        "notification_type": string,
        "payload": json,
        "schedule_time": timestamp,
        "sender_id": string,
        "update_time": timestamp
      },
      ...
    ]

where:

* ``creation_time`` (required): time when the sender originated the
  notification to the intended recipient.

* ``is_read`` (required): indicate whether the notification has been
  read by the intended recipient.

* ``notification_id`` (required): identification of the notification.

* ``notification_type`` (required): string representation of the
  type of the notification, such as, for instance,
  ``on_friendship_accepted``, as defined by the client application or
  the service that posted this notification to the user.

* ``payload`` (optional): additional information specific to this
  particular notification.

* ``schedule_time`` (required): time when this notification is
  scheduled to be sent to the intended recipient.  The notification
  is not visible to the intended recipient prior to this time.

* ``sender_id`` (optional): the identification of the account of the
  user who initiates the notification.

* ``update_time`` (required): time of the most recent modification
  of an attribute of the notification, such as its read status.


----------
Exceptions
----------

None.
