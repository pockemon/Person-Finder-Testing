"""Test cases for end-to-end testing.  Run with the server_tests script."""

import simplejson
from model import *
import setup_pf as setup
from server_tests_base import ServerTestsBase

class ConfigTests(ServerTestsBase):
    """Tests related to configuration settings (ConfigEntry entities)."""

    # Repo and ConfigEntry entities should be wiped between tests.
    kinds_to_keep = ['Authorization']

    def tearDown(self):
        ServerTestsBase.tearDown(self)

        # Restore the configuration settings.
        setup.setup_repos()
        setup.setup_configs()

        # Flush the configuration cache.
        config.cache.enable(False)
        self.go('/haiti?lang=en&flush=config')

    def get_admin_page_error_message(self):
        error_divs = self.s.doc.cssselect('div.error')
        if error_divs:
            return 'Error message: %s' % error_divs[0].text
        else:
            return 'Whole page HTML:\n%s' % self.s.doc.content

    def test_no_exception_for_unset_key(self):
        # Tests that a config will return None, and not throw an exception, when
        # asked for the value of an unknown key.
        config.set_for_repo('*', good_key_1='abc', good_key_2='def')
        config.set_for_repo('foo', good_key_1='ghi')
        cfg = config.Configuration('foo')
        assert cfg['good_key_1'] == 'ghi'
        assert cfg['good_key_2'] == 'def'
        assert cfg['unknown_key'] is None

    def test_get_with_default(self):
        config.set_for_repo('foo', key_1='abc')
        cfg = config.Configuration('foo')
        assert cfg.get('unknown_key', 'default_value') == 'default_value'

    def test_configuration_not_callable(self):
        """Checks that a Configuration instance is not callable.

        This is required to make it work in Django template. See the comment of
        config.Configuration.__getattr__() for details.
        """
        cfg = config.Configuration('xyz')
        assert not callable(cfg)
