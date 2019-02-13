class LinkedQueue:
    """ FIFO Queue implementation using Singly Linked List for storage """

    class _Node:
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            """ Creates a node object """
            self._element = element
            self._next = next_node

    def __init__(self):
        """ Creates an empty queue """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Returns true if the queue is empty """
        return self._size == 0

    def first(self):
        """ Returns but do not remove the first element of the queue

        Raises Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('LinkedQueue is empty')
        return self._head._element

    def enqueue(self, element):
        """ Adds an element to the end of the queue """
        new_node = self._Node(element, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """ Removes and returns an element from the front of the queue

        Raises Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('LinkedQueue is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
