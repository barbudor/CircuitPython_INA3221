
Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-ina3221/badge/?version=latest
    :target: https://circuitpython-ina3221.readthedocs.io/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://travis-ci.com/barbudor/CircuitPython_INA3221.svg?branch=master
    :target: https://travis-ci.com/barbudor/CircuitPython_INA3221
    :alt: Build Status

CircuitPython driver for the Texas Instruments' INA3221 3 channels current sensor.
Product page at `ti.com <http://www.ti.com/product/INA3221>`_.

2 version are available:

* ``barbudor_ina3221.full``	includes all constants for low-level register access + API for alarms
* ``barbudor_ina3221.lite``	only basic API and no constants - use less memory

Pick only one depending your needs. On processors with limited amount of memory (SAMD21), the
lite version is recommended. You may want to use ``mpy-cross`` to precompile the library to an
``.mpy`` file for lower memory footprint.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-neopixel/>`_. To install for current user:

.. code-block:: shell

    pip3 install --user barbudor-circuitpython-ina3221

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install barbudor-circuitpython-ina3221

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install barbudor-circuitpython-ina3221

Usage Example
=============

see `example <https://github.com/barbudor/CircuitPython_INA3221/blob/master/examples/ina3221_simpletest.py>`_.

Contributing
============

Contributions welcomed. My goal is to keep the library simple and as low on memory as possible.
