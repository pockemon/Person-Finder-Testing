"""Unittest for tasks.py module."""

import calendar
import datetime
import logging
import mox
import os
import sys
import unittest
import urllib
import webob

from google.appengine import runtime
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.api import quota
from google.appengine.api import taskqueue
from google.appengine.ext import testbed
from google.appengine.ext import webapp

import config
import const
import delete
import model
import tasks
import test_handler
from utils import get_utcnow, set_utcnow_for_test

class NotifyManyUnreviewedNotesTests(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_mail_stub()
        # root_path must be set the the location of queue.yaml.
        # Otherwise, only the 'default' queue will be available.
        path_to_app = os.path.join(os.path.dirname(__file__), '../app')
        self.testbed.init_taskqueue_stub(root_path=path_to_app)
        model.Repo(key_name='haiti').put()

    def tearDown(self):
        self.testbed.deactivate()

    def test_should_notify_empty_email(self):
        # If email is empty, always False is returned.
        config.set(notification_email='',
                   unreviewed_notes_threshold=9)
        handler = self.get_handler()
        self.assert_(not handler._should_notify(10))

    def test_should_notify_threshold(self):
        config.set(notification_email='inna-testing@gmail.com',
                   unreviewed_notes_threshold=100)
        handler = self.get_handler()
        # The number of unreviewed_notes larger than threshold: True
        self.assert_(handler._should_notify(101))
        # The number of unreviewed_notes is equal to threshold: False
        self.assert_(not handler._should_notify(100))
        # The number of unreviewed_notes is smaller than threshold: False
        self.assert_(not handler._should_notify(99))

    def get_handler(self):
        # The handler can't be initialized until after the config is set up.
        return test_handler.initialize_handler(
            handler_class=tasks.NotifyManyUnreviewedNotes,
            action=tasks.NotifyManyUnreviewedNotes.ACTION,
            repo='haiti', environ=None, params=None)
