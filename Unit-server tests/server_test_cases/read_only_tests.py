"""Test cases for end-to-end testing.  Run with the server_tests script."""

import scrape
from server_tests_base import ServerTestsBase

class ReadOnlyTests(ServerTestsBase):
    """Tests that don't modify data go here."""

    def setUp(self):
        """Sets up a scrape Session for each test."""
        self.s = scrape.Session(verbose=1)
        # These tests don't rely on utcnow, so don't bother to set it.

    def tearDown(self):
        # These tests don't write anything, so no need to reset the datastore.
        pass

    def test_noconfig(self):
        """Check the home page with no config (generic welcome page)."""
        doc = self.go('/')
        assert 'You are now running Person Finder.' in doc.text

    def test_start(self):
        """Check the start page with no language specified."""
        doc = self.go('/haiti')
        assert 'I\'m looking for someone' in doc.text

    def test_start_english(self):
        """Check the start page with English language specified."""
        doc = self.go('/haiti?lang=en')
        assert 'I\'m looking for someone' in doc.text
