class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end = True

    def search(self, key):
        current = self.root
        for char in key:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end

    def has_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
