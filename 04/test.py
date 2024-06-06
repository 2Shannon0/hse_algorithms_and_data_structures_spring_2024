import unittest
from index import HashTable


class TestHashT(unittest.TestCase):
    def test1_set_3_values_and_return_pairs(self):
        ht = HashTable()
        ht["andrey"] = 22
        ht["petr"] = 23
        ht["alex"] = 14
        actual_pairs = ht.items()
        expected_pairs = [("andrey", 22), ("petr", 23), ("alex", 14)]

        for pair in expected_pairs:
            self.assertIn(pair, actual_pairs)

    def test2_get_vlue_by_key(self):
        ht = HashTable()
        ht["andrey"] = 22
        ht["petr"] = 23
        ht["alex"] = 14

        actual_value = ht["petr"]
        expected_value = 23

        self.assertEqual(actual_value, expected_value)

    def test3_get_load_factor(self):
        ht = HashTable()
        ht["andrey"] = 22
        ht["petr"] = 23
        ht["alex"] = 14
        # capacity по умолчанию = 10
        # size = 3

        actual_value = ht.get_load_factor()
        expected_value = 0.3

        ##################################
        ht2 = HashTable(capacity=100)
        ht2["andrey"] = 22
        ht2["petr"] = 23
        # capacity явно задано = 100
        # size = 2

        actual_value2 = ht2.get_load_factor()
        expected_value2 = 0.02

        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_value2, expected_value2)

    def test4_get_size(self):
        ht = HashTable()

        actual_value = ht.get_size()
        expected_value = 0

        ##################################
        ht2 = HashTable(capacity=100)
        ht2["andrey"] = 22
        ht2["petr"] = 23
        # size = 2

        actual_value2 = ht2.get_size()
        expected_value2 = 2

        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_value2, expected_value2)

    def test5_raise_size(self):
        ht = HashTable()

        actual_value = ht.get_size()
        expected_value = 0

        ##################################
        ht2 = HashTable(capacity=100)
        ht2["andrey"] = 22
        ht2["petr"] = 23
        # size = 2

        actual_value2 = ht2.get_size()
        expected_value2 = 2

        ht2["marina"] = 22
        actual_value3 = ht2.get_size()
        expected_value3 = 3
        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_value2, expected_value2)
        self.assertEqual(actual_value3, expected_value3)

    def test6_get_capacity(self):
        ht = HashTable()
        # capacity по умолчанию = 10

        actual_value = ht.get_capacity()
        expected_value = 10

        ##################################
        ht2 = HashTable(capacity=200)
        # capacity явно задано = 200

        actual_value2 = ht2.get_capacity()
        expected_value2 = 200

        self.assertEqual(actual_value, expected_value)
        self.assertEqual(actual_value2, expected_value2)

    def test7_be_clear(self):
        ht = HashTable()
        ht["andrey"] = 22
        ht["petr"] = 23
        ht["alex"] = 14

        ht.clear()
        actual_pairs = ht.items()
        expected_pairs = []

        self.assertEqual(actual_pairs, expected_pairs)

    def test8_collision_resolution(self):
        # для того, чтобы создать колизию передадим hash функцию которая всегда возвращанет один и тот же индекс
        def collision_hash(key):
            return 5

        ht = HashTable(hash_func=collision_hash)
        ht["andrey"] = 22
        ht["petr"] = 23
        ht["alex"] = 14

        # с помощью метода  ht.get_bucket() получим по ключу ""ячейку""

        bucket_a = ht.get_bucket("andrey")
        bucket_p = ht.get_bucket("petr")
        # ""ячейки"" в данном случае эквиваленты - это первый узел цепочки,
        # который хранит ключ andrey и значение 22
        self.assertEqual(bucket_a, bucket_p)
        # ключ petr и значение 23, в свою очередь
        # хранятся в следующем узле цепочки
        self.assertEqual(bucket_a.next.key, "petr")
