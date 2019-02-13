class DoublyLinkedList:
    """ The implementation of the Doubly Linked List ADT """

    def __init__(self):
        """ Creates an empty list instance """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Gets the length of the list """
        return self._size

    def __contains__(self, item):
        """ Determines if any target value exists """
        pass

    def __iter__(self):
        """ Makes the list iterable """
        pass

    @property
    def head(self):
        """ Gets the current head """
        return self._head

    @property
    def tail(self):
        """ Gets the current tail """
        return self._tail

    @property
    def size(self):
        """ Gets the list size """
        return self._size

    @property
    def empty(self):
        """ Determines the emptiness of the list """
        return self._size is 0

    def addFront(self, data):
        """ Adds a node to the front of the list """
        new_list = _Node(data)
        temp = self._head

        if self._head is None:
            self._head = new_list
            self._tail = new_list
        else:
            new_list.next = temp
            new_list.next.prev = new_list
            self._head = new_list
        self._size += 1

    """ Adds a node to the back of the list """
    def addBack(self, data):
        newList = _Node(data)
        temp = self._tail

        if self._tail is None:
            self._head = newList
            self._tail = newList
        else:
            newList.prev = temp
            self._tail.next = newList
            self._tail = newList
        self._size += 1

    """ Removes a node from the front of the list"""
    def removeFront(self):
        if self._head is None:
            return

        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._head.next.prev = None
            self._head = self._head.next
        self._size -= 1

    """ Removes node from the back of the list """
    def removeBack(self):
        if self._head is None:
            return

        if self._size == 1:
            self._head = None
            self._tail = None
        else:
            self._tail.prev.next = None
            self._tail = self._tail.prev
        self._size -= 1

    """ Removes a node from the list """
    def remove(self, target):
        node = self.find(target)
        if node is not None:
            if self._size == 1:
                self._head = None
                self._tail = None
            else:
                if node.prev is None:
                    node.next.prev = None
                    self._head = node.next
                elif node.next is None:
                    node.prev.next = None
                    self._tail = node.prev
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node = None
            self._size -= 1

    """ Finds nod in the list """
    def find(self, target):
        current = self._head
        while current is not None:
            if target == current.data:
                return current
            current = current.next

    """ Inserts a node in the list """
    def insert(self, this_value, after_this_value):
        current = self._head
        while current is not None:
            if after_this_value == current.data:
                new_node = _Node(this_value)

                new_node.next = current.next
                new_node.prev = current

                current.next.prev = new_node
                current.next = new_node

                self._size += 1
                return True

            current = current.next

    """ Traverses the list in reverse order """
    def reverseTraversal(self, tail=None):
        if tail is not None:
            current = tail
        else:
            current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev


""" Storage class for a doubly linked list node """


class _Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def main():
    l = DoublyLinkedList()
    l.addFront(5)
    l.addFront(3)
    l.addFront(2)
    l.addFront(1)

    # l.removeFront()
    # l.remove(4)

    # 1, 2, 3, 4, 5
    l.insert(4, 3)

    print(l.head.next.next.next.next.prev.prev.data)
    print(l.size)


if __name__ == '__main__':
    main()