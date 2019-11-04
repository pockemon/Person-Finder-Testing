"""Unittest initialization for handlers.  No actual tests"""

import main
import webob
import urllib

from google.appengine.ext import webapp


def initialize_handler(
        handler_class, action, repo='haiti', environ=None, params=None):
    """Initialize handler_cless and return initialized handler.
    """

    params_str = ('?' + urllib.urlencode(params)) if params else ''
    request = webapp.Request(webob.Request.blank(
        '/' + repo + '/' + action + params_str, environ=environ).environ)
    response = webapp.Response()
    return handler_class(request, response, main.setup_env(request))
