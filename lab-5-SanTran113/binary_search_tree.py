from __future__ import annotations
from queue_array import Queue
from typing import Optional, Any, Tuple, List


class TreeNode:
    def __init__(self, key: Any, data: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, TreeNode):
            return (self.key == other.key
                    and self.data == other.data
                    and self.left == other.left
                    and self.right == other.right)
        else:
            return False

    def __repr__(self) -> str:
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))


class BinarySearchTree:
    def __init__(self, root_node: Optional[TreeNode] = None):  # Returns empty BST
        self.root: Optional[TreeNode] = root_node

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        if self.root is None:
          return True
        else:
          return False

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        # print(self.root.left)
        return self.search_helper(key, self.root)

    def search_helper(self, key, node) -> bool:
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
                return self.search_helper(key, node.left)
        elif key > node.key:
                return self.search_helper(key, node.right)

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = TreeNode(key, data)
    # On insert, can assume key not already in BST
    def insert(self, key: Any, data: Any = None) -> None:
        temp = TreeNode(key, data)
        node = self.root
        if node == None:
            self.root = temp
        else:
            return self.insert_helper(node, temp)
    def insert_helper(self, node, temp) -> None:
        if node is not None:
            if node.key == temp.key:
                node.data = temp.data
            if temp.key > node.key:
                if node.right is None:
                    node.right = temp
                else:
                    return self.insert_helper(node.right, temp)
            if temp.key < node.key:
                if node.left is None:
                    node.left = temp
                else:
                    return self.insert_helper(node.left, temp)


    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> Optional[Tuple[Any, Any]]:
        node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return (node.key, node.data)


    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> Optional[Tuple[Any, Any]]:
        node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return (node.key, node.data)

    #     if self.root is None:
    #         return None
    #     return self.find_max_helper(self.root)
    #
    # def find_max_helper(self, node):
    #     if node.right is None:
    #         return (self.root.key, self.root.data)
    #     return self.find_max_helper(node.right)

    # returns the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> Optional[int]:
        node = self.root
        if node is None:
            return None
        # heightL = 0
        # heightR = 0
        # heightL = self.tree_height_helper(node.left), heightL, heightR)
        # heightR = self.tree_height_helper(node.right, heightL, heightR)
        return self.tree_height_helper(self.root)
    def tree_height_helper(self, node) -> Optional[int]:
        if node.left is not None and node.right is not None:
            return 1 + max(self.tree_height_helper(node.left), self.tree_height_helper(node.right))
        elif node.left is not None and node.right is None:
            return 1 + self.tree_height_helper(node.left)
        elif node.left is None and node.right is not None:
            return 1 + self.tree_height_helper(node.right)
        else:
            return 0
        # if self.root is None:
        #     print("Base Case Ran")
        #     return None
        # print(self.data)
        #return self.tree_height_helper(self.root, heightL, heightR)

    # def tree_height_helper(self, node, heightL, heightR):
    #     print(f"L beg: {heightL}")
    #     print(f"R beg: {heightR}")
    #     # print(self.root.data)
    #     # if node is None:
    #
    #     if node is not None:
    #         print(f"L: {heightL}")
    #         heightL = self.tree_height_helper(node.left, heightL + 1, heightR)
    #     # else:
    #     #     heightL -= 1
    #     if node is not None:
    #         print(f"R: {heightR}")
    #         heightR = self.tree_height_helper(node.right, heightL, heightR + 1)
    #     # else:
    #     #     heightR -= 1
    #     print(f"L end: {heightL}")
    #     print(f"R end: {heightR}")
    #     return 1 + max(heightL, heightR)


    # returns Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        l: List[int] = []
        if self.root is None:
            return []
        return self.inorder_list_helper(self.root, l)
    def inorder_list_helper(self, node, l) -> List:
        if node is not None:
            self.inorder_list_helper(node.left, l)
            l.append(node.key)
            self.inorder_list_helper(node.right, l)
        return l
        # if node.left is not None:
        #     # print(f"left: {node.key}")
        #     self.inorder_list_helper(node.left, l)
        #     if node.left is None:
        #         # print(f"append left: {node.key}")
        #         l.append(node.key)
        # if node.right is not None:
        #     # print(f"right: {node.key}")
        #     l.append(node.key)
        #     self.inorder_list_helper(node.right, l)
        # else:
        #     # print(f"append left: {node.key}")
        #     l.append(node.key)
        # return l

    #     return
    #
    # def inorder_list_helper(self, node):
    #     if node.left is None:
    #         #process
    #     if node.right is None:
    #


    # returns Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        l: List[int] = []
        newL: List[int] = []
        if self.root is None:
            return []
        return self.preorder_list_helper(self.root, l, newL)
    def preorder_list_helper(self, node, l, newL) -> List:
        if node.left is not None:
            print(f"left: {node.key}")
            # print(f"left left key: {node.left.key}")
            l.append(node.key)
            self.preorder_list_helper(node.left, l, newL)
        else:
            l.append(node.key)
        if node.right is not None:
            print(f"right: {node.key}")
            l.append(node.key)
            self.preorder_list_helper(node.right, l, newL)
        else:
            l.append(node.key)

        for ele in l:
            if ele not in newL:
                newL.append(ele)
        return newL

    # returns Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        l = []
        node = self.root
        if node is None:
            return []
        q.enqueue(node)
        while q.is_empty() == False:
            node = q.dequeue()
            l.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return l