import unittest
from LinkedQueue import LinkedQueue, Empty


class TestLinkedQueue(unittest.TestCase):

    def setUp(self):
        self.lq = LinkedQueue()
        self.lq.enqueue('A')
        self.lq.enqueue('B')

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.lq, LinkedQueue)

    def test_is_empty_method(self):
        print('Can check if the queue is empty')
        self.lq.dequeue()
        self.lq.dequeue()

        self.assertEqual(self.lq.is_empty(), True)
        self.assertNotEqual(len(self.lq), 1)

    def test_first_method(self):
        print('Can return the first element from the queue')
        self.lq.enqueue('C')
        self.lq.enqueue('D')
        self.assertEqual(self.lq.first(), 'A')

    def test_enqueue_method(self):
        print('Can add element to the end of the queue')
        self.lq.enqueue('E')
        self.lq.enqueue('F')
        self.assertEqual(len(self.lq), 4)

    def test_dequeue_method(self):
        print('Can remove element from the front of the queue')
        self.lq.dequeue()
        self.assertEqual(len(self.lq), 1)

    def test_exception_raising(self):
        self.lq.dequeue()
        with self.assertRaises(Empty):
            self.lq.dequeue()
            self.lq.first()


if __name__ == '__main__':
    unittest.main()
