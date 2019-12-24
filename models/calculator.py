import unittest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def sum(self, numbers):  # Take in an array of nums
        sum = 0
        for i in numbers:
            sum += i
        return sum

    def max(self, numbers):  # Find max of list of nums
        pass


class TestCalculator(unittest.TestCase):

    def test_add_zeroes(self):
        x = 0
        y = 0
        ans = 0
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_simple(self):
        x = 1
        y = 1
        ans = 2
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_five_five(self):
        x = 5
        y = 5
        ans = 10
        self.assertEqual(Calculator().add(x, y), ans)

    def test_subtract_five_five(self):
        x = 5
        y = 5
        ans = 0
        self.assertEqual(Calculator().subtract(x, y), ans)

    def test_subtract_8_10(self):
        x = 8
        y = 10
        ans = -2
        self.assertEqual(Calculator().subtract(x, y), ans)

    def test_multiply_five_five(self):
        x = 5
        y = 5
        ans = 25
        self.assertEqual(Calculator().multiply(x, y), ans)

    def test_multiply_ten_zero(self):
        x = 10
        y = 0
        ans = 0
        self.assertEqual(Calculator().multiply(x, y), ans)

    def test_sum_minus_11519(self):
        nums = [-1, -1, -5, -1, -9]
        ans = -17
        self.assertEqual(Calculator().sum(nums), ans)

    def test_sum_8892310(self):
        nums = [8, 8, 9, 2, 3, 1, 0]
        ans = 31
        self.assertEqual(Calculator().sum(nums), ans)

    def test_sum_mixed_3149(self):
        nums = [3, 1, 4, -9]
        ans = -1
        self.assertEqual(Calculator().sum(nums), ans)


if __name__ == "__main__":
    unittest.main()
