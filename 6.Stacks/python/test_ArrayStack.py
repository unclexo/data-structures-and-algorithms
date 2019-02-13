import unittest
from ArrayStack import ArrayStack, Empty


class TestArrayStack(unittest.TestCase):

    def setUp(self):
        self.s = ArrayStack()
        self.s.push(1)
        self.s.push(2)

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.s, ArrayStack)

    def test_is_empty_method(self):
        print('Can check if the stack is empty')
        self.s.pop()
        self.s.pop()
        self.assertEqual(self.s.is_empty(), True)

    def test_push_method(self):
        print('Can add element to the top of the stack')
        self.s.push(5)

        self.assertEqual(self.s.top(), 5)

    def test_pop_method(self):
        print('Can remove element(s) from the top of the stack')

        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.top(), 1)

    def test_length_checking(self):
        print('Can check the length of the stack')
        self.assertEqual(len(self.s), 2)

    def test_exception_raising(self):
        print('Can raise exception while performing action(s) on empty stack')
        self.s.pop()
        self.s.pop()

        with self.assertRaises(Empty):
            self.s.top()
            self.s.pop()


if __name__ == '__main__':
    unittest.main()
