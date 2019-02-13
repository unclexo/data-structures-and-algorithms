"""
    The implementation of Map ADT
    But using Python list ADT
"""


class Map:

    """ Creates empty map instance """
    def __init__(self):
        self._items = list()

    """ Returns the number of entries in the map """
    def __len__(self):
        return len(self._items)

    """ Determines if the map contains the given key """
    def __contains__(self, key):
        index = self._findPosition(key)
        return index is not None

    """ 
        Adds a new entry to the map if the key does exist. Otherwise, 
        the new value replaces the current value associated with the key. 
    """
    def add(self, key, value):
        index = self._findPosition(key)
        if index is not None:
            self._items[index].value = value
            return False
        else:
            new_entry = _MapEntry(key, value)
            self._items.append(new_entry)
            return True

    """ Returns the value associated with the given key """
    def valueOf(self, key):
        index = self._findPosition(key)

        if index is None:
            raise ValueError("Invalid map key.")
        return self._items[index].value

    """ Removes the entry associated with the key """
    def remove(self, key):
        index = self._findPosition(key)
        if index is None:
            raise ValueError("Invalid map key")
        self._items.pop(index)

    """ Returns an iterator for traversing the keys in the map """
    def __iter__(self):
        return _MapIterator(self._items)

    """ Finds index position for the given key in the list """
    def _findPosition(self, key):
        # Iterates through each entry in the list
        for i in range(len(self)):
            # Is the key stored in the position (i)th?
            if self._items[i].key == key:
                return i
        # When not found, return None
        return None


""" Storage class for holding key=>value pairs """


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


""" Helper class for map iterator """


class _MapIterator:
    def __init__(self, items):
        self._current = 0
        self._items = items

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < len(self._items):
            item = self._items[self._current]
            self._current += 1
            return item
        else:
            raise StopIteration


def main():

    # Should create an empty map
    m = Map()

    # Should add some key/value pairs
    m.add("key1", "MNO")
    m.add("key2", "XYZ")

    len(m)

    # Should remove "key2"
    m.remove("key2")

    # Should contain "key1"
    print("key1" in m)

    # Should raise ValueError
    # print(m.valueOf("key2"))

    # Should be iterable
    for item in m:
        print(item.key, item.value)


if __name__ == '__main__':
    main()
