# The implementation of the Set ADT
class Set:
    def __init__(self):
        self._current = 0
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return _SetIterator(self._items)

    # Adds a unique item the to the set
    def add(self, item):
        if item not in self:
            self._items.append(item)
        else:
            raise ValueError('You must put unique value')

    # Removes an item from the set
    def remove(self, item):
        assert item in self, "The item was not found in the set"
        self._items.remove(item)

    # Creates and returns new set containing elements that are in both set
    def union(self, provided_set):
        new_set = Set()
        new_set._items.extend(self._items)
        for item in provided_set:
            if item not in self:
                new_set._items.append(item)
        return new_set

    # Creates and returns new set containing elements that are in this set and the set provided
    def intersection(self, provided_set):
        new_set = Set()
        for item in self:
            if item in provided_set:
                new_set._items.append(item)
        return new_set

    # Creates and returns new set containing elements that are in this set but not in the set provided
    def difference(self, provided_set):
        new_set = Set()
        for item in self:
            if item not in provided_set:
                new_set._items.append(item)
        return new_set

    # Determines if this set is subset of the set provided
    def is_subset_of(self, provided_set):
        for item in self:
            if item not in provided_set:
                return False
        return True


# Helper iterator class for the set
class _SetIterator:
    def __init__(self, items):
        self._items = items
        self._current = 0

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

    gold = Set()
    gold.add("CSCI-112")
    gold.add("MATH-121")
    gold.add("ICT-000")

    smith = Set()
    smith.add("CSCI-112")
    smith.add("MATH-121")
    smith.add("HIST-340")
    smith.add("ECON-101")

    roberts = Set()
    roberts.add("POL-101")
    roberts.add("ANTH-230")
    roberts.add("CSCI-112")
    roberts.add("ECON-101")

    # for item in roberts.difference(smith):
    #     print(item)

    # print(len(smith))
    print(gold.is_subset_of(smith))


if __name__ == '__main__':
    main()
