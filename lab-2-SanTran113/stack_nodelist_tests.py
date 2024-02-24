import unittest

import stack_nodelist
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty_01(self) -> None:
        s = stack_nodelist.Stack()
        self.assertTrue(Stack.is_empty(s))

    def test_is_empty_02(self) -> None:
        s = stack_nodelist.Stack(Node('hi', None))
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_03(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node('bunny', None)))
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_04(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node(None, None)))
        self.assertFalse(Stack.is_empty(s))


    def test_push_01(self) -> None:
        s = stack_nodelist.Stack()
        Stack.push(s, Node('bunny', None))
        self.assertEqual(Stack.size(s), 1)

    def test_push_02(self) -> None:
        s = stack_nodelist.Stack(Node('bunny', None))
        Stack.push(s, Node('hi', None))
        self.assertEqual(Stack.size(s), 2)

    def test_pop_01(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node('hello', Node('hey', None))))
        self.assertEqual(Stack.pop(s), 'hi')

    def test_pop_02(self) -> None:
        with self.assertRaises(IndexError):
            s = stack_nodelist.Stack()
            self.assertEqual(Stack.pop(s), Node('hey', None))

    def test_peek_01(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node('hello', Node('hey', None))))
        self.assertEqual(Stack.peek(s), 'hi')

    def test_peek_02(self) -> None:
        with self.assertRaises(IndexError):
            s = stack_nodelist.Stack()
            self.assertEqual(Stack.peek(s), 0)

    def test_size_01(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node('hello', Node('hey', None))))
        self.assertEqual(Stack.size(s), 3)

    def test_size_02(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node(None, Node('bunny', None))))
        self.assertEqual(Stack.size(s), 3)

    def test_size_03(self) -> None:
        s = stack_nodelist.Stack()
        self.assertEqual(Stack.size(s), 0)

    def test_size_04(self) -> None:
        s = stack_nodelist.Stack(Node('hi', None))
        self.assertEqual(Stack.size(s), 1)

    def test_size_05(self) -> None:
        s = stack_nodelist.Stack(Node(None, None))
        self.assertEqual(Stack.size(s), 1)

    def test_size_06(self) -> None:
        s = stack_nodelist.Stack(Node('hi', Node(None, None)))
        self.assertEqual(Stack.size(s), 2)

if __name__ == '__main__': 
    unittest.main()
