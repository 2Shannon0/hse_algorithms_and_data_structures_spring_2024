import unittest
from index import write_result_in_file


class Test_b_m_search(unittest.TestCase):
    def do_command_test(self, input, expected_output):
        output = "tmp_otput.txt"
        write_result_in_file(input, output)

        with open(expected_output, "r") as file:
            expected_output = file.read()

        with open(output, "r") as file:
            actual_output = file.read()
        self.assertEqual(actual_output, expected_output)

    def test0_from_example(self):
        self.do_command_test("0-input.txt", "0-expected-output.txt")

    def test1_one_line(self):
        self.do_command_test("1-input.txt", "1-expected-output.txt")

    def test2_empty_text(self):
        self.do_command_test("2-input.txt", "2-expected-output.txt")

    def test3_empty_input(self):
        self.do_command_test("3-input.txt", "3-expected-output.txt")

    def test4_many_lines(self):
        self.do_command_test("4-input.txt", "4-expected-output.txt")
