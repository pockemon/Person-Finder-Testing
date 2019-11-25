"""Test cases for end-to-end testing.  Run with the server_tests script."""

import datetime
import os
import re
import tempfile
from model import *
from server_tests_base import ServerTestsBase

class ImportTests(ServerTestsBase):
    """Tests for CSV import page at /api/import."""
    def setUp(self):
        ServerTestsBase.setUp(self)
        Repo(
            key_name='haiti',
            activation_status=Repo.ActivationStatus.ACTIVE).put()
        config.set_for_repo(
            'haiti',
            api_action_logging=True)
        self.filename = None

    def tearDown(self):
        if self.filename:
            os.remove(self.filename)
        ServerTestsBase.tearDown(self)

    def _write_csv_file(self, content):
        # TODO(ryok): We should use StringIO instead of a file on disk. Update
        # scrape.py to support StringIO.
        fd, self.filename = tempfile.mkstemp()
        os.fdopen(fd, 'w').write('\n'.join(content))

    def test_import_no_csv(self):
        """Verifies an error message is shown when no CSV file is uploaded."""
        doc = self.go('/haiti/api/import')
        form = doc.cssselect_one('form#persons-import-form')
        doc = self.s.submit(form, key='test_key')
        assert 'Please specify at least one CSV file.' in doc.text

    def test_import_broken_csv(self):
        """Verifies an error message is shown when a broken CSV is imported."""
        self._write_csv_file([
            'person_record_id,source_date,\0full_name',  # contains null
            'test.google.com/person1,2013-02-26T09:10:00Z,_test_full_name',
            ])
        doc = self.go('/haiti/api/import')
        form = doc.cssselect_one('form#persons-import-form')
        doc = self.s.submit(form, key='test_key', content=open(self.filename))
        assert 'The CSV file is formatted incorrectly' in doc.text
        assert Person.all().count() == 0
        assert Note.all().count() == 0
