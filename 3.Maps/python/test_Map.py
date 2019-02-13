import unittest
from Map import Map


class TestMap(unittest.TestCase):

    def setUp(self):
        print('Sets up map')
        self.map = Map()
        self.map.add("key1", "MNO")
        self.map.add("key2", "XYZ")

    def tearDown(self):
        print('Tears down map\n')

    def test_map_instance(self):
        print('Should create an instance')
        self.assertIsInstance(self.map, Map)

    def test_add_method(self):
        print('Should add some items to the map')
        self.assertEqual(len(self.map), 2)

        keys = ["key1", "key2"]
        values = ["MNO", "XYZ"]
        i = 0
        for item in self.map:
            self.assertEqual(item.key, keys[i])
            self.assertEqual(item.value, values[i])
            i += 1

    def test_remove_method(self):
        print("Should remove item from the map")
        self.map.remove("key2")
        self.assertEqual(len(self.map), 1)

    def test_valueOf_method(self):
        print("Should return a value associated with the give key, otherwise, ValueError if invalid key")
        self.assertEqual(self.map.valueOf("key1"), "MNO")

        with self.assertRaises(ValueError):
            self.map.valueOf("key3")

    def test_item_membership(self):
        print("Should contain the given key")
        self.assertTrue("key1" in self.map)
        self.assertFalse("key3" in self.map)

    def test_map_is_iterable(self):
        print("Should be iterable")

        keys = ["key1", "key2"]
        values = ["MNO", "XYZ"]
        i = 0
        for item in self.map:
            self.assertEqual(item.key, keys[i])
            self.assertEqual(item.value, values[i])
            i += 1


if __name__ == '__main__':
    unittest.main()
