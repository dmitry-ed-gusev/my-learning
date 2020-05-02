################################################################################
#
#	Test script for converter from DECIMAL to BINARY.
#
#	Created:  Ishkinin Dmitrii, 13.02.2020
#	Modified:
#
################################################################################

import unittest
from dec2bin import convert_dec2bin


class TestDec2Bin(unittest.TestCase):

    def test_dec2bin(self):
        self.assertEqual("0b0", str(convert_dec2bin(0)))
        self.assertEqual("0b1", str(convert_dec2bin(1)))
        self.assertEqual("0b11", str(convert_dec2bin(3)))
        self.assertEqual("0b1010", str(convert_dec2bin(10)))
        self.assertEqual("0b1011", str(convert_dec2bin(11)))

    def test_dec2bin_with_string(self):
        with self.assertRaises(TypeError):
            convert_dec2bin("sss")
