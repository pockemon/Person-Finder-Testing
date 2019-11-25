"""Tests for importer.py."""

import datetime
import unittest

from google.appengine.ext import db
from pytest import raises

import model
import importer

TEST_DATETIME = datetime.datetime(2010, 1, 1, 0, 0, 0)

def put_dummy_person_record(repo, person_record_id):
    db.put(model.Person(
        key_name='%s:%s' % (repo, person_record_id),
        repo=repo,
        author_name='_test_author_name',
        full_name='_test_given_name _test_family_name',
        given_name='_test_given_name',
        family_name='_test_family_name',
        source_date=TEST_DATETIME,
        entry_date=TEST_DATETIME,
    ))

class ImporterTests(unittest.TestCase):
    """Test the import utilities."""

    def tearDown(self):
        db.delete(model.Person.all())
        db.delete(model.Note.all())

    def test_strip(self):
        assert importer.strip('') == ''
        assert importer.strip(None) == ''
        assert importer.strip(0) == ''
        assert importer.strip(' ') == ''
        assert importer.strip(' \t') == ''
        assert importer.strip('\t ') == ''
        assert importer.strip(' \n ') == ''
        assert importer.strip('abc') == 'abc'
        assert importer.strip('a b\tc ') == 'a b\tc'
        assert importer.strip(' a b\tc\t') == 'a b\tc'

    def test_validate_datetime(self):
        assert importer.validate_datetime('2010-01-01T00:00:00Z') == \
            datetime.datetime(2010, 1, 1, 0, 0, 0)
        assert importer.validate_datetime('2010-01-01T01:23:45Z') == \
            datetime.datetime(2010, 1, 1, 1, 23, 45)

        assert importer.validate_datetime('') == None
        assert importer.validate_datetime(0) == None

        raises(ValueError, importer.validate_datetime, ' ')
        raises(ValueError, importer.validate_datetime, '2010-02-28')
        raises(ValueError, importer.validate_datetime, '2010-02-28 01:23:45')
        raises(ValueError, importer.validate_datetime, '2010-02-28 01:23:45Z')
        raises(ValueError, importer.validate_datetime, '2010-02-28 1:23:45')

    def test_validate_boolean(self):
        assert importer.validate_boolean('true')
        assert importer.validate_boolean('TRUE')
        assert importer.validate_boolean('True')
        assert importer.validate_boolean('trUe')
        assert importer.validate_boolean('1')

        assert not importer.validate_boolean('false')
        assert not importer.validate_boolean('ture')
        assert not importer.validate_boolean('')
        assert not importer.validate_boolean(None)
        assert not importer.validate_boolean(1)

    def test_create_person(self):
        # clone record
        fields = {'given_name': ' Zhi\n',
                  'family_name': ' Qiao',
                  'person_record_id': '  test_domain/person_1 '}
        person = importer.create_person('haiti', fields)
        assert hasattr(person, 'entry_date')
        assert hasattr(person, 'last_modified')
        assert person.given_name == 'Zhi'
        assert person.family_name == 'Qiao'
        assert person.record_id == 'test_domain/person_1'
        assert person.key().kind() == 'Person'
        assert person.key().id() == None
        assert person.key().name() == 'haiti:test_domain/person_1'

        # original record with new record_id
        fields = {'given_name': ' Zhi\n',
                  'family_name': ' Qiao'}
        person = importer.create_person('haiti', fields)
        assert person.record_id.startswith(
            'haiti.%s/person.' % model.HOME_DOMAIN)

        # original record with specified record_id
        fields = {'given_name': ' Zhi\n',
                  'family_name': ' Qiao',
                  'person_record_id': model.HOME_DOMAIN + '/person.23 '}
        person = importer.create_person('haiti', fields)
        assert person.record_id == model.HOME_DOMAIN + '/person.23'

    def test_create_note(self):
        # clone record
        fields = {'note_record_id': ' test_domain/note_1',
                  'person_record_id': '  test_domain/person_1 '}

        # source_date should be required.
        raises(AssertionError, importer.create_note, 'haiti', fields)

        # With source_date, the conversion should succeed.
        fields['source_date'] = '2010-01-02T12:34:56Z'
        note = importer.create_note('haiti', fields)
        assert note.record_id == 'test_domain/note_1'
        assert note.person_record_id == 'test_domain/person_1'
        assert note.status == ''
        assert note.key().kind() == 'Note'
        assert note.key().id() == None
        assert note.key().name() == 'haiti:test_domain/note_1'

        # original record
        fields = {'person_record_id': '  test_domain/person_1 ',
                  'source_date': '2010-01-02T03:04:05Z'}
        note = importer.create_note('haiti', fields)
        assert note.record_id.startswith('haiti.%s/note.' % model.HOME_DOMAIN)
        assert note.person_record_id == 'test_domain/person_1'

    def test_import_person_records(self):
        records = []
        for i in range(20):
            given_name = "given_name_%d" % i
            family_name = "family_name_%d" % i

            source_date = "2010-01-01T01:23:45Z"
            record_id = "test_domain/%d" % i

            # Records 0, 8, and 16 have bad domains.
            if not i % 8:
                record_id = "other_domain/%d" % i
            # Records 0, 9, and 18 have invalid dates.
            elif not i % 9:
                source_date = "2010-01-01 01:23:45"

            records.append({'given_name': given_name,
                            'family_name': family_name,
                            'person_record_id': record_id,
                            'source_date': source_date})
        written, skipped, total = importer.import_records(
            'haiti', 'test_domain', importer.create_person, records, False,
            True, None)

        assert written == 15
        assert len(skipped) == 5
        assert skipped[0] == (
            'Not in authorized domain: u\'other_domain/0\'', {
                'given_name': 'given_name_0',
                'family_name': 'family_name_0',
                'source_date': '2010-01-01T01:23:45Z',
                'person_record_id': 'other_domain/0'
            })
        assert skipped[3] == (
            'Not in authorized domain: u\'other_domain/16\'', {
                'given_name': 'given_name_16',
                'family_name': 'family_name_16',
                'source_date': '2010-01-01T01:23:45Z',
                'person_record_id': 'other_domain/16'
            })
        assert skipped[2] == (
            'ValueError: Bad datetime: \'2010-01-01 01:23:45\'', {
                'given_name': 'given_name_9',
                'family_name': 'family_name_9',
                'source_date': '2010-01-01 01:23:45',
                'person_record_id': 'test_domain/9'
            })
        assert skipped[4] == (
            'ValueError: Bad datetime: \'2010-01-01 01:23:45\'', {
                'given_name': 'given_name_18',
                'family_name': 'family_name_18',
                'source_date': '2010-01-01 01:23:45',
                'person_record_id': 'test_domain/18'
            })
        assert total == 20

        # Also confirm that 15 records were put into the datastore.
        assert model.Person.all().count() == 15

    def test_import_note_records(self):
        # Prepare person records which the notes will be added to.
        for domain in ['test_domain', 'other_domain']:
            for i in range(20):
                put_dummy_person_record('haiti', '%s/person_%d' % (domain, i))

        records = []
        for i in range(20):
            source_date = '2010-01-01T01:23:45Z'
            note_id = 'test_domain/record_%d' % i
            person_id = 'test_domain/person_%d' % i

            # Records 0, 8, and 16 have bad note record domains.
            if not i % 8:
                note_id = 'other_domain/record_%d' % i
            # Records 0, 9, and 18 have bad person record domains.
            # This should not matter for note records.
            elif not i % 9:
                person_id = 'other_domain/person_%d' % i
            # Records 0, 5, 10, and 15 have invalid dates.
            elif not i % 5:
                source_date = '2010-01-01 01:23:45'

            records.append({'person_record_id': person_id,
                            'note_record_id': note_id,
                            'source_date': source_date})
        written, skipped, total = importer.import_records(
            'haiti', 'test_domain', importer.create_note, records, False,
            True, None)

        assert written == 14
        assert len(skipped) == 6
        assert skipped[0] == (
            'Not in authorized domain: u\'other_domain/record_0\'', {
                'person_record_id': 'test_domain/person_0',
                'source_date': '2010-01-01T01:23:45Z',
                'note_record_id': 'other_domain/record_0'
            })
        assert skipped[2] == (
            'Not in authorized domain: u\'other_domain/record_8\'', {
                'person_record_id': 'test_domain/person_8',
                'source_date': '2010-01-01T01:23:45Z',
                'note_record_id': 'other_domain/record_8'
            })
        assert skipped[1] == (
            'ValueError: Bad datetime: \'2010-01-01 01:23:45\'', {
                'person_record_id': 'test_domain/person_5',
                'source_date': '2010-01-01 01:23:45',
                'note_record_id': 'test_domain/record_5'
            })
        assert skipped[4] == (
            'ValueError: Bad datetime: \'2010-01-01 01:23:45\'', {
                'person_record_id': 'test_domain/person_15',
                'source_date': '2010-01-01 01:23:45',
                'note_record_id': 'test_domain/record_15'
            })
        assert total == 20
        # Also confirm that 14 records were put into the datastore.
        assert model.Note.all().count() == 14
        # Confirm all records are NOT marked reviewed.
        for note in model.Note.all():
            assert note.reviewed == False

if __name__ == "__main__":
    unittest.main()
