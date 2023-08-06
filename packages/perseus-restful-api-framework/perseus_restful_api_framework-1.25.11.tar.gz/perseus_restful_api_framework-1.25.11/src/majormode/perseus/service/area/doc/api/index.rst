===============
Geographic Area
===============

.. toctree::
   :hidden:

   get_area


------------
Introduction
------------

A geographic area corresponds to a demarcated area of the Earth such as a continent or political boundaries, which are the dividing lines between countries, states, provinces, counties, cities, districts, wards, etc.  These lines, more often called borders, are created by people to separate areas governed by different groups.  Sometimes, political boundaries follow physical boundaries, but most of the time we can’t see them.

Example of geographic areas::

                 Asia                           : continent
                   |
                   |
          South Eastern Asia                    : sub-region
         /         |        \
        /          |         \
    Cambodia    Vietnam   Thailand              : country
               /   |   \
              /    |    \
           Hanoi  Hue  Ho Chi Minh City         : city
                         /          \
                        /            \
                     quan 1   huyen Binh Chanh  : district

A geographic area is identified by a unique immutable identification
number that is maintained by the platform.

A geographic area has one or several labels.  A label is a human-readable name of the geographic area for a given locale.  A locale is a set of parameters that defines a language, country and any special variant references.

A geographic area is defined by a boundary that delimits the topological space of the geographic area.

---------
Resources
---------

* :doc:`get_area`: return up to 100 geographic areas worth of extended information, specified by their identification.

* :doc:`get_area_boundaries`: return the boundaries of the specified geographic area.

