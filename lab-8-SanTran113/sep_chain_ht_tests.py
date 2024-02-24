import unittest
from sep_chain_ht import *


class TestList(unittest.TestCase):

    def test_insert1(self) -> None:
        hash1 = MyHashTable()
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.size(), 2)
        with self.assertRaises(ValueError):
            hash1.insert(-5, "c")

    def test_insert2(self) -> None:
        hash1 = MyHashTable()
        hash1.insert(11, "a")
        hash1.insert(6, "b")
        self.assertEqual(hash1.size(), 2)

    def test_get1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        self.assertEqual(hash1.get_item(3), 'b')
        self.assertEqual(hash1.get_item(11), 'a')

    def test_get2(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        with self.assertRaises(LookupError):
            hash1.get_item(6)

    def test_get3(self) -> None:
        # in lists of lists
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(6, "b")
        hash1.insert(21, "c")
        self.assertEqual(hash1.get_item(6), 'b')

    def test_get4(self) -> None:
        # with rehashing
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(11, "b")
        hash1.insert(11, "c")
        self.assertEqual(hash1.get_item(11), 'c')
        self.assertEqual(hash1.size(), 1)

    def test_get5(self) -> None:
        # with rehashing
        hash1 = MyHashTable(5)
        with self.assertRaises(LookupError):
            self.assertEqual(hash1.get_item(11), 'c')

    def test_remove1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        self.assertEqual(hash1.remove(11), (11, 'a'))
        self.assertEqual(hash1.size(), 0)

    def test_remove2(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(6, "b")
        self.assertEqual(hash1.remove(11), (11, 'a'))
        self.assertEqual(hash1.size(), 1)

    def test_remove3(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(6, "b")
        with self.assertRaises(LookupError):
            hash1.remove(5)

    def test_remove4(self) -> None:
        # check empty
        hash1 = MyHashTable(5)
        with self.assertRaises(LookupError):
            hash1.remove(5)

    def test_remove5(self) -> None:
        # check empty
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(11, "b")
        hash1.insert(11, "c")
        self.assertEqual(hash1.remove(11), (11, 'c'))
        self.assertEqual(hash1.size(), 0)

    def test_load_factor1(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.load_factor(), 1.4)

    def test_load_factor2(self) -> None:
        # with rehashing
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(6, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.load_factor(), 8 / 11)

    def test_collisions2(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        self.assertEqual(hash1.collisions(), 2)

    def test_collisions3(self) -> None:
        hash1 = MyHashTable(5)
        hash1.insert(11, "a")
        hash1.insert(3, "b")
        hash1.insert(1, "c")
        hash1.insert(8, "d")
        hash1.insert(4, "e")
        hash1.insert(5, "f")
        hash1.insert(1, "a")
        hash1.insert(1, "g")
        hash1.insert(2, "h")
        hash1.insert(0, "i")
        self.assertEqual(hash1.collisions(), 3)


if __name__ == '__main__':
    unittest.main()
