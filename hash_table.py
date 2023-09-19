from typing import List


class Node:

    def __init__(self, key: int = None, val: str = None):
        if key is None or val is None:
            self.exists: bool = False
        else:
            self.exists: bool = True
            self.key = key
            self.value = val
            self.next = None

    def __repr__(self) -> str:
        if self.exists:
            return f'"{self.key}" : "{self.value}"'
        else:
            return ""


class HashTable:

    _entities: int = 0

    def __init__(self, size: int = 8):
        self.size = size
        self.__map: List[Node] = [Node()] * self.size

    def __copy__(self):
        self.size = self.size * 2
        temp: List[Node] = self.__map
        self.__map: List[Node] = [Node()] * self.size
        for node in temp:
            if node.exists:
                item = Node(node.key, node.value)
                self.__add__(item)

    def __add__(self, item: Node) -> None:
        hash_value = self.hashCode(str(item.key), self.size)

        if self.size == self._entities:
            self.__copy__()

        if self.__map[hash_value].exists:
            temp = item
            p = self.__map[hash_value]
            while p.next is not None:
                p = p.next
            p.next = temp
            self._entities = self._entities + 1

        else:
            self.__map[hash_value] = item
            self._entities = self._entities + 1

    def __getitem__(self, key: int) -> Node:

        hash_value = self.hashCode(str(key), self.size)

        if self.__map[hash_value].key == key:

            return self.__map[hash_value]

        else:
            p = self.__map[hash_value]

            while p is not None and p.key != key:
                p = p.next

            if p is not None and p.key == key:
                return p

        return None

    def find_by_value(self, value: str):

        for node in self.__map:
            temp = node
            if temp.exists:
                if temp.value == value:
                    return temp
                else:
                    while temp.next is not None:
                        if temp.next.value == value:
                            return temp.next
                        else:
                            temp = node.next

    def hashCode(self, value: str, base: int = 4219):
        hash_result = 0

        for c in value:
            hash_result = (hash_result * base + ord(c)) % self.size

        return hash_result

    def __repr__(self) -> str:
        printable = "{\n"

        for node in self.__map:
            temp = node
            if temp.exists:
                while temp.next is not None:
                    printable += f'\t {temp} \n'
                    temp = node.next
                printable += f'\t {temp} \n'

        printable += "}"

        return printable

    def delete(self, key: int) -> bool:

        if not self.__getitem__(key):
            return False

        hash_value = self.hashCode(str(key), self.size)

        if self.__map[hash_value].key == key:
            self.__map[hash_value].exists = False
            return True

        else:
            p = self.__map[hash_value]

            temp = None

            while p is not None and p.key != key:
                temp = p
                p = p.next

            if p is None:
                return False
            else:
                temp.next = p.next
                return True



map = HashTable()
node = Node(1, "fasdf")
map.__add__(node)
node = Node(2, "fasdf2")
map.__add__(node)
node = Node(3, "fasdf3")
map.__add__(node)
node = Node(4, "fasdf4")
map.__add__(node)
node = Node(5, "fasdf5")
map.__add__(node)
node = Node(6, "fasdf6")
map.__add__(node)
node = Node(7, "fasdf7")
map.__add__(node)
# node = Node(7, "fasdf7")
# map.__add__(node)
# node = Node(8, "fasdf8")
# map.__add__(node)
# node = Node(9, "fasdf9")
# map.__add__(node)
# node = Node(10, "fasdf10")
# map.__add__(node)
# node = Node(11, "fasdf11")
# map.__add__(node)

print(map)
