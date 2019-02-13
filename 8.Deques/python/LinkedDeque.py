class LinkedDeque:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """ Returns (but do not remove) the first element from the deque """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._tail._element

    def last(self):
        """ Returns (but do not remove) the last element from the deque """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._head._element

    def add_right(self, element):
        new_node = self._Node(element, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def add_left(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def remove_right(self):
        if self.is_empty():
            raise Empty('LinkedDeque is empty')

        current = self._head
        while current is not None:
            if current._next == self._tail:
                current._next = None
                self._tail = current
                self._size -= 1
                return current._element
            current = current._next

    def remove_left(self):
        if self.is_empty():
            raise Empty('LinkedDeque is empty')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element



class Empty(Exception):
    pass


def main():

    d = LinkedDeque()
    d.add_right('A')
    d.add_right('B')
    d.add_left('E')
    d.add_left('F')

    # print(d.remove_right() + ' ' + d.remove_left())
    #
    # print(d.first())
    # print(d.last())
    # print(len(d))

    print(d)



if __name__ == '__main__':
    main()