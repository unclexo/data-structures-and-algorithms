const Node = require('../src/Node')
const SinglyLinkedList = require('../src/SinglyLinkedList');


describe('Node and SinglyLinkedList Class', () => {
  test('can call constructor method', () => {
    const node = new Node();
    const list = new SinglyLinkedList();
    expect(node).toBeTruthy();
    expect(list).toBeTruthy();
  });

  test('has data and next attributes', () => {
    const node = new Node(1);
    expect(node.getData()).toEqual(1);
    expect(node.getNext()).toEqual(null);
  });
})

describe('SinglyLinkedList Class', () => {
  test('can call constructor', () => {
    const list = new SinglyLinkedList();
    expect(list).toBeTruthy();
  });
})

describe('addFirst method', () => {
  test('can add item to the front of the list', () => {
    const list = new SinglyLinkedList();
    list.addFirst(4);
    expect(list.getHead().getData()).toEqual(4);
    expect(list.getTail().getData()).toEqual(4);
  })

  test('can add more items to the front of the list', () => {
    const list = new SinglyLinkedList();
    list.addFirst(6);
    list.addFirst(5);
    list.addFirst(4);

    expect(list.display()).toEqual([4, 5, 6]);
    expect(list.getHead().getData()).toEqual(4);
    expect(list.getTail().getData()).toEqual(6);
  })
})