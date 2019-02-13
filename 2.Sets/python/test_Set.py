import unittest
from Set import Set
from unittest.mock import patch


class TestSetMethods(unittest.TestCase):

    def setUp(self):
        self.s = Set()

    def test_add_method(self):
        print('Testing add method')
        self.s.add(1)
        self.s.add(2)
        index = 1
        for item in self.s:
            self.assertEqual(item, index)
            index += 1

        with self.assertRaises(ValueError):
            self.s.add(2)

    def test_length(self):
        print('Testing length')
        self.s.add('a')
        self.s.add('b')
        self.assertEqual(len(self.s), 2)

    # def test_mock_a_method(self):
    #     with patch('class.module.method') as mocked_method:
    #         mocked_method.return_value.attribute = True
    #         mocked_method.return_value.attribute = 'Success'
    #
    #         schedule = self.s.call_the_method('with_argument')
    #         mocked_method.assert_called_with('with_argument')
    #         self.assertEqual(schedule, 'Success')


if __name__ == '__main__':
    unittest.main()