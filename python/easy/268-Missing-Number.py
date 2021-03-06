'''
Psudocode:
Sort list
Loop through list
    Check that next number is i + 1
'''

import unittest


def what_is_missing_list(nums: list) -> int:
    nums.sort()
    if nums[0] != 0:
        return 0
    for i, num in enumerate(nums):
        if len(nums) == i + 1:
            return num + 1
        elif nums[i + 1] != num + 1:
            return num + 1


def what_is_missing_set(nums: list) -> int:
    num_set = set(nums)
    for i in range(len(nums) + 1):
        if i not in num_set:
            return i


def what_is_missing(nums: list) -> int:
    sum_list = sum(nums)
    list_val = 0
    for i in range(len(nums) + 1):
        list_val += i
    return list_val - sum_list


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
        output = 99
        self.assertEqual(input, output)

    def test_4320(self):
        input = what_is_missing([4, 3, 2, 0])
        output = 1
        self.assertEqual(input, output)

    def test_0(self):
        input = what_is_missing([0])
        output = 1
        self.assertEqual(input, output)

    def test_10(self):
        input = what_is_missing([1, 0])
        output = 2
        self.assertEqual(input, output)

    def test_1(self):
        input = what_is_missing([1])
        output = 0
        self.assertEqual(input, output)


if __name__ == '__main__':
    unittest.main()
