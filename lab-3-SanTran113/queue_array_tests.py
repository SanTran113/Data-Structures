import unittest

import queue_array
from queue_array import Queue

class TestLab1(unittest.TestCase):

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        print(q)
        print(f"front: {q.front}")
        print(f"rear: {q.rear}")
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)


    def test_dequeue_01(self) -> None:
        q: Queue = Queue(4, [1, 2, 8, 10])
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.size(), 2)


    def test_dequeue_02(self) -> None:
        q: Queue = Queue(6, [1, 2, 8, 10])
        self.assertEqual(q.dequeue(), 1)

    def test_dequeue_03(self) -> None:
        with self.assertRaises(IndexError):
            q: Queue = Queue(10, [])
            self.assertEqual(q.dequeue(), 1)

    def test_dequeue_04(self) -> None:
        with self.assertRaises(IndexError):
            q: Queue = Queue(0, [])
            self.assertEqual(q.dequeue(), 1)

    def test_enqueue_01(self) -> None:
        q: Queue = Queue(6, [5, 2, 8, 10])
        q.enqueue(20)
        self.assertEqual(q.size(), 5)

    def test_enqueue_02(self) -> None:
        with self.assertRaises(IndexError):
            q: Queue = Queue(4, [5, 2, 8, 10])
            q.enqueue(20)
            # self.assertEqual(q.size(), 5)

    def test_is_empty_01(self) -> None:
        q = Queue(6, [])
        self.assertTrue(q.is_empty())

    def test_is_empty_02(self) -> None:
        q = Queue(0, [])
        self.assertTrue(q)

    def test_is_empty_03(self) -> None:
        q = Queue(4, [1, 2, 3, 4])
        self.assertFalse(q.is_empty())

    def test_is_full_01(self) -> None:
        q = Queue(4, [1, 2, 3, 4])
        self.assertTrue(q.is_full())

    def test_is_full_02(self) -> None:
        q = Queue(4, [1, 4])
        self.assertFalse(q.is_full())

    def test_is_full_03(self) -> None:
        q = Queue(4, [])
        self.assertFalse(q.is_full())

if __name__ == '__main__': 
    unittest.main()
