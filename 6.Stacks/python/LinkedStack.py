class LinkedStack:
    """ LIFO Stack implementation using Singly Linked List for storage """

    class _Node:
        """ Lightweight, nonpublic class for storing a singly linked node """
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            """ Creates a node object """
            self._element = element
            self._next = next_node

    def __init__(self):
        """ Creates an empty stack """
        self._size = 0
        self._head = None

    def __len__(self):
        """ Returns the number of elements in the stack """
        return self._size

    def is_empty(self):
        """ Returns true if the stack is empty """
        return self._size == 0

    def top(self):
        """ Returns but do not remove the element at the top of the stack

        Raises empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('LinkedStack is empty')
        return self._head._element

    def push(self, element):
        """ Adds element to the top of the stack """
        self._head = self._Node(element, self._head)
        self._size += 1

    def pop(self):
        """ Returns and removes the element from the top of the stack

        Raises empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('LinkedStack is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
