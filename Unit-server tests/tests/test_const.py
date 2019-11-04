"""Tests for const."""

from __future__ import absolute_import
import const
import pfif
import unittest

class ConstTests(unittest.TestCase):
    def test_constants(self):
        # Ensure const.py is consistent with pfif.py.
        assert set(const.PERSON_SEX_TEXT) == set(pfif.PERSON_SEX_VALUES)
        assert set(const.NOTE_STATUS_TEXT) == set(pfif.NOTE_STATUS_VALUES)
        assert set(const.PERSON_STATUS_TEXT) == set(pfif.NOTE_STATUS_VALUES)
