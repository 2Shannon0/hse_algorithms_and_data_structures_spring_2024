# Узел односвязного списка
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Хэш-таблица с методом цепочек
class HashTable:
    def __init__(self, capacity=10, hash_func=None):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.hash_func = hash_func or self.default_hash

    def default_hash(self, key):
        return abs(hash(key)) % self.capacity

    def __setitem__(self, key, value):
        self.size += 1
        index = self.hash_func(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def __getitem__(self, key):
        index = self.hash_func(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def get_load_factor(self):
        return self.size / self.capacity

    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return self.size

    def get_bucket(self, key):
        index = self.hash_func(key)
        node = self.buckets[index]
        return node

    def clear(self):
        self.size = 0
        self.buckets = [None] * self.capacity

    def items(self):
        items_list = []
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                items_list.append((node.key, node.value))
                node = node.next
        return items_list
