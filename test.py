
# how was my code error free, highest stantard - TDD

from calc import SimpleCalc # will need to create file and class with functionality
import unittest
import pytest

class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_sub(self):
        self.assertEqual(self.calc_obj.sub(4,2),2)
    #
    def test_mul(self):
        self.assertEqual(self.calc_obj.mul(2,2),4)
    #
    def test_div(self):
        self.assertEqual(self.calc_obj.div(4,2),2)

    def test_per(self):
        self.assertEqual(self.calc_obj.per(5,10), 50)

    # def test_dob(self):
    #     self.assertEqual(self.calc_obj.dob(6,98))

    def test_convert(self):
        self.assertEqual(self.calc_obj.convert(126),1.26)