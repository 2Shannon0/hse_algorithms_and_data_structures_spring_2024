import unittest
from index import radix_sort


class TestSortData(unittest.TestCase):
    def radix_sort_test(self, input, expected_output):
        output = "tmp_output.txt"
        radix_sort(input, output)

        with open(expected_output, "r") as file:
            expected_output = file.read()

        with open(output, "r") as file:
            actual_output = file.read()

        self.assertEqual(actual_output, expected_output)

    def test0(self):
        self.radix_sort_test("0-input.txt", "0-expected-output.txt")

    def test1(self):
        self.radix_sort_test("1-input.txt", "1-expected-output.txt")

    def test2(self):
        self.radix_sort_test("2-input.txt", "2-expected-output.txt")

    def test3(self):
        self.radix_sort_test("3-input.txt", "3-expected-output.txt")

    def test4(self):
        self.radix_sort_test("4-input.txt", "4-expected-output.txt")

#     def test5(self):
#         self.radix_sort_test("5-input.txt", "5-expected-output.txt")
