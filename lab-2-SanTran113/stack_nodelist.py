from __future__ import annotations
from typing import Optional, Any

# Node list is one of
# None or
# Node(value, rest), where rest is reference to the rest of the list
class Node:
    def __init__(self, value: Any, rest: Optional[Node]):
        self.value = value      # object reference stored in Node
        self.rest = rest        # reference to Node list

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Node):
            return (self.value == other.value
                    and self.rest == other.rest)
        else:
            return False

    def __repr__(self) -> str:
        return ("Node({!r}, {!r})".format(self.value, self.rest))

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a node list"""

    # top is the top Node of stack
    def __init__(self, top: Optional[Node] = None):
        self.top = top              # top node of stack
        self.num_items = 0          # number of items in stack
        node = top                  # set number of items based on input
        while node is not None:
            self.num_items += 1
            node = node.rest

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Stack):
            return (self.top == other.top)
        else:
            return False

    def __repr__(self) -> str:
        return ("Stack({!r})".format(self.top))

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance"""
        if self.num_items == 0:
            return True
        else:
            print(self.top)
            print(self.num_items)
            return False

    def push(self, item: Any) -> None:
        """Pushes item on stack.
           MUST have O(1) performance"""
        # if self.num_items == 0:
        #     self.top = Node(item, self.top)
        if self.num_items != 0:
            temp = Node(item, self.top)
            self.top = temp
        self.num_items = self.num_items + 1
        # print(self.items)


    def pop(self) -> Any:
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance"""
        if self.num_items == 0 or self.top is None:
            raise IndexError
        if self.num_items != 0:
            item = self.top.value
            self.top = self.top.rest
            return item

    def peek(self) -> Any:
        """If stack is not empty, returns next item to be popped (but does not remove the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance"""
        if self.num_items == 0:
            raise IndexError
        if self.num_items != 0:
            if self.top is not None:
                return self.top.value

    # Check if 'hi' is the return value or Node(hi, None)

    def size(self) -> int:
        """Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance"""
        return self.num_items