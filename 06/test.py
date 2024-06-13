import unittest
from index import TrieTree


class TestTrieTree(unittest.TestCase):
    def test0_init(self):
        t = TrieTree()
        result = t.root.children
        excpected_result = {}
        self.assertEqual(result, excpected_result)

    def test1_insert_4_letters(self):
        t = TrieTree()
        t.insert("a")
        t.insert("p")
        t.insert("b")
        t.insert("c")
        result = list(t.root.children.keys())
        excpected_result = ["a", "p", "b", "c"]
        self.assertEqual(result, excpected_result)

    def test2_search_key(self):
        t = TrieTree()
        t.insert("andrey")
        t.insert("petr")
        t.insert("pet")
        result = [t.search("petr"), t.search("pet"), t.search("petrrrr")]
        excpected_result = [True, True, False]
        self.assertEqual(result, excpected_result)

    def test3_has_prefix(self):
        t = TrieTree()
        t.insert("andrey")
        t.insert("petr")
        result = [t.has_prefix("and"), t.has_prefix("pe"), t.has_prefix("alex")]
        excpected_result = [True, True, False]
        self.assertEqual(result, excpected_result)
