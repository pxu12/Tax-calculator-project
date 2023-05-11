from tax import *
import unittest

class TestResults(unittest.TestCase):
    def test_1(self):
        OR = OldRegime(2220)
        self.assertEqual(round(OR.calculate_tax()), 56 , "incorrect old tax")

        NR = NewRegime(2220)
        self.assertEqual(round(NR.calculate_tax()), 0 , "incorrect new tax")

    def test_2(self):
        OR = OldRegime(3250)
        self.assertEqual(round(OR.calculate_tax()), 86 , "incorrect old tax")

        NR = NewRegime(3250)
        self.assertEqual(round(NR.calculate_tax()), 2 , "incorrect new tax")

    def test_3(self):
        OR = OldRegime(7000)
        self.assertEqual(round(OR.calculate_tax()), 228 , "incorrect old tax")

        NR = NewRegime(7000)
        self.assertEqual(round(NR.calculate_tax()), 114 , "incorrect new tax")

    def test_4(self):
        OR = OldRegime(10000)
        self.assertEqual(round(OR.calculate_tax()), 389 , "incorrect old tax")

        NR = NewRegime(10000)
        self.assertEqual(round(NR.calculate_tax()), 204 , "incorrect new tax")

    def test_5(self):
        OR = OldRegime(18000)
        self.assertEqual(round(OR.calculate_tax()), 938 , "incorrect old tax")

        NR = NewRegime(18000)
        self.assertEqual(round(NR.calculate_tax()), 513 , "incorrect new tax")


