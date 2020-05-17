from utils.util import Util

"""
Authors:
Forgacs Amelia
Dragan Alex
Enasoae Simona
VVSS
Date: 19.05.2020
"""

import unittest

class TestUtil(unittest.TestCase):

    def test_UtilIsOnlyDigits(self):

        number = "07464393"
        self.assertTrue(Util.isOnlyDigits(number))

        number = "fjfkg99"
        self.assertFalse(Util.isOnlyDigits(number))

if __name__ == '__main__':
    unittest.main()