class ArrayQueue:
    """ FIFO Queue implementation using python list as underlying storage """
    def __init__(self):
        self._data = []
        self._front = 0
        self._size = 0

    def __len__(self):
        """ Returns the number of elements in the queue """
        return self._size

    def is_empty(self):
        """ Returns true if the queue is empty """
        return self._size == 0

    def first(self):
        """ Returns (but do not remove) the element at the front of the queue

        Raises Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def enqueue(self, element):
        """ Enqueues an element to the end of the queue """
        self._size += 1
        self._data.append(element)

    def dequeue(self):
        """ Removes and returns an element from the front of the queue

        Raises Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty')

        # Resizes the queue when its size is near the half
        if self._front * 2 > len(self._data):
            self._resize()

        element = self._data[self._front]
        self._size -= 1
        self._front += 1
        return element

    def _resize(self):
        """ Resizes the queue when its size is near the half """
        new_list = []
        for i in range(self._front, len(self._data)):
            new_list.append(self._data[i])
        self._data = new_list
        self._size = len(new_list)
        self._front = 0


class Empty(Exception):
    """ Error attempting to access an element from an empty container """
    pass
