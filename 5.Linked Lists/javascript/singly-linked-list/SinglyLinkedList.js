const Node = require('./Node');

class SinglyLinkedList {
  constructor() {
    // Contains node reference as head
    this._head = null;

    // Contains node reference as tail
    this._tail = null;

    // Determines size of the list
    this._size = 0;
  }

  /**
   * Get the current head
   * 
   * @return {Node}
   */
  getHead() {
    return this._head;
  }

  /**
   * Get the current tail
   */
  getTail() {
    return this._tail;
  }

  /**
   * Gets the list size
   * 
   * @param {Integer} data 
   */
  getSize() {
    return this._size;
  }

  /**
   * Checks if the list is empty
   * 
   * @param {Boolean} data 
   */
  isEmpty() {
    return this._size === 0;
  }

  /**
   * Adds an item to the front of the list
   * 
   * @param {String|Integer} data
   * @return void 
   */
  addFirst(data) {
    const node = new Node(data);
    const temp = this._head;

    this._head = node;
    this._head.setNext(temp);

    this._size++;

    if (this._size == 1) {
      this._tail = this._head;
    }
  }

  /**
   * Adds an item to the end of the list
   * 
   * @param {String|Integer} data 
   * @return void
   */
  addLast(data) {
    const node = new Node(data);
    if (this._size == 0) {
      this._head = node;
    } else {
      this._tail.setNext(node);
    }

    this._tail = node;
    this._size++;
  }

  /**
   * Removes an item from the front of the list 
   * 
   * @return void
   */
  removeFirst() {
    if (this._size !== 0) {
      this._head = this._head.getNext();
      this._size--;
    }

    if (this._size === 0) {
      this._tail = null;
    }
  }

  /**
   * Removes an item from the end of the list
   * 
   * @return void
   */
  removeLast() {
    if (this._size !== 0) {
      if (this._size == 1) {
        this._head = null;
        this._tail = null;
      } else {
        let current = this._head;
        while (current.getNext() !== this._tail) {
          current = current.getNext();
        }

        current.setNext(null);
        this._tail = current;
      }

      this._size--;
    }
  }

  /**
   * Finds an item from the list
   * 
   * @param {String|Integer} data
   * @return {Node|Boolean} 
   */
  find(data) {
    if (this.isEmpty()) {
      return false;
    }

    let node = this._head;
    while (node !== null) {
      if (node.getData() === data) {
        return node;
      }

      node = node.getNext();
    }

    return false;
  }

  /**
   * Insert an item in the list after the specified item
   * 
   * @param {String|Integer} insert 
   * @param {String|Integer} after 
   * @return {Node|Boolean}
   */
  insert(insertThisElement, afterThisElement) {
    if (this.isEmpty()) {
      return false;
    }

    let node = this._head;
    while (node !== null) {
      if (node.getData() === afterThisElement) {
        const newNode = new Node(insertThisElement);

        if (node.getNext() == null) {
          this._tail = newNode;
        }

        newNode.setNext(node.getNext());
        node.setNext(newNode);

        this._size++;

        return newNode;
      }

      node = node.getNext();
    }

    return false;
  }

  display() {
    if (this.isEmpty()) {
      return null;
    }

    let node = this._head;
    let items = [];
    while (node !== null) {
      items.push(node.getData());
      node = node.getNext();
    }

    return items;
  }
}

module.exports = SinglyLinkedList;