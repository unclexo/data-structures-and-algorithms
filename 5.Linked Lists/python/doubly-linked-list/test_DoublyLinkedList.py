import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = DoublyLinkedList()

    def test_create_instance(self):
        print('Can create an instance')
        self.assertIsInstance(self.list, DoublyLinkedList)

    def test_check_properties(self):
        print('Can check the existence of properties')
        self.assertEqual(self.list.head, None)
        self.assertEqual(self.list.tail, None)
        self.assertEqual(self.list.size, 0)

    def test_check_emptiness(self):
        print('Can check if the linked list is empty')
        self.assertEqual(self.list.empty, True)

    def test_add_node_to_the_front(self):
        print('Can add node to the front of the linked list')
        self.list.addFront(3)
        self.list.addFront(2)
        self.list.addFront(1)

        self.assertEqual(self.list.size, 3)
        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(self.list.head.next.data, 2)
        self.assertEqual(self.list.head.next.prev.data, 1)
        self.assertEqual(self.list.head.next.next.data, 3)

    def test_add_node_to_the_back(self):
        print('Can add node to the back of the linked list')
        self.list.addBack(4)
        self.list.addBack(5)
        self.list.addBack(6)

        self.assertEqual(self.list.size, 3)
        self.assertEqual(self.list.tail.data, 6)
        self.assertEqual(self.list.tail.next, None)
        self.assertEqual(self.list.tail.prev.data, 5)
        self.assertEqual(self.list.tail.prev.prev.data, 4)

    def test_remove_node_from_the_front(self):
        print('Can remove node from the front of the linked list')
        self.list.addFront(3)
        self.list.addFront(2)
        self.list.addFront(1)

        self.assertEqual(self.list.head.data, 1)
        self.assertEqual(self.list.head.prev, None)

        self.list.removeFront()

        self.assertEqual(self.list.head.data, 2)
        self.assertEqual(self.list.head.prev, None)
        self.assertEqual(self.list.head.next.data, 3)

    def test_remove_node_from_the_back(self):
        print('Can remove node from the back of the linked list')
        self.list.addBack(1)
        self.list.addBack(2)
        self.list.addBack(3)

        self.assertEqual(self.list.tail.data, 3)
        self.assertEqual(self.list.tail.next, None)

        self.list.removeBack()

        self.assertEqual(self.list.tail.data, 2)
        self.assertEqual(self.list.tail.next, None)
        self.assertEqual(self.list.tail.prev.data, 1)

    def test_remove_node_from_the_list(self):
        print('Can remove a node from the list')
        self.list.addFront(3)
        self.list.addFront(2)
        self.list.addFront(1)

        self.list.addBack(4)
        self.list.addBack(5)
        self.list.addBack(6)

        self.list.remove(4)
        self.list.remove(3)

        self.assertEqual(self.list.size, 4)

        # 1, 2, 5, 6
        self.assertEqual(self.list.head.next.next.data, 5)
        self.assertEqual(self.list.head.next.next.prev.data, 2)

    def test_find_node_in_the_list(self):
        print('Can find a node in the list')
        self.list.addFront(3)
        self.list.addFront(2)
        self.list.addFront(1)

        self.list.addBack(4)
        self.list.addBack(5)
        self.list.addBack(6)

        self.list.find(3)
        self.list.find(5)
        self.assertEqual(self.list.find(8), None)

    def test_insert_node_in_the_list(self):
        print('Can insert a node in the list')

        self.list.addFront(5)
        self.list.addFront(3)
        self.list.addFront(2)
        self.list.addFront(1)

        self.list.insert(4, 3)

        self.assertEqual(self.list.size, 5)

        # 1, 2, 3, 4, 5
        self.assertEqual(self.list.tail.prev.data, 4)
        self.assertEqual(self.list.head.next.next.next.next.prev.prev.data, 3)


if __name__ == '__main__':
    unittest.main()
