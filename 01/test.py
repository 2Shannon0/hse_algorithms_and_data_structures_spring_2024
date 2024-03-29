import unittest

from index import quicksort
from index import read_file_to_array


class TestSortData(unittest.TestCase):

    def test_1(self):
        input_data = read_file_to_array('file_1.txt')
        expected_output = [(6, 'vXANxciIts'), (19, 'fTrZaHKFkk'), (21, 'JdSdjJlULL'), (21, 'VebHNUjWyG'), (27, 'VPtRFmWgCI'), (31, 'dgiFATToGK'), (32, 'sOWjfXtcCt'), (46, 'BOhMMCiuwz'), (47, 'LiFMOIUcap'), (49, 'GJKyXNJuPN'), (76, 'kbGoAaUhkK')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

    def test_2(self):
        input_data = read_file_to_array('file_2.txt')
        expected_output = [(5, 'AaBbCcDdEe'), (11, 'FfGgHhIiJj'), (22, 'KkLlMmNnOo'), (33, 'PpQqRrSsTt'), (40, 'UuVvWwXxYy'), (45, 'Zz'), (50, 'FfEeDdCcBb')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

    def test_3(self):
        input_data = read_file_to_array('file_3.txt')
        expected_output = [(8, 'FfGgHhIiJj'), (16, 'KkLlMmNnOo'), (30, 'UuVvWwXxYy')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

    def test_4(self):
        input_data = read_file_to_array('file_4.txt')
        expected_output = [(6, 'vXANxciIts'), (7, 'kbGoAaUhkK'), (7, 'BOhMMCiuwz'), (19, 'fTrZaHKFkk'), (21, 'JdSdjJlULL'), (21, 'VebHNUjWyG'), (27, 'VPtRFmWgCI'), (31, 'dgiFATToGK'), (32, 'sOWjfXtcCt'), (46, 'LiFMOIUcap'), (47, 'GJKyXNJuPN')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

    def test_5(self):
        input_data = read_file_to_array('file_5.txt')
        expected_output = [(3, 'AaBbCcDdEe'), (3, 'FfGgHhIiJj'), (3, 'KkLlMmNnOo'), (3, 'UuVvWwXxYy'), (3, 'ZzYyXxWwVv')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

    def test_6(self):
        input_data = read_file_to_array('file_6.txt')
        expected_output = [(5, 'AaBbCcDdEe'), (5, 'FfGgHhIiJj 1324213'), (11, 'KkLlMmNnOo'), (22, 'UuVvWwXxYy'), (22, 'ZzYyXxWwVv'), (22, 'UuTtSsRrQq'), (22, 'PpOoNnMmLl'), (22, 'KkJjIiHhGg'), (22, 'FfEeDdCcBb')]

        actual_output = quicksort(input_data)

        self.assertEqual(actual_output, expected_output)

