# Utils

General utilities complimenting and expanding on standard python.

## Setup & Install

https://pypi.org/project/utils-nuuuwan/#history

```
pip install utils-nuuuwan
```

## Version History

### 1.1.17 (CURRENT RELEASE)
* Added TimeIDs 
* Added TimeUnits 
* #Refactor Time into new folder 

### 1.1.16 

* Refactored log to have Log(name)
* Added Time addition 
* Renamed RandomColor to Color
* Cleaned-up Browser
* Deleted Image

### 1.1.15 

* Deprecated xy, geo, latlng
* Refactored dt into String

### 1.1.14 

* Deprecated jsonx
* feat: import cache directly, instead of cache.cache
* Deprecated db
* renamed www -> WWW
* Deprecated printx
* Deprecated sysx
* Deprecated timex
* Deprecated filex, tsv
* Deprecated ds

### 1.1.13 

* Deprecated zipx
* Deprecated legacy www

### 1.1.12 

* Make WWW primary, and add PendingDeprecationWarnings to stand-alone functions

* Deprecated colorx; replaced with RandomColor

* Added (smart) Dict
* Added (smart) List
* Added Iter
* Added Table and TableRow

### 1.1.11 

* Added Time, TimeDelta and TimeFormat (i.e. made time a class)

### 1.1.8 

* Removed pandas, geopandas and shapely

### 1.1.7

* Fixed bug in Git

### 1.1.6

* Added WWW
* Added readBinary to File
* Git - lazy clone. Clone only the branch to checkout

### 1.1.5

* Added Zip
* Updated Git checkout to pull on checkout

### 1.1.4

* Added Git

### 1.1.3

* Fixed Tweepy "me" bug

### 1.1.2

* Added write_lines to file
* Added get_address_details to GoogleMaps

### 1.1.1

* Added GoogleMaps with basic mapping functions. Requires API keys

### 1.1.0

Version 1.1 will start replacing and deprecating 1.0.

* Added CSVFile, File, JSONFile, TSVFile, XSVFile which togther should replace filex, jsonx, and tsv.

### 1.0.40
* Changed logging.DEBUG color to  textColor.BLUE (Gray was not working on some consoles)
* Added xy with get_bbox and get_func_transform, latlng_to_xy, xy_to_latlng

### 1.0.39

* Removed text from DEFAULT_ATTRIB_MAP
* Changed logging.DEBUG Color (easier on the eye)
* Added get_time_id

### 1.0.38

* Added timezone logic to timex.format_time and parse_time
* Removed StopWatch
* Fixed propogate #BUG in logx.get_logger
* Added xmlx.render_link_styles

### 1.0.37

* Added defaults to colorx
* Added colorx with various random color generators
* Added basic latlng container
* Added ds.get_count

### 1.0.36

* Added printx with printing utils
* Added snake_to_camel and camel_to_snake to dt
* Added zipx - with basic Zip utils.

### 1.0.35

* Added xmlx, which contains various utils for manipulating xml

### 1.0.34
(No Release)

### 1.0.33

* Added logx. get_logger creates a custom logger that prints log messages in color
