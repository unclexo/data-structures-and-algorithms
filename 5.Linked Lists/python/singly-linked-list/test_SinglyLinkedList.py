import unittest
from SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.sll = SinglyLinkedList()

    def test_instantiation(self):
        print('Can create an instance')
        self.assertIsInstance(self.sll, SinglyLinkedList)

    def test_is_empty_method(self):
        print('Can check if the list is empty')
        self.assertEqual(self.sll.is_empty(), True)

    def test_add_front_method(self):
        print('Can add element to the front of the list')
        self.sll.add_front('A')
        self.sll.add_front('B')
        self.sll.add_front('C')
        self.assertEqual(len(self.sll), 3)

    def test_add_last_method(self):
        print('Can add element to the end of the list')
        self.sll.add_last('A')
        self.sll.add_last('B')
        self.sll.add_last('C')
        self.assertEqual(len(self.sll), 3)

if __name__ == '__main__':
    unittest.main()
