#!/usr/bin/env python3.6

import unittest

from time import sleep
from zealot.utils import waiting_for
from zealot.exceptions import TimeoutException, InvalidArgumentException


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

    def test_invalid_func_decorated(self):
        with self.assertRaises(InvalidArgumentException):
            f = waiting_for(1)
