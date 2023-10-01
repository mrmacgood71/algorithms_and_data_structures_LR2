import unittest
from typing import List

from hash_table import HashTable, TheSameKeyException
from linked_list import LinkedList, Cat, Direction, IndexOutOfBoundException


class TestLinkedList(unittest.TestCase):

    def test_adding(self):
        linked_list = LinkedList[Cat]()
        linked_list[0] = Cat("Max", 7)
        linked_list[0] = Cat("Max2", 7)
        linked_list[0] = Cat("Max3", 7)
        linked_list[0] = Cat("Max4", 7)
        linked_list[0] = Cat("Max5", 7)

        self.assertTrue(linked_list.get_size() == 5)
        self.assertEqual(linked_list[1], Cat("Max4", 7))

        print(f'{linked_list[1]} == {Cat("Max4", 7)}')

    def test_is_empty(self):
        linked_list = LinkedList[Cat]()
        self.assertTrue(linked_list.is_empty())

    def test_length(self):
        linked_list = LinkedList[Cat]()
        linked_list[0] = Cat("Max", 7)
        linked_list[0] = Cat("Max2", 7)
        self.assertTrue(linked_list.get_size() == 2)

    def test_forward_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max", 7)
        actual_list[0] = Cat("Max2", 7)
        actual_list[0] = Cat("Max3", 7)
        actual_list[0] = Cat("Max4", 7)
        actual_list[0] = Cat("Max5", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max3", 7)
        expected_list[0] = Cat("Max4", 7)
        expected_list[0] = Cat("Max5", 7)
        expected_list[0] = Cat("Max", 7)
        expected_list[0] = Cat("Max2", 7)

        actual_list.shift(Direction.FORWARD, 2)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list[i], expected_list[i])
            print(f'{actual_list[i]} == {expected_list[i]}')

    def test_backward_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max", 7)
        actual_list[0] = Cat("Max2", 7)
        actual_list[0] = Cat("Max3", 7)
        actual_list[0] = Cat("Max4", 7)
        actual_list[0] = Cat("Max5", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max3", 7)
        expected_list[0] = Cat("Max4", 7)
        expected_list[0] = Cat("Max5", 7)
        expected_list[0] = Cat("Max", 7)
        expected_list[0] = Cat("Max2", 7)

        actual_list.shift(Direction.BACKWARD, 3)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list[i], expected_list[i])
            print(f'{actual_list[i]} == {expected_list[i]}')

    def test_push_head(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max", 7)
        actual_list[0] = Cat("Max2", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max", 7)
        expected_list[0] = Cat("Max2", 7)
        expected_list[0] = Cat("Max3", 7)

        actual_list.push_head(Cat("Max3", 7))
        self.assertEqual(actual_list.head(), expected_list.head())
        print(f'{actual_list.head()} == {expected_list.head()}')

    def test_get_head(self):
        actual_list = LinkedList[Cat]()
        cat = Cat("Max", 7)
        actual_list[0] = cat
        self.assertTrue(actual_list.head() == cat)

    def test_get_tail(self):
        actual_list = LinkedList[Cat]()
        cat = Cat("Max", 7)
        actual_list[0] = cat
        self.assertTrue(actual_list.tail() == cat)

    def test_push_tail(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max2", 7)
        actual_list[0] = Cat("Max3", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max", 7)
        expected_list[0] = Cat("Max2", 7)
        expected_list[0] = Cat("Max3", 7)

        actual_list.push_tail(Cat("Max", 7))
        self.assertEqual(actual_list.tail(), expected_list.tail())
        print(f'{actual_list.tail()} == {expected_list.tail()}')

    def test_get_item(self):
        actual_list = LinkedList[Cat]()
        cat_max2 = Cat("Max2", 7)
        actual_list.insert(cat_max2)
        actual_list.insert(Cat("Max3", 7))

        self.assertEqual(actual_list[1], cat_max2)
        print(f'{actual_list[1]} == {cat_max2}')

    def test_append_with_index(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max1", 7)
        actual_list[0] = Cat("Max2", 7)
        actual_list[0] = Cat("Max3", 7)
        actual_list[2] = Cat("Max4", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max4", 7)
        expected_list[0] = Cat("Max1", 7)
        expected_list[0] = Cat("Max2", 7)
        expected_list[0] = Cat("Max3", 7)

        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list[i], expected_list[i])
            print(f'{actual_list[i]} == {expected_list[i]}')

    def test_item_containing(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max1", 7)
        self.assertTrue(Cat("Max1", 7) in actual_list)
        print(Cat("Max1", 7) in actual_list)

    def test_deletion(self):
        actual_list = LinkedList[Cat]()
        actual_list.insert(Cat("Max1", 7))
        actual_list.insert(Cat("Max2", 7))
        actual_list.insert(Cat("Max3", 7))

        del actual_list[2]
        with self.assertRaises(IndexOutOfBoundException):
            actual_list[2]

    def test_forward_negative_shift(self):
        actual_list = LinkedList[Cat]()
        actual_list[0] = Cat("Max", 7)
        actual_list[0] = Cat("Max2", 7)
        actual_list[0] = Cat("Max3", 7)
        actual_list[0] = Cat("Max4", 7)
        actual_list[0] = Cat("Max5", 7)

        expected_list = LinkedList[Cat]()
        expected_list[0] = Cat("Max5", 7)
        expected_list[0] = Cat("Max", 7)
        expected_list[0] = Cat("Max2", 7)
        expected_list[0] = Cat("Max3", 7)
        expected_list[0] = Cat("Max4", 7)

        actual_list.shift(Direction.FORWARD, -1)
        for i in range(0, actual_list.get_size()):
            self.assertEqual(actual_list[i], expected_list[i])
            print(f'{actual_list[i]} == {expected_list[i]}')


class TestHashTableArray(unittest.TestCase):
    map = HashTable()
    map[1] = "fasdf"
    map[2] = "fasdf2"
    map[3] = "fasdf3"
    map[4] = "fasdf4"
    map[5] = "fasdf5"

    def test_init(self):
        values: List[HashTable._Node] = self.map.__dict__['_HashTable__map']

        state = False
        state = self.map[1] in values
        self.assertTrue(state)
        state = self.map[2] in values
        self.assertTrue(state)
        state = self.map[3] in values
        self.assertTrue(state)
        state = self.map[4] in values
        self.assertTrue(state)
        state = self.map[5] in values
        self.assertTrue(state)

        print(self.map)

    def test_find_by_key(self):
        actual = self.map[1].key
        expected = 1
        self.assertEqual(expected, actual)
        print(f'{expected} == {actual}')

    def test_item_containing(self):
        self.assertTrue(self.map[1] in self.map)
        print(self.map[1] in self.map)

    def test_find_by_value(self):
        expected = "fasdf3"
        actual = self.map.find_by_value("fasdf3").value
        self.assertEqual(expected, actual)
        print(f'{expected} == {actual}')

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
            same_map[1] = "fasdf"
            same_map[1] = "fasdf21"
            same_map[21] = "fasdf211"

    def test_deleting(self):
        del_map = HashTable(2)
        del_map[1] = "fasdf"
        del_map[21] = "fasdf21"
        del_map[41] = "fasdf41"
        del_map[3] = "fasdf3"
        del_map[2] = "fasdf2"

        print(del_map)
        # case 1 - с возвращаемым значением
        self.assertTrue(del_map.delete(41))
        self.assertFalse(del_map[41].visible)
        # case 2 - переопределение, без возвращаемого значения
        del del_map[1]
        self.assertFalse(del_map[1].visible)

        print(del_map)
