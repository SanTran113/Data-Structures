import unittest
from stack_array import Stack
import stack_array

class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty_01(self) -> None:
        s = stack_array.Stack(0, [])
        self.assertTrue(Stack.is_empty(s))

    def test_is_empty_02(self) -> None:
        s = stack_array.Stack(4, [1, 2, 3, 4])
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_03(self) -> None:
        s = stack_array.Stack(1, [None])
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_04(self) -> None:
        s = stack_array.Stack(4, [34])
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_05(self) -> None:
        s = stack_array.Stack(10, [1, 2, 3, 4])
        self.assertFalse(Stack.is_empty(s))

    def test_is_empty_06(self) -> None:
        s = stack_array.Stack(10, [1, None, 3, 4])
        self.assertFalse(Stack.is_empty(s))

    def test_is_full_01(self) -> None:
        s = stack_array.Stack(10, [1, None, 3, 4])
        self.assertFalse(Stack.is_full(s))

    def test_is_full_02(self) -> None:
        s = stack_array.Stack(4, [1, None, 3, 4])
        self.assertTrue(Stack.is_full(s))

    def test_push_02(self) -> None:
        with self.assertRaises(IndexError):
            s = stack_array.Stack(5, [1, 2, 3, 4, 5])
            self.assertEqual(Stack.push(s, 5), Stack(5, [1, 2, 3, 4, 5]))

    def test_pop_01(self) -> None:
        s = stack_array.Stack(5, [1, 2, 3, 4])
        self.assertEqual(Stack.pop(s), 4)

    def test_pop_02(self) -> None:
        with self.assertRaises(IndexError):
            s = stack_array.Stack(5, [])
            self.assertEqual(Stack.pop(s), Stack(5, []))

    def test_pop_03(self) -> None:
        s = stack_array.Stack(10, [1, 2, 3, 8, None])
        self.assertEqual(Stack.pop(s), None)

    def test_pop_04(self) -> None:
        s = stack_array.Stack(10, [2])
        self.assertEqual(Stack.pop(s), 2)

    def test_pop_05(self) -> None:
        s = stack_array.Stack(10, [1, 5])
        self.assertEqual(Stack.pop(s), 5)

    def test_pop_06(self) -> None:
        s = stack_array.Stack(4, [1, 2, 3, 4])
        self.assertEqual(Stack.pop(s), 4)

    def test_peek_01(self) -> None:
        s = stack_array.Stack(5, [1, 2, 3, 8])
        self.assertEqual(Stack.peek(s), 8)

    def test_peek_02(self) -> None:
        with self.assertRaises(IndexError):
            s = stack_array.Stack(5, [])
            self.assertEqual(Stack.peek(s), 0)

    def test_size_01(self) -> None:
        s = stack_array.Stack(4, [1, 2, 3, 8])
        self.assertEqual(Stack.size(s), 4)

    def test_size_02(self) -> None:
        s = stack_array.Stack(12, [1, 2, 3, 8])
        self.assertEqual(Stack.size(s), 4)

    def test_size_03(self) -> None:
        s = stack_array.Stack(12, None)
        self.assertEqual(Stack.size(s), 0)

    def test_size_04(self) -> None:
        s = stack_array.Stack(12, [38])
        self.assertEqual(Stack.size(s), 1)

    def test_size_05(self) -> None:
        s = stack_array.Stack(12, [1, None, 2, 3])
        self.assertEqual(Stack.size(s), 4)

if __name__ == '__main__':
    unittest.main()
