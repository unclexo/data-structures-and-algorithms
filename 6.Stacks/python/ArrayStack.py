class ArrayStack:
    """ LIFO Stack implementation using pythong list as underlying storage """

    def __init__(self):
        """ Creates an empty stack """
        self._data = []
        self._size = 0

    def __len__(self):
        """ Returns the size of the stack """
        return self._size

    def is_empty(self):
        """ Returns true if the stack is empty """
        return self._size == 0

    def top(self):
        """ Returns (but do not remove) the top element of the stack

        Raises Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def push(self, element):
        """ Adds an element to the end of the stack """
        self._size += 1
        self._data.append(element)

    def pop(self):
        """ Removes and returns an element from the top of the stack

        Raises Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        self._size -= 1
        return self._data.pop()


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
