import unittest
from LinkedStack import LinkedStack, Empty


class TestLinkedStack(unittest.TestCase):

    def setUp(self):
        self.ls = LinkedStack()

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.ls, LinkedStack)

    def test_is_empty_method(self):
        print('Can check if the stack is empty')
        self.assertEqual(self.ls.is_empty(), True)

    def test_top_method(self):
        print('Can return the top element from the stack')
        self.ls.push('A')
        self.ls.push('B')
        self.assertEqual(self.ls.top(), 'B')

    def test_push_method(self):
        print('Can adds element(s) to the stack')
        self.ls.push('A')
        self.ls.push('B')
        self.ls.push('C')
        self.assertEqual(len(self.ls), 3)

    def test_pop_method(self):
        print('Can prove LIFO order')
        self.ls.push('A')
        self.ls.push('B')
        self.ls.push('C')

        self.assertEqual(self.ls.pop(), 'C')
        self.assertEqual(self.ls.pop(), 'B')

    def test_length_checking(self):
        print('Can check the length of the stack')
        self.ls.push('A')
        self.ls.push('B')
        self.assertEqual(len(self.ls), 2)
        self.assertNotEqual(len(self.ls), 3)

    def test_exception_raising(self):
        print('Can raise exception while performing action(s) on empty stack')
        with self.assertRaises(Empty):
            self.ls.top()
            self.ls.pop()


if __name__ == '__main__':
    unittest.main()
