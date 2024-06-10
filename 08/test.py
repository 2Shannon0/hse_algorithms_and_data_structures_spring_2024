import unittest
from index import johnson_algoritm


class Test_johnson_algoritm(unittest.TestCase):
    def test_1_only_positive_edge(self):
        graph = {
            "A": {"B": 4, "C": 7},
            "B": {"A": 4, "D": 2, "E": 8},
            "C": {"A": 7, "D": 2, "E": 5},
            "D": {"B": 2, "C": 2, "E": 1, "F": 4},
            "E": {"B": 8, "C": 5, "F": 11},
            "F": {"B": 8, "D": 4, "E": 11},
        }
        result = johnson_algoritm(graph)
        expected_result = {
            "A": {"A": 0, "B": 4, "C": 7, "D": 6, "E": 7, "F": 10},
            "B": {"A": 4, "B": 0, "C": 4, "D": 2, "E": 3, "F": 6},
            "C": {"A": 7, "B": 4, "C": 0, "D": 2, "E": 3, "F": 6},
            "D": {"A": 6, "B": 2, "C": 2, "D": 0, "E": 1, "F": 4},
            "E": {"A": 12, "B": 8, "C": 5, "D": 7, "E": 0, "F": 11},
            "F": {"A": 10, "B": 6, "C": 6, "D": 4, "E": 5, "F": 0},
        }
        self.assertEqual(result, expected_result)

    def test_2_with_negative_edges(self):
        graph = {
            "A": {"B": 1, "C": 4},
            "B": {"C": -2, "D": 2},
            "C": {"D": 3},
            "D": {"E": -1},
            "E": {"A": 2},
        }
        result = johnson_algoritm(graph)
        expected_result = {
            "A": {"A": 0, "B": 1, "C": -1, "D": 2, "E": 1},
            "B": {"A": 2, "B": 0, "C": -2, "D": 1, "E": 0},
            "C": {"A": 4, "B": 5, "C": 0, "D": 3, "E": 2},
            "D": {"A": 1, "B": 2, "C": 0, "D": 0, "E": -1},
            "E": {"A": 2, "B": 3, "C": 1, "D": 4, "E": 0},
        }
        self.assertEqual(result, expected_result)

    def test_3_empty_graph(self):
        graph = {}
        result = johnson_algoritm(graph)
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test_4_only_one_vertix(self):
        graph = {
            "A": {},
        }
        result = johnson_algoritm(graph)
        expected_result = {
            "A": {"A": 0},
        }
        self.assertEqual(result, expected_result)

    def test_5_with_not_connected_vertix(self):
        graph = {
            "A": {"B": 1, "C": 10},
            "B": {"C": 1},
            "C": {"D": 5},
            "D": {},
            "E": {},
        }
        result = johnson_algoritm(graph)
        expected_result = {
            "A": {"A": 0, "B": 1, "C": 2, "D": 7, "E": float("infinity")},
            "B": {
                "A": float("infinity"),
                "B": 0,
                "C": 1,
                "D": 6,
                "E": float("infinity"),
            },
            "C": {
                "A": float("infinity"),
                "B": float("infinity"),
                "C": 0,
                "D": 5,
                "E": float("infinity"),
            },
            "D": {
                "A": float("infinity"),
                "B": float("infinity"),
                "C": float("infinity"),
                "D": 0,
                "E": float("infinity"),
            },
            "E": {
                "A": float("infinity"),
                "B": float("infinity"),
                "C": float("infinity"),
                "D": float("infinity"),
                "E": 0,
            },
        }
        self.assertEqual(result, expected_result)

    def test_6_with_negative_cycle(self):
        graph = {
            "A": {"B": 1},
            "B": {"C": 1},
            "C": {"D": 5, "A": -3},
            "D": {},
            "E": {},
        }
        result = johnson_algoritm(graph)
        expected_result = "Граф содержит цикл отрицательного веса"
        self.assertEqual(result, expected_result)
