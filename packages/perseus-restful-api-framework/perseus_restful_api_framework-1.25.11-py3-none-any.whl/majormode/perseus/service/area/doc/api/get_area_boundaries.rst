=================================
``GET area/(area_id)/boundaries``
=================================

--------
Synopsis
--------

Return the boundaries of the specified geographic area.

If the requested geographic area is unknown, the platform doesn't return any data.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

* ``area_id``: identification of a geographic area.


------------------------
Request Query Parameters
------------------------

* ``sync_time`` (optional): indicate the time of the latest version of the coordinates of the boundaries of this geographic area cached by the client application.  If this time corresponds to the most recent coordinates of this geographic area's boundaries, the request doesn't return any data, otherwise it returns the last version of these coordinates.  If this parameter is not provided, the function always returns the most recent version of the coordinates of this geographic area's boundaries.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON structure if the boundaries of this geographic area is a simple polygon::

   [ longitude:decimal, latitude:decimal], ... ]

or the following JSON structure if the boundaries of this geographical area is a multi-ploygon:

   [ [ longitude:decimal, latitude:decimal], ... ], ... ]

where:

* ``latitude``: latitude-angular distance, expressed in decimal degrees (WGS84 datum), measured from the center of the Earth, of a point north or south of the Equator corresponding to the next point of the boundaries.

* ``longitude``: longitude-angular distance, expressed in decimal degrees (WGS84 datum), measured from the center of the Earth, of a point east or west of the Prime Meridian corresponding to the next point of the boundaries.


----------
Exceptions
----------

None.
