import unittest
from index import max_rectangle_S_0


class Test_max_S_0(unittest.TestCase):
    def test_0(self):
        result = max_rectangle_S_0("0-input.txt")
        expected_result = 4
        self.assertEqual(result, expected_result)

    def test_1(self):
        result = max_rectangle_S_0("1-input.txt")
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_2(self):
        result = max_rectangle_S_0("2-input.txt")
        expected_result = 40
        self.assertEqual(result, expected_result)

    def test_3(self):
        result = max_rectangle_S_0("3-input.txt")
        expected_result = 80
        self.assertEqual(result, expected_result)

    def test_4(self):
        result = max_rectangle_S_0("4-input.txt")
        expected_result = 30
        self.assertEqual(result, expected_result)

    def test_5(self):
        result = max_rectangle_S_0("5-input.txt")
        expected_result = 4
        self.assertEqual(result, expected_result)

    def test_6(self):
        result = max_rectangle_S_0("6-input.txt")
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_7(self):
        result = max_rectangle_S_0("7-input.txt")
        expected_result = 0
        self.assertEqual(result, expected_result)
