#!/usr/bin/env python3.6

from time import sleep
from zealot.utils import waiting_for
from zealot.exceptions import TimeoutException

import unittest


def sleeper(how_long_have_i_sleep):
    sleep(how_long_have_i_sleep)
    return how_long_have_i_sleep


class TestWaitingFor(unittest.TestCase):

    def test_timeout_raises(self):
        f = waiting_for(timeout=1)(sleeper)
        with self.assertRaises(TimeoutException):
            f(2)

    def test_timeout_passes(self):
        f = waiting_for(timeout=3)(sleeper)
        self.assertEqual(f(1), 1)
