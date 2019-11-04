"""Unittest for api.py module."""

import datetime
import unittest

import api
import model
import test_handler

from google.appengine.ext import testbed

class APITests(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_sms_render_person(self):
        handler = test_handler.initialize_handler(
            api.HandleSMS, 'api/handle_sms')

        person = model.Person.create_original(
            'haiti',
            full_name='John Smith',
            latest_status='believed_alive',
            sex='male',
            age='30',
            home_city='Los Angeles',
            home_state='California',
            entry_date=datetime.datetime(2010, 1, 1))
        assert (handler.render_person(person) ==
            'John Smith / '
            'Someone has received information that this person is alive / '
            'male / 30 / From: Los Angeles California')

        person = model.Person.create_original(
            'haiti',
            full_name='John Smith',
            entry_date=datetime.datetime(2010, 1, 1))
        assert handler.render_person(person) == 'John Smith'

        person = model.Person.create_original(
            'haiti',
            full_name='John Smith',
            home_state='California',
            entry_date=datetime.datetime(2010, 1, 1))
        assert handler.render_person(person) == 'John Smith / From: California'
