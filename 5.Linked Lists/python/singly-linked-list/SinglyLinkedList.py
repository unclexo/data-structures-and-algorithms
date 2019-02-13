class SinglyLinkedList:
    """ The implementation of Singly Linked List ADT """

    class _Node:
        """ Helper class for singly linked list storage """
        __slots__ = 'element', 'next'

        def __init__(self, element, next_node=None):
            self.element = element
            self.next = next_node

    def __init__(self):
        """ Creates an empty list """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Returns the number of elements of the list """
        return self._size

    def __iter__(self):
        """ Makes the list iterable """
        pass

    def is_empty(self):
        """ Returns true if the list is empty """
        return self._size == 0

    def add_front(self, element):
        """ Adds an element to the front of the list """
        self._head = self._Node(element, self._head)
        self._size += 1
        if self._size == 1:
            self._tail = self._head

    def add_last(self, element):
        """ Adds an element to the end of the list """
        new_node = self._Node(element)
        if self._size == 0:
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def remove_front(self):
        """ Removes an element from the front of the list """
        if self._size == 0:
            raise Empty('List is empty')

        self._head = self._head.next
        self._size -= 1

        if self._size == 0:
            self._tail = None

    def remove_last(self):
        """ Removes an element from the end of the list """
        if self._size == 0:
            raise Empty('List is empty')

        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            node = self._head
            while node.next != self._tail:
                node = node.next
            node.next = None
            self._tail = node
        self._size -= 1



class Empty(Exception):
    """ Error attempting to access an element from an empty list """
    pass


def main():

    sll = SinglyLinkedList()
    sll.add_front('A')
    # sll.add_front('B')
    # sll.add_last('Y')
    # sll.add_last('Z')

    sll.remove_front()

    # A, B, C, D
    print(len(sll))
    print(sll._head)
    print(sll._tail)

if __name__ == '__main__':
    main()