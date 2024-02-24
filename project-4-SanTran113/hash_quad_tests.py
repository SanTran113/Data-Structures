import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self) -> None:
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self) -> None:
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_num_items(), 1)



    def test_02c(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [5, 17])
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", [10])
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", [12]) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

    #Num Items Tests
    def test_05a(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [8])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 1)

    def test_05b(self) -> None:
        # collision
        ht = HashTable(5)
        ht.insert("cat", [5])
        ht.insert("bird", [3])
        # ht.insert("dog", [8])
        self.assertEqual(ht.get_num_items(), 2)

    def test_05c(self) -> None:
        # testing rehashing
        ht = HashTable(5)
        ht.insert("cat", [5])
        ht.insert("dog", [8])
        ht.insert("bird", [3])
        self.assertEqual(ht.get_num_items(), 3)
        #[None, None, None, ['bird', [3]], None, None, ['dog', [8]], None, None, None, ['cat', [5]]]

    def test_05d(self) -> None:
        # testing rehashing w/ quadratic probing
        ht = HashTable(5)
        ht.insert("of", [1])
        ht.insert("off", [1])
        ht.insert("often", [1])
        ht.insert("on", [1])
        ht.insert("only", [1])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 5)

    def test_05e(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("cat", [5])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 1)

    def test_05f(self) -> None:
        ht = HashTable(7)
        ht.insert("cat", [1, 2, 3, 4, 5])
        ht.insert("cat", [8])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 1)

    def test_05g(self) -> None:
        ht = HashTable(7)
        ht.insert('Acts', [88])
        ht.insert('Acts', [164])
        ht.insert('Acts', [88, 164])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 1)

    # In Table Tests
    def test_06(self) -> None:
        # collision check
        ht = HashTable(5)
        ht.insert("cat", [5])
        ht.insert("bird", [3])
        print(ht.hash_table)
        self.assertEqual(ht.in_table("bird"), True)

    def test_06a(self) -> None:
        # with multiple items
        ht = HashTable(11)
        ht.insert("cat", [5])
        ht.insert("dog", [8])
        ht.insert("bird", [3])
        self.assertEqual(ht.in_table("dog"), True)

    # Get Index Tests
    def test_7(self) -> None:
        #collision
        ht = HashTable(5)
        ht.insert("cat", [5])
        ht.insert("bird", [3])
        self.assertEqual(ht.get_index("bird"), 3)

    # Get Value Tests
    def test_08(self) -> None:
        # collision
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("bird", [3])
        print(ht.hash_table)
        self.assertEqual(ht.get_value("bird"), [3])

    def test_08b(self) -> None:
        # collision then get item of the collided item
        ht = HashTable(7)
        ht.insert("cat", [5])
        ht.insert("dog", [3])
        ht.insert("birds", [3])
        print(ht.horner_hash('dog'))
        print(ht.horner_hash('birds'))
        print(ht.hash_table)
        self.assertEqual(ht.get_value("birds"), [3])

    # Sample Tests
    def test_09(self) -> None:
        ht = HashTable(7)
        ht.insert('', [123])
        ht.insert('a', [1])
        ht.insert('a', [5])
        ht.insert('a', [39])
        ht.insert('a', [44])
        ht.insert('a', [62])
        ht.insert('a', [69])
        ht.insert('a', [71])
        ht.insert('a', [80])
        ht.insert('a', [88])
        ht.insert('a', [104])
        ht.insert('a', [127])
        ht.insert('a', [137])
        ht.insert('a', [153])
        ht.insert('a', [154])
        ht.insert('a', [156])
        ht.insert('a', [159])
        ht.insert('a', [163])
        ht.insert('a', [164])
        ht.insert('a', [165])
        ht.insert('abdicated', [115])
        ht.insert('abolish', [21])
        ht.insert('abolish', [27])
        ht.insert('abolish', [103])
        ht.insert('abolish', [109])
        ht.insert('abolishing', [27])
        ht.insert('abolishing', [27])
        ht.insert('abolishing', [27])
        ht.insert('abolishing', [103])
        ht.insert('abolishing', [103])
        ht.insert('abolishing', [103])
        ht.insert('abolishing', [109])
        ht.insert('abolishing', [109])
        ht.insert('abolishing', [109])
        ht.insert('absolute', [30])
        ht.insert('absolute', [30])
        ht.insert('absolute', [30])
        ht.insert('absolute', [36])
        ht.insert('absolute', [36])
        ht.insert('absolute', [36])
        ht.insert('absolute', [107])
        ht.insert('absolute', [107])
        ht.insert('absolute', [107])
        ht.insert('absolved', [159])
        ht.insert('abuses', [28])
        ht.insert('accommodation', [47])
        ht.insert('accordingly', [26])
        ht.insert('accustomed', [28])
        ht.insert('acquiesce', [150])
        ht.insert('act', [36])
        ht.insert('act', [137])
        ht.insert('act', [138])
        ht.insert('act', [163])
        ht.insert('acts', [88])
        ht.insert('acts', [88])
        ht.insert('acts', [164])
        ht.insert('acts', [164])
        print(ht.hash_table)
        self.assertEqual(ht.get_num_items(), 14)
        # self.assertEqual(ht.get_index("bird"), 3)

if __name__ == '__main__':
   unittest.main()
