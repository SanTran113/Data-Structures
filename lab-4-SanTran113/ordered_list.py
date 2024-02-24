from __future__ import annotations
from typing import Optional, Any, List


class Node:
    """Node for use with doubly-linked list"""

    def __init__(self, item: Any):
        self.item = item  # item held by Node
        self.next: Node = self  # reference to next Node, init to this Node
        self.prev: Node = self  # reference to previous Node, init to this Node


class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""

    def __init__(self) -> None:
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel: Node = Node(None)  # Empty linked list, just sentinel Node
        self.sentinel.next = self.sentinel  # Initialize next to sentinel
        self.sentinel.prev = self.sentinel  # Initialize prev to sentinel

    def __eq__(self, other: object) -> bool:
        lists_equal = True
        if not isinstance(other, OrderedList):
            lists_equal = False
        else:
            s_cur = self.sentinel.next
            o_cur = other.sentinel.next
            while s_cur != self.sentinel and o_cur != other.sentinel:
                if s_cur.item != o_cur.item:
                    lists_equal = False
                s_cur = s_cur.next
                o_cur = o_cur.next
            if s_cur != self.sentinel or o_cur != other.sentinel:
                lists_equal = False
        return lists_equal

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        if self.sentinel.next == self.sentinel:
            # if self.sentinel.next == self.sentinel.item and self.sentinel.next == self.sentinel.prev:
            return True
        else:
            return False

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        current = self.sentinel.next
        while current is not self.sentinel and item > current.item:
            current = current.next
        if item != current.item:
            temp = Node(item)
            temp.next = current
            temp.prev = current.prev
            current.prev.next = temp
            current.prev = temp
        # newNode = Node(item)
        # if self.sentinel.item is None:
        #     self.sentinel = newNode
        # elif newNode.item < self.sentinel.item:
        #     newNode.next = self.sentinel
        #     newNode.prev = self.sentinel.prev
        #     newNode.prev.next = newNode
        #     self.sentinel.prev = newNode
        # elif newNode.item > self.sentinel.item:
        #     self.sentinel = self.sentinel.next
        # elif newNode.item == self.sentinel.item:
        #     self.sentinel = newNode

    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        # if self.sentinel.next == self.sentinel and self.sentinel.prev == self.sentinel:
        # print(f"item: {item}")
        # print(f" Python List:{self.python_list()}")
        # if item in self.python_list():
        #     # print(self.remove(item))
        #     x = self.index(item)
        #     self.python_list().pop(x)
        #     # print(f" Python List After:{self.python_list()}")
        #     return True
        # else:
        #     return False
        current = self.sentinel.next
        # current = current.next
        return self.remove_helper(item, current)

    def remove_helper(self, item: Any, current: Any) -> bool:
        if current is self.sentinel:
            return False
        # print(f"cur Item: {current.item}")
        elif current.item == item:
            current.prev.next = current.next
            current.next.prev = current.prev
            return True
        return self.remove_helper(item, current.next)

        # cur = self.sentinel.next
        # # while cur is not self.sentinel and item > cur.item:
        # #     cur = cur.next
        # cur.prev.next = cur.next
        # cur.next.prev = cur.prev
        # if cur.prev == cur.prev.next:
        #     return True
        # else:
        #     return False
        # self.sentinel.prev.next = self.sentinel.next
        # self.sentinel.next.prev = self.sentinel.prev
        # if item in self.sentinel.item:
        #     return True
        # else:
        #     return False

    def index(self, item: Any) -> Optional[int]:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        count = 0
        cur = self.sentinel.next
        while cur is not self.sentinel:
            if item is cur.item:
                return count
            else:
                count += 1
            cur = cur.next
        return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        count = 0
        cur = self.sentinel.next
        return self.pop_helper(index, cur, count)

    def pop_helper(self, index: int, cur: Any, count: int) -> Any:
        if index < 0 or index >= self.size():
            raise IndexError
        elif count == index:
            # cur = self.sentinel.next
            IndexItem = cur.item
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            return IndexItem
        return self.pop_helper(index, cur.next, count + 1)
        # if current == self.sentinel:
        #     return False
        # else:
        #     while current != self.sentinel:
        #         # print(f"cur Item: {current.item}")
        #         if current.item == item:
        #             return True
        #         else:
        #             current = current.next

        # elif count != index:
        # while cur != self.sentinel and count != index:
        #     # print(self.sentinel.item)
        #     # print(self.sentinel.item)
        #     # if cur != self.sentinel:
        #     if count == index:
        #     # cur = self.sentinel.next
        #         IndexItem = cur.item
        #         cur.prev.next = cur.next
        #         cur.next.prev = cur.prev
        #         return IndexItem
        #     count += 1
        #     cur = cur.next
        # return cur.item

    def search(self, item: Any) -> bool:
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""

        # return self.search_helper(item, current)
        # print(f"Item: {item}")
        # print(f"Cur Index Item: {self.index(current.item)}")
        # print(f"Size: {self.size()}")
        # print(self.sentinel.next.item)
        current = self.sentinel.next
        # current = current.next
        return self.search_helper(item, current)

    def search_helper(self, item: Any, current: Any) -> bool:
        if current is self.sentinel:
            return False
        # print(f"cur Item: {current.item}")
        elif current.item == item:
            return True
        return self.search_helper(item, current.next)

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        py_list: List[int] = []
        current = self.sentinel.next
        while current is not self.sentinel:
            py_list.append(current.item)
            current = current.next
        return py_list
        # l = []
        # for _ in self.sentinel.item:
        #     l.append(self.sentinel.item)
        #     self.sentinel = self.sentinel.next
        # return l

    def python_list_reversed(self) -> List:
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        py_list: List[int] = []
        revList: List[int]
        self.python_list_reversed_helper(self.sentinel.next, py_list)
        revList = list(reversed(py_list))
        return revList

    def python_list_reversed_helper(self, node: Node, py_list: List) -> None:
        if node is not self.sentinel:
            py_list.append(node.item)
            return self.python_list_reversed_helper(node.next, py_list)

    def size(self) -> int:
        """Returns number of items in the OrderedList - USE RECURSION"""
        count = 0
        return self.size_helper(self.sentinel, count)

    def size_helper(self, node: Node, count: int) -> Any:
        if node.next is self.sentinel:
            return count
        elif node.next is not self.sentinel:
            return self.size_helper(node.next, count + 1)
