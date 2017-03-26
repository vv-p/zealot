import unittest
import zealot.conf

# Test settings
ENABLE_TIMEOUTS = False
DEFAULT_TIMEOUT = 7
TEST_ME = 'Some string here'


class TestEnableTimeouts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        zealot.conf.settings = zealot.conf.Settings(settings_module='test_user_settings')
        cls.settings = zealot.conf.settings

    def test_timeout_disable(self):
        self.assertEqual(self.settings.ENABLE_TIMEOUTS, ENABLE_TIMEOUTS)

    def test_default_timeout(self):
        self.assertEqual(self.settings.DEFAULT_TIMEOUT, DEFAULT_TIMEOUT)

    def test_me(self):
        self.assertEqual(self.settings.TEST_ME, TEST_ME)
