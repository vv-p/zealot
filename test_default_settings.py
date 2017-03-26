#!/usr/bin/env python3.6

import unittest

from zealot.conf import settings


class TestWaitingFor(unittest.TestCase):

    def test_default_timeout(self):
        self.assertEqual(settings.DEFAULT_TIMEOUT, 1)

    def test_default_timeout_enable(self):
        self.assertTrue(settings.ENABLE_TIMEOUTS)


