# Unicode Normalizer Project

The Unicode Normalizer Project is a unicode converter written in Python. 
It supports unicode latin characters which will be transformed into ASCII characters.

## The Unicode Normalizer Project Compile-time Dependencies

* [Python](http://www.python.org) (3.11+ required;)
* [CX_Freeze](https://cx-freeze.readthedocs.io/en/stable) (optional)

## Installation

The [Unicode Normalizer Project installation guides] includes instructions for installing the project as part of a local application.

### Standalone Installation

* Create the following tables according to the [Unicode Normalizer Project files schema]:
 - `unicode`
 - `ascii`

## Running Graded Unit

### Run-time options:

* `python <path/to/main.py> unicode.txt ascii.txt` - Path to entry point file. If unspecified, the current working directory is used.