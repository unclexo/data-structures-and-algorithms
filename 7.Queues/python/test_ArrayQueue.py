import unittest
from ArrayQueue import ArrayQueue, Empty


class TestArrayQueue(unittest.TestCase):

    def setUp(self):
        self.q = ArrayQueue()
        self.q.enqueue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.q, ArrayQueue)

    def test_length_checking(self):
        print('Can check the length of the queue')
        self.assertEqual(len(self.q), 3)

    def test_first_method(self):
        print('Can return the first element of the queue')
        self.assertEqual(self.q.first(), 1)

    def test_enqueue_method(self):
        print('Can add elements to the queue')

        self.q.enqueue(4)
        self.q.enqueue(5)

        self.assertEqual(len(self.q), 5)
        self.assertEqual(self.q.first(), 1)

    def test_dequeue_method(self):
        print('Can remove elements from the front of the queue')

        self.q.enqueue(4)
        self.q.enqueue(5)

        self.q.dequeue()
        self.assertEqual(self.q.dequeue(), 2)

        self.assertEqual(len(self.q), 3)
        self.assertEqual(self.q.first(), 3)

    def test_is_empty_method(self):
        print('Can check if the queue is empty')

        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()

        self.assertEqual(self.q.is_empty(), True)

    def test_exception_raising(self):
        print('Can raise exception while performing action(s) on an empty queue')

        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()

        with self.assertRaises(Empty):
            self.q.first()
            self.q.dequeue()


if __name__ == '__main__':
    unittest.main()
