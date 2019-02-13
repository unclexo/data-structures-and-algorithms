import unittest
from Deque import Deque, Empty


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.d = Deque()

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.d, Deque)

    def test_add_first_method(self):
        print('Can add element(s) to the front of the deque')
        self.d.add_first(1)
        self.assertEqual(self.d.first(), 1)

    def test_add_last_method(self):
        print('Can add element(s) to the back of the deque')
        self.d.add_last(2)
        self.assertEqual(self.d.last(), 2)

    def test_remove_first_method(self):
        print('Can remove element(s) from the front of the deque')
        self.d.add_first('a')
        self.assertEqual(self.d.remove_first(), 'a')

    def test_remove_last_method(self):
        print('Can remove element(s) from the back of the deque')
        self.d.add_last('b')
        self.assertEqual(self.d.remove_last(), 'b')

    def test_is_empty_method(self):
        print('Can check if the deque is empty')
        self.assertEqual(self.d.is_empty(), True)

        self.d.add_first('hi')
        self.assertEqual(self.d.is_empty(), False)

    def test_length_checking(self):
        print('Can check the length of the deque')
        self.d.add_first('hmm')
        self.d.add_last('naa')
        self.assertEqual(len(self.d), 2)

        self.d.remove_last()
        self.assertEqual(len(self.d), 1)


if __name__ == '__main__':
    unittest.main()
