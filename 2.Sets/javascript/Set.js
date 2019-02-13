/**
 * The implementation of Set ADT
 * Using JavaScript's Array ADT
 */
class Set {
  // Creates an empty set instance
  constructor() {
    this._elements = [];
  }

  // Make the set iterable
  *[Symbol.iterator]() {
    for (let element of this._elements) {
      yield element;
    }
  }

  // Retrieves the size of the set
  getSize() {
    return this._elements.length;
  }

  // Determines an element's existence
  contains(element) {
    if (this._elements.indexOf(element) > -1) {
      return true;
    } else {
      return false;
    }
  }

  // Adds a unique element to the set
  add(element) {
    if (this._elements.indexOf(element) < 0) {
      this._elements.push(element);
    } else {
      throw new Error("The element must be unique");
    }
  }

  // Removes an element from the set
  remove(element) {
    const position = this._elements.indexOf(element)
    if (position > -1) {
      this._elements.splice(position, 1);
    } else {
      throw new Error("The element was not found");
    }
  }

  // Creates and returns new set containing all 
  // elements in set A and those elements in set 
  // B that are not in set A
  union(givenSet) {
    if (!givenSet instanceof Set) {
      throw new Error("The argument must be instance of Set");
    }

    const newSet = new Set();
    const items = [...this._elements];
    newSet._elements = items;
    for (let element of givenSet) {
      if (this._elements.indexOf(element) < 0) {
        newSet._elements.push(element);
      }
    }

    return newSet;
  }

  // Creates and returns a new set containing elements
  // that are in both set A and set B
  intersect(givenSet) {
    if (!givenSet instanceof Set) {
      throw new Error("The argument must be instance of Set");
    }

    const newSet = new Set();
    for (let element of this._elements) {
      if (givenSet._elements.indexOf(element) > -1) {
        newSet._elements.push(element);
      }
    }

    return newSet;
  }

  // Creates and returns a new set containing elements
  // that are in set A but not in B
  difference(givenSet) {
    if (!givenSet instanceof Set) {
      throw new Error("The argument must be instance of Set");
    }

    const newSet = new Set();
    for (let element of this._elements) {
      if (givenSet._elements.indexOf(element) < 0) {
        newSet._elements.push(element)
      }
    }

    return newSet;
  }

  // Checks if this set is a subset of other set
  isSubsetOf(givenSet) {
    if (!givenSet instanceof Set) {
      throw new Error("The argument must be instance of Set");
    }

    for (let element of this._elements) {
      if (givenSet._elements.indexOf(element) < 0) {
        return false;
      }
    }

    return true;
  }
}

module.exports = Set;