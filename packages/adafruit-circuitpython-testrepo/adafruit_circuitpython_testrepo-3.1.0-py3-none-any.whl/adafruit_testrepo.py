# SPDX-FileCopyrightText: 2019 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_testrepo`
================================================================================


    This repo exists solely for test purposes!


* Author(s): Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

note::

    PyPI will reject a release if no source code has changed.
    Please increment this counter if needed: 4

"""

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_TestRepo.git"


class Test:
    """Test class."""

    def __init__(self):
        self._test_value = "Untested"

    @staticmethod
    def test():
        """Test function."""
        while True:
            pass

    def test_method(self):
        """Test method."""
        return "Test value {}".format(self._test_value)

    @property
    def test_property(self):
        """Test property"""
        return self._test_value

    @test_property.setter
    def test_property(self, value):
        self._test_value = value
