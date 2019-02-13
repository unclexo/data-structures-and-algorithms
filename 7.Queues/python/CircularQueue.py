class CircularQueue:
    """ Queue implementation using Circular Linked List for storage """

    class _Node:
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node=None):
            """ Creates a node object """
            self.element = element
            self.next = next_node

    def __init__(self):
        """ Creates an empty queue """
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Returns true if the queue is empty """
        return self._size == 0

    def first(self):
        """ Returns (but do not remove) the element at the front of the queue

        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail.next
        return head.element

    def enqueue(self, element):
        """ Add an element to the back of the queue """
        new_node = self._Node(element)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._tail.next
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """ Removes and returns the first element of the queue

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        old_head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next
        self._size -= 1
        return old_head.element

    def rotate(self):
        """ Rotates front element to the back of the queue """
        if self._size > 0:
            self._tail = self._tail.next


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass


