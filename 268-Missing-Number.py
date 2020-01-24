'''
Psudocode:
Sort list
Loop through list
    Check that next number is i + 1
'''

import unittest


def what_is_missing(nums: list) -> int:
    pass


class TestMissing(unittest.TestCase):

    def test_301(self):
        input = what_is_missing([3, 0, 1])
        output = 2
        self.assertEqual(input, output)

    def test_964235701(self):
        input = what_is_missing([9, 6, 4, 2, 3, 5, 7, 0, 1])
        output = 8
        self.assertEqual(input, output)

    def test_1to100(self):
        list_100 = [i for i in range(99)] + [100]
        input = what_is_missing(list_100)
        output = 98
        self.assertEqual(input, output)

    def test_4320(self):
        input = what_is_missing([4, 3, 2, 0])
        output = 1
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
