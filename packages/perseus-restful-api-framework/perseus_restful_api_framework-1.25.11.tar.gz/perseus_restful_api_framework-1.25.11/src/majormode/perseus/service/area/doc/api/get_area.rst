============
``GET area``
============

--------
Synopsis
--------

Return a list of geographic areas worth of extended information, either specified by their identification, either by a location that these areas encompass, either a bounding box that intersects these areas.


---------------------
Request Header Fields
---------------------

.. include:: /_include/authenticated_session_header_fields.inc


----------------
Request URL Bits
----------------

None.


------------------------
Request Query Parameters
------------------------

* ``ids`` (optional): a comma separated list of geographic area identifications, up to 100 are allowed in a single request.  If a requested geographic area is unknown, then that area will not be returned in the results list.

* ``latitude`` (optional): atitude-angular distance, expressed in decimal degrees (WGS84 datum), measured from the center of the Earth, of a point north or south of the Equator corresponding to the location that the returned geographic areas encompass.

* ``locale`` (optional): the locale in which the label of the geographic area has to be returned.  A locale corresponds to a tag respecting RFC 4646, which is a set of parameters that defines a language, country and any special variant references.  The labels of all the geographic areas are at least available in English, which is the default locale.  If not specified, the function returns the label of the geographic area in English.

* ``longitude`` (optional): longitude-angular distance, expressed in decimal degrees (WGS84 datum), measured from the center of the Earth, of a point east or west of the Prime Meridian corresponding to the location that the returned geographic area encompass.

* ``bounds`` (optional): the bounding box that the returned geographic areas intersect.  The value is a string of the form ``lat_lo,lng_lo,lat_hi,lng_hi`` where ``lo`` corresponds to the southwest corner of the bounding box ``hi`` corresponds to the northeast corner of that box.


--------------------
Request Message Body
--------------------

None.


---------------------
Response Message Body
---------------------

The platform returns the following JSON structure::

   [
      {
        "area_id": string,
        "area_type": string,
        "area_label": string,
        "parent_area_id": string
      },
      ...
    ]

* ``area_id``: identification of the geographic area.

* ``area_type``: symbolic name of the type of the geographic area.

* ``area_label``: label in the specified locale, or the closest locale if no label is defined for this particular locale, which is, at least, English by default.

* ``parent_area_id``: identification of the parent geographic area or ``None`` if none defined.


----------
Exceptions
----------

None.
