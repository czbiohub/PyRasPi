# PyRasPi

## Introduction
This repository contains Python utilities for interacting with a Raspberry Pi in CZ Biohub Bioengineering team applications. It primarily builds off of the native RPi.GPIO library pre-compiled on the Pi and adds extra functionality. All utilities support Python 3.7+.

## Contents
* __GpioOut__ - GPIO base class for setting or reading the state of an output pin.
* __RPiOut__ - A specific implementation of GpioOut that utilizes RPi.GPIO.
* __RPiTimedOut__ - Extends RPiOut with an expiration timer.
* __RPiDc__ - A specific implementation of pymotors.DcBase.
* __RPiDcArray__ - A specific implementation of pymotors.DcArray.

## Dependencies

RPiOut :: RPi.GPIO<br>
RPiDC :: pymotors.DcBase<br>
RPiDcArray :: RPi.GPIO<br>
RPiDCArray :: pymotors.DcArray<br>

## Installation and Use
### Installing Module
1. Create and/or activate a virtual environment in a convenient location with Python3
2. Download / clone this repository
3. Navigate to the base of the repository
4. Install setuptools (__pip install setuptools__)
5. Test the module for completeness (__python setup.py test__)
6. Install module (__pip install .__)

NOTE: Developers may want to install the module with __pip install -e .__ so that changes they make to the module are immediately reflected when subsequently imported.

### Installing without cloning the repository
1. Create and/or activate a virtual environment in a convenient location with Python3
2. Install module (__pip install git+https://github.com/czbiohub/PyRasPi__)

NOTE: It is unclear that module can be tested for completeness if directly installed.

### Updating Module from Repository
1. Pull changes from remote repository
2. Activate virtual environment with previous install
3. Navigate to the module directory
4. Test the module for completeness (__python setup.py test__)
5. Update module (__pip install . --upgrade__)

### Updating Without Cloning
1. Update module (__pip install git+https://github.com/czbiohub/PyRasPi --upgrade__)

### Using Module
1. Edit files to include `import pyraspi` or a variant such as `from pyraspi import RPiOut`
2. Activate virtual environment with module installed
3. Execute python script or application

## Testing Module for Completeness
Before using this code or updating to newer versions, it would be wise to check for completeness. Breaking changes that can impact your work occasionally occur during development. Although major and minor versioning of code helps indicate when specific interfaces may no longer be compatible with previous versions, there can also be smaller code breaks that cause methods to silently fail.

This repository includes unit tests that can be used to assess the health of the code. Whenever a new feature is added, new tests are made to confirm that the feature behaves correctly. Whenever a feature is changed, the old tests should be updated to reflect the new behavior. If an author breaks code and does not fix the issue, the previously written tests should fail. You can evaluate these tests for yourself by running the command __make__ in the outer directory of the repository.


## How to Contribute
If you would like to contribute to PyMotors, please review the guidelines described in [CONTRIBUTING.md](https://github.com/czbiohub/PyConfigHandler/blob/master/CONTRIBUTING.md).
