import unittest
from index import exchange


class Test_exchange(unittest.TestCase):
    def test_0(self):
        result = exchange([1, 2, 5, 10], 11)
        expected_result = [10, 1]
        self.assertEqual(result, expected_result)

    def test_1(self):
        result = exchange([1, 2, 5], 11)
        expected_result = [5, 5, 1]
        self.assertEqual(result, expected_result)

    def test_2(self):
        result = exchange([1, 2, 5, 10], 9)
        expected_result = [5, 2, 2]
        self.assertEqual(result, expected_result)

    def test_3(self):
        result = exchange([2, 5, 10], 1)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_4(self):
        result = exchange([], 200)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_5(self):
        result = exchange([3, 7], 5)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_6(self):
        result = exchange([1, 2, 5, 10], 99)
        expected_result = [10, 10, 10, 10, 10, 10, 10, 10, 10, 5, 2, 2]
        self.assertEqual(result, expected_result)

    def test_7(self):
        result = exchange([1, 2, 5, 10, 25, 50], 76)
        expected_result = [50, 25, 1]
        self.assertEqual(result, expected_result)

    def test_8(self):
        result = exchange([1, 2, 5, 10, 25], 37)
        expected_result = [25, 10, 2]
        self.assertEqual(result, expected_result)

    def test_9(self):
        result = exchange([1, 2, 5, 10], 100)
        expected_result = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(result, expected_result)

    def test_9(self):
        result = exchange([7], 7)
        expected_result = [7]
        self.assertEqual(result, expected_result)
