/**
 * The implementation of Map ADT
 * Using JavaScript's Array ADT
 */

class Map {

  // Creates an empty map instance
  constructor() {
    this._elements = [];
  }

  // Makes the map iterable
  *[Symbol.iterator]() {
    for (let element of this._elements) {
      yield element;
    }
  }

  // Gives the length of the map
  len() {
    return this._elements.length;
  }

  // Determines an element's existence
  contains(element) {
    const index = this._findPosition(element);
    if (index === null) {
      return false;
    } else {
      return true;
    }
  }

  // Returns the value associated with the given key
  valueOf(key) {
    const index = this._findPosition(key);
    if (index === null) {
      throw new Error('Invalid map key.');
    }

    return this._elements[index].value;
  }

  // Adds a new entry to the map if the key does exist. Otherwise,
  // the new value replaces the current value associated with the key. 
  add(key, value) {
    const index = this._findPosition(key);
    if (index !== null) {
      this._elements[index].value = value;

      return false;
    } else {
      const new_entry = new _MapEntry(key, value);
      this._elements.push(new_entry);

      return true;
    }
  }

  // Removes the entry associated with the key
  remove(key) {
    const index = this._findPosition(key);
    if (index === null) {
      throw new Error('Invalid map key.');
    }

    this._elements.pop(index);
  }

  // Finds index position for the given key in the list
  _findPosition(key) {
    for (let i = 0; i < this._elements.length; i++) {
      if (this._elements[i].key === key) {
        return i;
      }
    }

    return null;
  }
}

// Storage class for holding key=>value pairs
class _MapEntry {
  constructor(key, value) {
    this.key = key;
    this.value = value;
  }
}

module.exports = Map;