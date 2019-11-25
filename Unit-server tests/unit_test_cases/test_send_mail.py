"""Tests for send_mail.py."""

from google.appengine.api import mail
from google.appengine.api import mail_errors
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import model
import mox
import os
import send_mail
import unittest
import webob

class SendMailTests(unittest.TestCase):
    '''Test the send_mail error handling.'''

    def test_email_fail(self):
        subject = 'test'
        to = 'bad_email_address'
        sender = 'me@example.com'
        body = 'stuff'
        mymox = mox.Mox()
        mymox.StubOutWithMock(logging, 'error')
        logging.error('EmailSender (to: %s, subject: %s), '
                      'failed with exception %s' % (to, subject, 'exception'))
        mymox.StubOutWithMock(mail, 'send_mail')
        mail.send_mail(sender=sender,
                       subject=subject,
                       to=to,
                       body=body).AndRaise(mail_errors.Error('exception'))
        handler = send_mail.EmailSender()
        repo = 'haiti'
        model.Repo(key_name=repo).put()
        request = webapp.Request(
            webob.Request.blank(
                '/admin/send_mail?to=%s&subject=%s&sender=%s' %
                (to, subject, sender)).environ)
        request.method = 'POST'
        request.body = 'body=%s' % body
        handler.initialize(request, webapp.Response())
        mymox.ReplayAll()
        handler.post()
        # shouldn't raise an error.
        assert True
        mymox.VerifyAll()
