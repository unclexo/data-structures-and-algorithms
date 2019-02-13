const Map = require('./Map');

const map = new Map();
map.add('key1', 'MNO');
map.add('key2', 'XYZ');

describe('Map ADT', () => {
  test('can create an empty map instance', () => {
    const inst = new Map();
    expect(inst).toBeTruthy();
  });

  test('can be iterable', () => {
    expect(typeof map[Symbol.iterator]).toBe('function');
  });

  test('can get the size', () => {
    expect(map.len()).toBe(2);
  });

  test('can prove the existence of an element', () => {
    expect(map.contains('key1')).toBeTruthy();
    expect(map.contains('key3')).toBeFalsy();
  });

  test('can get the value for the associated key', () => {
    expect(map.valueOf('key1')).toBe('MNO');
  });

  test('can add elements to the map', () => {
    expect(map.len()).toBe(2);

    const elements = {
      'key1': 'MNO',
      'key2': 'XYZ'
    };
    for (let element of map) {
      expect(element.value).toBe(elements[element.key]);
    }
  });

  test('can remove an element from the map', () => {
    map.remove('key2');
    expect(map.len()).toBe(1);
  })
});