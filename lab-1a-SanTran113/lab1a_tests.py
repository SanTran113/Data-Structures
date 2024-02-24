# CPE 202 Lab 1 Test Cases

import unittest
from lab1a import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        """ Tests for a value in a list"""
        tlist = [1,2,3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_02(self) -> None:
        """ Tests that ValueError is raised with the list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_03(self) -> None:
        """ Tests that it returns None when the given list is empty"""
        tlist: List[float] = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse(self) -> None:
        """ Tests that lists reverse"""
        intlist: List[int] = [1,2,3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])

    def test_reverse_2(self) -> None:
        """ Tests that ValueError is raised when the inital list is None"""
        intlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list(intlist)

    def test_reverse_mutate(self) -> None:
        """Tests that the list reverses normally"""
        intlist = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])

    def test_reverse_mutate2(self) -> None:
        """Tests that empty list returns an empty list"""
        intlist: List[int] = []
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [])

    def test_reverse_mutate3(self) -> None:
        """Tests that ValueError is raised when inital list is None"""
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(intlist)

if __name__ == "__main__":
        unittest.main()