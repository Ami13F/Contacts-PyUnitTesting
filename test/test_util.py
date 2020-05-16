from utils.util import Util

__author__ = 'Team0'

import unittest


class TestUtil(unittest.TestCase):

    def test_methods(self):

        s = "07464393"
        self.assertTrue(Util.isOnlyDigits(s))

        s = "fjfkg99"
        self.assertFalse(Util.isOnlyDigits(s))
