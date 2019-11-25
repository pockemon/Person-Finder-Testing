"""Unittest for indexing.py module."""

from google.appengine.ext import db
import datetime
import indexing
import logging
import model
import sys
import unittest

from text_query import TextQuery

def create_person(given_name, family_name):
    return model.Person.create_original(
        'test', given_name=given_name, family_name=family_name,
        full_name=('%s %s' % (given_name, family_name)),
        entry_date=datetime.datetime.utcnow())

class IndexingTests(unittest.TestCase):
    def setUp(self):
        db.delete(model.Person.all())

    def tearDown(self):
        db.delete(model.Person.all())

    def add_persons(self, *persons):
        for p in persons:
            indexing.update_index_properties(p)
            db.put(p)

    def get_matches(self, query, limit=100):
        results = indexing.search('test', TextQuery(query), limit)
        return [(p.given_name, p.family_name) for p in results]

    def get_ranked(self, results, query, limit=100):
        ranked = indexing.rank_and_order(results, TextQuery(query), limit)
        return [(p.given_name, p.family_name) for p in results]

    def test_rank_and_order(self):
        res= [create_person(given_name='Bryan', family_name='abc', ),
              create_person(given_name='Bryan', family_name='abcef'),
              create_person(given_name='abc', family_name='Bryan'),
              create_person(given_name='Bryan abc', family_name='efg')]

        sorted = indexing.rank_and_order(res, TextQuery('Bryan abc'), 100)
        assert ['%s %s'%(p.given_name, p.family_name) for p in sorted] == \
            ['Bryan abc', 'abc Bryan', 'Bryan abc efg', 'Bryan abcef']

        sorted = indexing.rank_and_order(res, TextQuery('Bryan abc'), 2)
        assert ['%s %s'%(p.given_name, p.family_name) for p in sorted] == \
            ['Bryan abc', 'abc Bryan']

        sorted = indexing.rank_and_order(res, TextQuery('abc Bryan'), 100)
        assert ['%s %s'%(p.given_name, p.family_name) for p in sorted] == \
            ['abc Bryan', 'Bryan abc', 'Bryan abc efg', 'Bryan abcef']

        res= [create_person(given_name='abc', family_name='efg'),
              create_person(given_name='ABC', family_name='EFG'),
              create_person(given_name='ABC', family_name='efghij')]

        sorted = indexing.rank_and_order(res, TextQuery('abc'), 100)
        assert ['%s %s'%(p.given_name, p.family_name) for p in sorted] == \
            ['abc efg', 'ABC EFG', 'ABC efghij']

    def test_cjk_ranking_1(self):
        # This is Jackie Chan's Chinese name.  His family name is CHAN and given
        # name is KONG + SANG; the usual Chinese order is CHAN + KONG + SANG.
        CHAN, KONG, SANG = u'\u9673', u'\u6e2f', u'\u751f'

        # This is I. M. Pei's Chinese name.  His family name is BEI and his
        # given name is YU + MING; the usual Chinese order is BEI + YU + MING.
        BEI, YU, MING = u'\u8c9d', u'\u807f', u'\u9298'
        persons = [
            create_person(given_name=CHAN + KONG + SANG, family_name='foo'),
            create_person(given_name=SANG, family_name=CHAN + KONG),
            create_person(given_name=CHAN, family_name=KONG + SANG),
            create_person(given_name=KONG + SANG, family_name=CHAN),
            create_person(given_name=KONG + CHAN, family_name=SANG),
            create_person(given_name=KONG, family_name=SANG),
            create_person(given_name=YU + MING, family_name=BEI),
        ]

        assert self.get_ranked(persons, CHAN + KONG + SANG) == [
            (KONG + SANG, CHAN),  # surname + given name is best
            (SANG, CHAN + KONG),  # then multi-char surname + given name
            (CHAN, KONG + SANG),  # then surname/given switched
            (KONG + CHAN, SANG),  # then out-of-order match
            (CHAN + KONG + SANG, 'foo'),  # then exact given name match
            (KONG, SANG),  # then partial match
            (YU + MING, BEI),  # then nothing match
        ]

        assert self.get_ranked(persons, CHAN + ' ' + KONG + SANG) == [
            (KONG + SANG, CHAN),  # surname + given name is best
            (CHAN, KONG + SANG),  # then surname/given switched
            (KONG + CHAN, SANG),  # then multi-char surname / given switched
            (SANG, CHAN + KONG),  # then out-of-order match
            (CHAN + KONG + SANG, 'foo'),  # then exact given name match
            (KONG, SANG),  # then partial match
            (YU + MING, BEI),  # then nothing match
        ]

    def test_sort_query_words(self):
        # Sorted lexicographically.
        assert indexing.sort_query_words(
            ['CC', 'BB', 'AA']) == ['AA', 'BB', 'CC']
        # Sorted by lengths.
        assert indexing.sort_query_words(
            ['A', 'AA', 'AAA']) == ['AAA', 'AA', 'A']
        # Sorted by popularity.
        assert indexing.sort_query_words(
            [u'川', u'口', u'良']) == [u'口', u'良', u'川']
        # Test sort key precedence.
        assert indexing.sort_query_words(
            ['CCC', 'BB', 'AA', 'A']) == ['CCC', 'AA', 'BB', 'A']

    def test_no_query_terms(self):
        # Regression test (this used to throw an exception).
        assert indexing.search('test', TextQuery(''), 100) == []

if __name__ == '__main__':
    logging.basicConfig( stream=sys.stderr )
    unittest.main()
