"""Tests for photo.py."""

import os
import unittest

import model
import photo
import test_handler

from google.appengine.ext import testbed

class PhotoTests(unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_user_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_photo_url(self):
        entity = model.Photo.create('haiti', image_data='xyz')
        entity.put()
        id = entity.key().name().split(':')[1]

        os.environ['HTTP_HOST'] = 'example.appspot.com'
        ph = test_handler.initialize_handler(
            photo.Handler, 'photo', environ=os.environ)
        self.assertEquals(
            'http://example.appspot.com/haiti/photo?id=%s' % id,
            photo.get_photo_url(entity, 'haiti', ph.transitionary_get_url))


if __name__ == '__main__':
    unittest.main()
