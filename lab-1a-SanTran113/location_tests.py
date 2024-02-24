# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!

    def test_eq_1(self) -> None:
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    def test_eq_2(self) -> None:
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = None
        self.assertNotEqual(loc1, loc2)

    def test_eq_3(self) -> None:
        loc1 = Location('SLO', 35.3, -120.7)
        loc2 = Location('13', 13, 13)
        self.assertFalse(loc1 == loc2, False)

    def test_init(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc, Location('SLO', 35.3, -120.7))

if __name__ == "__main__":
        unittest.main()
