class CircularlyLinkedList:
    """ The implementation of the Circular Linked List ADT """

    class _Node:
        """ Lightweight, nonpublic class for storing a circularly linked node """
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node=None):
            """ Creates a node object """
            self.element = element
            self.next = next_node

    def __init__(self):
        """ Creates an empty list """
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the number of elements of the list """
        return self._size

    def is_empty(self):
        """ Returns true if the list is empty """
        return self._size == 0

    def add_(self):
        """ Adds an element to the end of the q """
