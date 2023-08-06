# WMSS: A Web Map Service Sampler

# Description

The `wmss` module allows extracting multiple image samples from Web Map Services (WMS), one of the mapping services described in the Open Geospatial Consortium (OGC) standard collection ([OGC, 2006](https://www.ogc.org/standards/wms)).

# Installation

Install the package using `pip`

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Python 
>>> pip install wmss
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Dependencies

- GUI programming in Python [easygui](https://pypi.org/project/easygui/)
- Programming with Open Geospatial Consortium (OGC) web service [OWSLib](https://pypi.org/project/OWSLib/)
- Python interface to PROJ (cartographic projections and coordinate transformations library) [Pyproj](https://pypi.org/project/pyproj/)
- Pure Python read/write support for ESRI Shapefile format [pyshp](https://pypi.org/project/pyshp/)