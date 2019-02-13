class Deque:
    """ Deque implementation using python list as underlying storage """
    def __init__(self):
        """ Creates an empty deque """
        self._data = []

    def __len__(self):
        """ Returns the length of the deque """
        return len(self._data)

    def display(self):
        return self._data

    def is_empty(self):
        """ Returns true if the deque is empty, false otherwise """
        return len(self._data) == 0

    def first(self):
        """ Returns (but do not remove) the first element from the deque """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[-1]

    def last(self):
        """ Returns (but do not remove) the last element from the deque """
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._data[0]

    def add_first(self, element):
        """ Adds an element to the front of the deque """
        self._data.append(element)

    def add_last(self, element):
        """ Adds an element to the back of the deque """
        self._data.insert(0, element)

    def remove_first(self):
        """ Removes an element from the front of the deque """
        return self._data.pop()

    def remove_last(self):
        """ Removes an element from the back of the deque """
        return self._data.pop(0)


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
