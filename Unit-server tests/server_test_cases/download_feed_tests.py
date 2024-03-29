"""Test cases for end-to-end testing.  Run with the server_tests script."""

import os
import tempfile
import download_feed
from server_tests_base import ServerTestsBase

class DownloadFeedTests(ServerTestsBase):
    """Tests for the tools/download_feed.py script."""
    def setUp(self):
        ServerTestsBase.setUp(self)
        self.setup_person_and_note()
        fd, self.filename = tempfile.mkstemp()
        os.close(fd)

    def tearDown(self):
        os.remove(self.filename)
        ServerTestsBase.tearDown(self)

    def test_download_xml(self):
        url = 'http://%s/personfinder/haiti/feeds/person' % self.hostport
        download_feed.main('-q', '-o', self.filename, url)
        output = open(self.filename).read()
        assert '<pfif:pfif ' in output
        assert '<pfif:person>' in output
        assert '<pfif:given_name>_test_given_name</pfif:given_name>' in output

    def test_download_csv(self):
        url = 'http://%s/personfinder/haiti/feeds/person' % self.hostport
        download_feed.main('-q', '-o', self.filename, '-f', 'csv',
                           '-F', 'family_name,given_name,age', url)
        lines = open(self.filename).readlines()
        assert len(lines) == 2
        assert lines[0].strip() == 'family_name,given_name,age'
        assert lines[1].strip() == '_test_family_name,_test_given_name,52'

    def test_download_notes(self):
        url = 'http://%s/personfinder/haiti/feeds/note' % self.hostport
        download_feed.main('-q', '-o', self.filename, '-n', url)
        output = open(self.filename).read()
        assert '<pfif:pfif ' in output
        assert '<pfif:note>' in output
        assert '<pfif:text>Testing</pfif:text>' in output
