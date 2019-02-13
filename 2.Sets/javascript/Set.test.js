const Set = require('./Set');

const john = new Set();
john.add('Apple');
john.add('Banana');
john.add('Mango');
john.add('Orange');

const jane = new Set();
jane.add('Apple');
jane.add('Grape');
jane.add('Guava');
jane.add('Orange');

const joe = new Set();
joe.add('Apple');
joe.add('Mango');

describe('Set ADT', () => {
  test('can be instantiated', () => {
    const inst = new Set();
    expect(inst).toBeTruthy();
  });

  test('can be iterable', () => {
    expect(typeof john[Symbol.iterator]).toBe("function");
  });

  test('can add elements in it', () => {
    expect(john.getSize()).toBe(4);
  });

  test('can get returned the number of elements in it', () => {
    expect(john.getSize()).toBe(4);
    expect(jane.getSize()).toBe(4);
  });

  test('can prove that the specified element exists', () => {
    expect(john.contains("Apple")).toBeTruthy();
    expect(john.contains("Pine Apple")).toBeFalsy();

    expect(jane.contains("Guava")).toBeTruthy();
    expect(jane.contains("Avocado")).toBeFalsy();
  });

  test('can raise error upon adding existing element', () => {
    expect(() => {
      john.add('Apple')
    }).toThrow(Error);
  });

  test('can remove an element from its collection', () => {
    john.remove("Banana");
    expect(john.getSize()).toBe(3);
  });

  test('can raise error on removing element that does not exist', () => {
    expect(() => {
      john.remove("Avocado");
    }).toThrow(Error);
  });

  test('can union between this set and the given set', () => {
    const newSet = john.union(jane);
    expect(newSet.getSize()).toBe(5);
  });

  test('can intersect between this set and the given set', () => {
    const newSet = john.intersect(jane);
    expect(newSet.getSize()).toBe(2);
  });

  test('can differ from between this set and the given set', () => {
    const newSet = john.difference(jane);
    expect(newSet.getSize()).toBe(1);
  });

  test('can prove a set is a subset of another set', () => {
    expect(joe.isSubsetOf(john)).toBeTruthy();
  });

});