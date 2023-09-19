import unittest
from typing import List

from hash_table import HashTable, Node


class TestDynamicArray(unittest.TestCase):
    map = HashTable()
    node = Node(1, "fasdf")
    map.__add__(node)
    node2 = Node(2, "fasdf2")
    map.__add__(node2)
    node3 = Node(3, "fasdf3")
    map.__add__(node3)
    node4 = Node(4, "fasdf4")
    map.__add__(node4)
    node5 = Node(5, "fasdf5")
    map.__add__(node5)

    def test_init(self):

        values: List[Node] = self.map.__dict__['_HashTable__map']

        state = False
        state = values.__contains__(self.node)
        self.assertTrue(state)
        state = values.__contains__(self.node2)
        self.assertTrue(state)
        state = values.__contains__(self.node3)
        self.assertTrue(state)
        state = values.__contains__(self.node4)
        self.assertTrue(state)
        state = values.__contains__(self.node5)
        self.assertTrue(state)

        print(values)

    def test_find_by_key(self):
        actual = self.map.__getitem__(1)
        expected = self.node
        self.assertEqual(expected, actual)

    def test_find_by_value(self):
        expected = self.node3.value
        actual = self.map.find_by_value("fasdf3").value
        self.assertEqual(expected, actual)

    def test_is_hash_fun_correct(self):
        hash_result = self.map.hashCode("12345")
        hash_result2 = self.map.hashCode("12345")
        s = "12345"
        hash_result3 = self.map.hashCode(s)

        self.assertEqual(hash_result, hash_result2)
        self.assertEqual(hash_result2, hash_result3)
        self.assertEqual(hash_result, hash_result3)

        print(hash_result)

    def test_deleting(self):
        map = HashTable()
        node = Node(1, "fasdf")
        map.__add__(node)
        node2 = Node(2, "fasdf2")
        map.__add__(node2)
        node3 = Node(3, "fasdf3")
        map.__add__(node3)

        values: List[Node] = map.__dict__['_HashTable__map']

        self.assertTrue(map.delete(1))
        self.assertFalse(values[1].exists)

        print(values)


