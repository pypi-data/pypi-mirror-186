Notification
============

.. toctree::
   :hidden:

   delete_notification
   get_notification
   post_registration


Introduction
------------

A notification is a lightweight message that needs to be delivered to one or more recipients.  It informs the recipients about an event that occurs, which might require fetching additional data from the server platform or requesting the recipient to perform some action.  A recipient is generally a client application that acts on behalf of a user, but it could also be an agent or botnet that controls a device.

A message can be delivered to a recipient using different styles of network communication:

* ``email``: the message is delivered in an Internet electronic mail message to the specified recipients based on a store-and-forward model.

* ``push``: the message is delivered to the specified recipients when the request for the transmission of information is initiated by the publisher or server platform and pushed out to the receiver or client application.

* ``pull``: the message is delivered to the specified recipients when the request for the transmission of information is initiated by the receiver or client application, and then is responded by the publisher or server platform.  Push style requires recipients to register with the server platform before it can receive messages using this mode.


Resources
---------

* :doc:`get_notification`: return a list of notifications that have been sent to the user.

* :doc:`delete_notification`: flush all the notifications originated from the client application that were sent to the user.

* :doc:`post_registration`: register a device to receive push notification messages from the server platform.
