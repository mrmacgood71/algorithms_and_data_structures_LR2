import unittest
from typing import List
from linked_list import LinkedList, Cat, Node, Direction, IndexOutOfBoundException
from hash_table import HashTable, Node, TheSameKeyException


class TestLinkedList(unittest.TestCase):
    def test_adding(self):
        linked_list = LinkedList[Cat]()
        linked_list.__add__(Cat("Max", 7))
        linked_list.__add__(Cat("Max2", 7))
        linked_list.__add__(Cat("Max3", 7))
        linked_list.__add__(Cat("Max4", 7))
        linked_list.__add__(Cat("Max5", 7))
        self.assertTrue(linked_list.get_size() == 5)
        self.assertEqual(linked_list.__getitem__(1), Cat("Max4", 7))

    def test_is_empty(self):
        linked_list = LinkedList[Cat]()
        self.assertTrue(linked_list.is_empty())

    def test_length(self):
        linked_list = LinkedList[Cat]()
        linked_list.__add__(Cat("Max", 7))
        linked_list.__add__(Cat("Max2", 7))
        self.assertTrue(linked_list.get_size() == 2)

    def test_forward_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max", 7))
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))
        actual_list.__add__(Cat("Max4", 7))
        actual_list.__add__(Cat("Max5", 7))

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max3", 7))
        expected_list.__add__(Cat("Max4", 7))
        expected_list.__add__(Cat("Max5", 7))
        expected_list.__add__(Cat("Max", 7))
        expected_list.__add__(Cat("Max2", 7))

        actual_list.shift(Direction.FORWARD, 2)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list.__getitem__(i), expected_list.__getitem__(i))
            print(actual_list.__getitem__(i))
            print(expected_list.__getitem__(i))

    def test_backward_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max", 7))
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))
        actual_list.__add__(Cat("Max4", 7))
        actual_list.__add__(Cat("Max5", 7))

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max3", 7))
        expected_list.__add__(Cat("Max4", 7))
        expected_list.__add__(Cat("Max5", 7))
        expected_list.__add__(Cat("Max", 7))
        expected_list.__add__(Cat("Max2", 7))

        actual_list.shift(Direction.BACKWARD, 3)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list.__getitem__(i), expected_list.__getitem__(i))
            print(actual_list.__getitem__(i))
            print(expected_list.__getitem__(i))

    def test_push_head(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max", 7))
        actual_list.__add__(Cat("Max2", 7))

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max", 7))
        expected_list.__add__(Cat("Max2", 7))
        expected_list.__add__(Cat("Max3", 7))

        actual_list.push_head(Cat("Max3", 7))
        self.assertEqual(actual_list.head(), expected_list.head())
        print(actual_list.head())
        print(expected_list.head())

    def test_get_head(self):
        actual_list = LinkedList[Cat]()
        cat = Cat("Max", 7)
        actual_list.__add__(cat)
        self.assertTrue(actual_list.head() == cat)

    def test_get_tail(self):
        actual_list = LinkedList[Cat]()
        cat = Cat("Max", 7)
        actual_list.__add__(cat)
        self.assertTrue(actual_list.tail() == cat)

    def test_push_tail(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max", 7))
        expected_list.__add__(Cat("Max2", 7))
        expected_list.__add__(Cat("Max3", 7))

        actual_list.push_tail(Cat("Max", 7))
        self.assertEqual(actual_list.tail(), expected_list.tail())
        print(actual_list.tail())
        print(expected_list.tail())

    def test_get_item(self):
        actual_list = LinkedList[Cat]()
        cat_max2 = Cat("Max2", 7)
        actual_list.__add__(cat_max2)
        actual_list.__add__(Cat("Max3", 7))

        self.assertEqual(actual_list.__getitem__(1), cat_max2)
        print(actual_list.__getitem__(1))
        print(cat_max2)

    def test_append_with_index(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max1", 7))
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))

        actual_list.__add__(Cat("Max4", 7), 1)

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max1", 7))
        expected_list.__add__(Cat("Max2", 7))
        expected_list.__add__(Cat("Max4", 7))
        expected_list.__add__(Cat("Max3", 7))

        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list.__getitem__(i), expected_list.__getitem__(i))
            print(actual_list.__getitem__(i))
            print(expected_list.__getitem__(i))

    def test_item_containing(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max1", 7))
        self.assertTrue(Cat("Max1", 7) in actual_list)
        print(Cat("Max1", 7) in actual_list)

    def test_deletion(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max1", 7))
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))

        actual_list.__delitem__(2)
        with self.assertRaises(IndexOutOfBoundException):
            actual_list.__getitem__(2)

    def test_forward_negative_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list.__add__(Cat("Max", 7))
        actual_list.__add__(Cat("Max2", 7))
        actual_list.__add__(Cat("Max3", 7))
        actual_list.__add__(Cat("Max4", 7))
        actual_list.__add__(Cat("Max5", 7))

        expected_list = LinkedList[Cat]()
        expected_list.__add__(Cat("Max5", 7))
        expected_list.__add__(Cat("Max", 7))
        expected_list.__add__(Cat("Max2", 7))
        expected_list.__add__(Cat("Max3", 7))
        expected_list.__add__(Cat("Max4", 7))


        actual_list.shift(Direction.FORWARD, -1)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list.__getitem__(i), expected_list.__getitem__(i))
            print(actual_list.__getitem__(i))
            print(expected_list.__getitem__(i))



class TestHashTableArray(unittest.TestCase):
    map = HashTable()
    node = Node(1, "fasdf")
    map.__add__(node.key, node.value)
    node2 = Node(2, "fasdf2")
    map.__add__(node2.key, node2.value)
    node3 = Node(3, "fasdf3")
    map.__add__(node3.key, node3.value)
    node4 = Node(4, "fasdf4")
    map.__add__(node4.key, node4.value)
    node5 = Node(5, "fasdf5")
    map.__add__(node5.key, node5.value)
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

        print(self.map)

    def test_find_by_key(self):
        actual = self.map.__getitem__(1)
        expected = self.node
        self.assertEqual(expected, actual)

    def test_item_containing(self):
        self.assertTrue(self.node in self.map)

    def test_find_by_value(self):
        expected = self.node3.value
        actual = self.map.find_by_value("fasdf3").value
        self.assertEqual(expected, actual)

    def test_is_hash_fun_correct(self):
        hash_result = self.map._hash_code("12345")
        hash_result2 = self.map._hash_code("12345")
        s = "12345"
        hash_result3 = self.map._hash_code(s)

        self.assertEqual(hash_result, hash_result2)
        self.assertEqual(hash_result2, hash_result3)
        self.assertEqual(hash_result, hash_result3)

        print(hash_result)
    def test_add_the_same_key(self):

        with self.assertRaises(TheSameKeyException):
            same_map = HashTable(2)
            same_map.__add__(1, "fasdf")
            same_map.__add__(1, "fasdf21")
            same_map.__add__(21, "fasdf211")

    def test_deleting(self):
        del_map = HashTable(2)
        del_map.__add__(1, "fasdf")
        del_map.__add__(21, "fasdf21")
        del_map.__add__(41, "fasdf41")
        del_map.__add__(3, "fasdf3")
        del_map.__add__(2, "fasdf2")

        print(del_map)

        self.assertTrue(del_map.delete(41))
        self.assertFalse(del_map.__getitem__(41).visible)

        print(del_map)

