"""Tests for create.py."""

import datetime
import unittest

from google.appengine.ext import webapp
from pytest import raises

import create

class CreateTests(unittest.TestCase):
    def test_validate_date(self):
        assert create.validate_date('2008-09-12') == \
            datetime.datetime(2008, 9, 12)
        raises(ValueError, create.validate_date, '2008-09-12-1')
        raises(ValueError, create.validate_date, '2008-09')
        raises(ValueError, create.validate_date, '2008-13-12')
        raises(ValueError, create.validate_date, '2008-09-31')
        raises(Exception, create.validate_date, None)

if __name__ == '__main__':
    unittest.main()
