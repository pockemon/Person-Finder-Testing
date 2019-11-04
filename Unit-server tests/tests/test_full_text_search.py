"""Tests for full_text_search.py"""

import datetime
import unittest

from google.appengine.ext import db
from google.appengine.ext import testbed
from google.appengine.api import search
import sys
import logging
import delete
import full_text_search
import model

TEST_DATETIME = datetime.datetime(2010, 1, 1, 0, 0, 0)

class FullTextSearchTests(unittest.TestCase):
    def setUp(self):
        self.tb = testbed.Testbed()
        self.tb.activate()
        self.tb.init_search_stub()
        self.p1 = model.Person.create_original_with_record_id(
            'haiti',
            'haiti/0505',
            given_name='Iori',
            family_name='Minase',
            full_name='Iori Minase',
            alternate_names='Iorin',
            entry_date=TEST_DATETIME
        )
        self.p2 = model.Person.create_original_with_record_id(
            'haiti',
            'haiti/1123',
            given_name='Miki',
            family_name='Hoshii',
            full_name='Miki Hoshii',
            entry_date=TEST_DATETIME
        )
        self.p3 = model.Person.create_original_with_record_id(
            'haiti',
            'haiti/0522',
            given_name='Ami',
            family_name='Futami',
            full_name='Ami Futami',
            entry_date=TEST_DATETIME
        )
        self.p4 = model.Person.create_original_with_record_id(
            'haiti',
            'haiti/0225',
            given_name='Chihaya',
            family_name='Kisaragi',
            full_name='Chihaya Kisaragi',
            home_street='Kunaideme72',
            home_city='Arao',
            home_state='Kumamoto',
            home_postal_code='864-0003',
            home_neighborhood='Araokeibajou',
            home_country='Japan',
            entry_date=TEST_DATETIME
        )
        self.p5 = model.Person.create_original_with_record_id(
            'haiti',
            'haiti:0810',
            given_name='Rin',
            family_name='Shibuya',
            full_name='Rin Shibuya',
            home_city='shinjuku',
            entry_date=TEST_DATETIME
        )

    def tearDown(self):
        db.delete(model.Person.all())
        self.tb.deactivate()

    def test_search_by_name_only(self):
        db.put(self.p1)
        db.put(self.p2)
        db.put(self.p3)
        db.put(self.p4)
        db.put(self.p5)
        full_text_search.add_record_to_index(self.p1)
        full_text_search.add_record_to_index(self.p2)
        full_text_search.add_record_to_index(self.p3)
        full_text_search.add_record_to_index(self.p4)
        full_text_search.add_record_to_index(self.p5)

        # Search by alternate name - p1
        results = full_text_search.search('haiti', {'name': 'Iorin'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0505'])

        # Search by family name -p1
        results = full_text_search.search('haiti', {'name': 'Minase'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0505'])

        # Search by given name - p1
        results = full_text_search.search('haiti', {'name': 'Iori'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0505'])

        # Search by given name + family name - p1
        results = full_text_search.search('haiti', {'name': 'Minase Iori'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0505'])

        # Search by full name - p1
        resutls = full_text_search.search('haiti', {'name': 'Iori Minase'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0505'])

        # Search by a name contains location - p4
        results = full_text_search.search('haiti', {'name': 'Chihaya Arao'}, 5)
        assert not results

        # Search by name & location - p4
        results = full_text_search.search('haiti', {'name':'Chihaya',
                                                    'location': 'Arao'}, 5)
        assert set([r.record_id for r in results]) == \
            set(['haiti/0225'])

        # Search by home_street only ( input inside the name box) - p4
        results = full_text_search.search('haiti', {'name': 'Kunaideme72'}, 5)
        assert not results

        # Search by home_city only ( input inside the location box) - p4
        results = full_text_search.search('haiti', {'location': 'Arao'}, 5)
        assert not results

        # Search by home_state only ( input inside the location box) - p4
        results = full_text_search.search('haiti', {'location': 'Kumamoto'}, 5)
        assert not results

        # Search by home_postal_code only ( input inside the name box) - p4
        results = full_text_search.search('haiti', {'name': '864-0003'}, 5)
        assert not results

        # Search by home_neighborhood only ( input inside the location box) - p4
        results = full_text_search.search(
                                    'haiti', {'location': 'Araokeibajou'}, 5)
        assert not results

        # Search by home_country only ( input inside the name box) - p4
        results = full_text_search.search('haiti', {'name': 'Japan'}, 5)
        assert not results

        # Check no results
        results = full_text_search.search('haiti', {'name': 'Producer san'}, 5)
        assert not results

        # Search with no query text
        results = full_text_search.search(
                                    'haiti', {'name': '', 'location': ''}, 5)
        assert not results

        # Search deleted record - p3
        delete.delete_person(self, self.p3)
        results = full_text_search.search('haiti', {'name': 'Ami'}, 5)
        assert not results

        # Search with empty dict
        results = full_text_search.search('haiti', {}, 5)

        # Search by full name - p5
        results = full_text_search.search('haiti', {'name': 'Rin Shibuya'}, 5)
        assert set([r.record_id for r in results]) == \
               set(['haiti:0810'])


        # Search Name with Location part contain a part of person's name - p5
        results = full_text_search.search('haiti',
                                          {'name': 'Rin Shibuya',
                                           'location': 'Shinjuku Rin'}, 5)
        assert not results

        # Input the name and location in the wrong box - p5
        results = full_text_search.search('haiti',
                                          {'name': 'Shinjuku',
                                           'location': 'Rin Shibuya'}, 5)
        assert not results

    def test_delete_record_from_index(self):
        db.put(self.p2)
        full_text_search.add_record_to_index(self.p2)
        full_text_search.delete_record_from_index(self.p2)
        results = full_text_search.search('haiti',  {'name': 'Miki'}, 5)
        assert not results
