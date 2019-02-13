class Node {
  constructor(data) {
    this._data = data;
    this._next = null;
  }

  getData() {
    return this._data;
  }

  setData(data) {
    this._data = data;
  }

  getNext() {
    return this._next;
  }

  setNext(node) {
    this._next = node;
  }
}

module.exports = Node;