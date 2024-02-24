import unittest
from binary_search_tree import *
import random

class TestLab4(unittest.TestCase):

    def test_00(self) -> None:
        tn1 = TreeNode(1, None)
        tn2 = TreeNode(1, None)
        self.assertFalse(tn1.__eq__(None))
        self.assertEqual(tn1, tn2)
        self.assertEqual(tn1.__repr__(),"TreeNode(1, None, None, None)")

    def test_01_simple(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())

    def test_02_insert_search(self) -> None:
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)

        for val in values:
            self.assertTrue(bst.search(val))
            self.assertFalse(bst.search(val - 1))
            self.assertFalse(bst.search(val + 1))

    def test_02_insert_search_02(self) -> None:
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)

        self.assertTrue(bst.search(99))
        self.assertTrue(bst.search(-4))
        self.assertTrue(bst.search(167))
        self.assertTrue(bst.search(139))
        self.assertTrue(bst.search(55))
        self.assertTrue(bst.search(-89))
        self.assertTrue(bst.search(13))
        self.assertTrue(bst.search(78))
        self.assertTrue(bst.search(128))
        self.assertTrue(bst.search(119))


    def test_03_search_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertFalse(bst.search(999))

    def test_04_pre_in_level_order_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
                
    def test_07_test_min_max_empty(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(None, bst.find_max())
        self.assertEqual(None, bst.find_min())

    def test_08_test_inorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.inorder_list(), [-89, -4, 13, 55, 78, 99, 139, 167, 174, 178])

    def test_09_test_preorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.preorder_list(), [99, -4, -89, 55, 13, 78, 167, 139, 178, 174])

    def test_09_test_level_order(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.level_order_list(), [99, -4, 167, -89, 55, 139, 178, 13, 78, 174])
        
    def test_14_insert_replace(self) -> None:
        bst = BinarySearchTree()
        bst.insert(30, 'aaa')
        bst.insert(40, 'bbb')
        bst.insert(35, 'ccc')
        bst.insert(50, 'ddd')
        bst.insert(60, 'eee')
        bst.insert(60, 'zzz')
        self.assertEqual(bst.find_max(), (60, 'zzz'))
        self.assertEqual(bst.tree_height(), 3)

    def test_16_test_tree_height(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
        # print(bst.root.key)
        for i in range(len(keys)):
            bst.insert(keys[i])
            print(bst.root)

        # print(bst.insert(keys[i]))
        self.assertEqual(bst.tree_height(), 3)

    def test_height(self) -> None:
        bst = BinarySearchTree()
        bst.root = TreeNode(6, None)
        leftNode = TreeNode(5, None, TreeNode(3, "hi"))
        rightNode = TreeNode(9, None, None, TreeNode(12, "bye"))
        bst.root.left = leftNode
        bst.root.right = rightNode
        self.assertEqual(bst.tree_height(), 2)

    def test_09_test_preorder_02(self) -> None:
        bst = BinarySearchTree()
        keys = [20, 25, 23, 10, 21, 5, 24, 8]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.preorder_list(), [20, 10, 5, 8, 25, 23, 21, 24])

    def test_empty_02(self) -> None:
        bst = BinarySearchTree()
        bst.root = TreeNode(6, None)
        leftNode = TreeNode(5, None, TreeNode(3, "hi"))
        rightNode = TreeNode(9, None, None, TreeNode(12, "bye"))
        bst.root.left = leftNode
        bst.root.right = rightNode
        self.assertFalse(bst.is_empty())

    def test_min_01(self) -> None:
        bst = BinarySearchTree()
        bst.root = TreeNode(6, None)
        leftNode = TreeNode(5, None, TreeNode(3, "hi"))
        rightNode = TreeNode(9, None, None, TreeNode(12, "bye"))
        bst.root.left = leftNode
        bst.root.right = rightNode
        self.assertEqual((3, "hi"), bst.find_min())

    def test_max_01(self) -> None:
        bst = BinarySearchTree()
        keys = [20, 25, 23, 10, 21, 5, 24, 8]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual((5, None), bst.find_min())

    def test_max_01(self) -> None:
        bst = BinarySearchTree()
        keys = [20, 25, 23, 10, 21, 5, 24, 8]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual((25, None), bst.find_max())

    def test_max_02(self) -> None:
        bst = BinarySearchTree()
        keys = [20, 25, 23, 10, 25, 25, 24, 8]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual((25, None), bst.find_max())

    def test_max_03(self) -> None:
        bst = BinarySearchTree()
        keys = [25, 25, 25]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual((25, None), bst.find_max())

if __name__ == '__main__': 
    unittest.main()
