import unittest
from CircularQueue import CircularQueue, Empty


class TestCircularQueue(unittest.TestCase):

    def setUp(self):
        self.cq = CircularQueue()
        self.cq.enqueue('A')
        self.cq.enqueue('B')

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.cq, CircularQueue)

    def test_is_empty_method(self):
        print('Can check if the queue is empty')
        self.assertEqual(len(self.cq), 2)
        self.assertNotEqual(len(self.cq), 4)

    def test_first_method(self):
        print('Can return the first element from the front of the queue')
        self.assertEqual(self.cq.first(), 'A')

    def test_enqueue_method(self):
        print('Can add element to the back of the queue')
        self.cq.enqueue('C')
        self.assertEqual(len(self.cq), 3)

    def test_dequeue_method(self):
        print('Can remove element from the queue')
        self.cq.dequeue()
        self.cq.dequeue()
        self.assertEqual(self.cq.is_empty(), True)

    def test_rotate_method(self):
        print('Can rotate front element to the back of the queue')
        self.cq.rotate()
        self.assertEqual(self.cq.first(), 'B')

    def test_exception_raising(self):
        print('Can raise exception while performing actions on empty queue')
        self.cq.dequeue()
        self.cq.dequeue()
        with self.assertRaises(Empty):
            self.cq.first()
            self.cq.dequeue()


if __name__ == '__main__':
    unittest.main()
