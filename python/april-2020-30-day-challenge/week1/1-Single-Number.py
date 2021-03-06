import unittest


# Count hash map solution
def single_num_count(nums: list) -> int:
    from collections import Counter
    counts = Counter(nums)
    for i in counts:
        if counts[i] == 1:
            return i
    return 0


# Set solution
def single_num(nums: list) -> int:
    unique_nums = set()
    for i in nums:
        if i in unique_nums:
            unique_nums.remove(i)
        else:
            unique_nums.add(i)
    return unique_nums.pop()


class TestSingleNum(unittest.TestCase):

    def test_221(self):
        self.assertEqual(single_num([2, 2, 1]), 1)

    def test_41212(self):
        self.assertEqual(single_num([4, 1, 2, 1, 2]), 4)

    def test_0(self):
        self.assertEqual(single_num([0]), 0)


if __name__ == "__main__":
    unittest.main()
