import unittest
from queue_nodelist import *

class TestLab1(unittest.TestCase):

    def test_nodelist(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, None)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.front, None)
        q.enqueue(2)
        print(f"rear tst: {q.rear}")
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.dequeue(),1)
        print(f"why: {q.front}")
        print(f"rear tst: {q.rear}")
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, Node(2, None))
        self.assertFalse(Node(1,None).__eq__(None))

    def test_repr(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.__repr__(), "Queue(Node(1, None), None)")

    def test_eq(self) -> None:
        q1 = Queue()
        q1.enqueue(1)
        q1.enqueue(2)
        q2 = Queue()
        q2.enqueue(1)
        q2.enqueue(2)
        self.assertEqual(q1, q2)
        self.assertFalse(q1.__eq__(None))
        q1.dequeue()
        q2.dequeue()
        self.assertEqual(q1, q2)

    def test_queue_simple(self) -> None:
        q = Queue()
        print(f"q0: {q}")
        q.enqueue(1)
        print(f"q1: {q}")
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        print(f"q2: {q}")
        print(f"rear: {q.rear}")
        print(f"front: {q.front}")
        # print(q.rear.value)
        q.enqueue(3)
        print(f"q3: {q}")
        q.enqueue(4)
        print(f"q4: {q}")
        q.enqueue(5)

        print(f"q5: {q}")
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        print(f"q1: {q.front}")
        self.assertEqual(q.dequeue(), 2)
        print(f"q2: {q}")
        self.assertEqual(q.dequeue(), 3)
        print(f"q3: {q}")
        self.assertEqual(q.dequeue(), 4)
        print(f"q4: {q}")
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)

    def test_enqueue_01(self) -> None:
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.size(), 1)

    def test_size_01(self) -> None:
        q = Queue(Node(1, None))

        self.assertEqual(q.size(), 1)

    def test_dequeue_01(self) -> None:
        q = Queue(Node(5, Node(4, Node(3, Node(2,  Node(1, None))))))
        self.assertEqual(q.dequeue(), 1)

    def test_dequeue_02(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(None, None)
            self.assertEqual(q.dequeue(), 1)

    def test_is_empty_01(self) -> None:
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_is_empty_02(self) -> None:
        q = Queue(Node(5, Node(4, Node(3, Node(2, Node(1, None))))), None, 5)
        self.assertFalse(q.is_empty())

    def test_is_empty_03(self) -> None:
        q = Queue(Node(5, Node(4, Node(3, Node(2, Node(1, None))))))
        self.assertFalse(q.is_empty())

if __name__ == '__main__': 
    unittest.main()
