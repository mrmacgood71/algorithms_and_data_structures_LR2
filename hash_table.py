from typing import List
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar('T')

class TheSameKeyException(Exception):
    pass

class HashTable:
    @dataclass
    class _Node(Generic[T]):
        def __init__(self, key, value, visible: bool = True):
            self.key: Optional['T'] = key
            self.value: Optional['T'] = value
            self.visible: bool = visible
            self.next: Optional['HashTable._Node[T]'] = None

        def __repr__(self) -> str:
            if self.key is not None and self.value is not None:
                return f'"{self.key}" : "{self.value}"'
            else:
                return ""

    _entities: int = 0

    """
        Конструктор класса HashTable. 
        Инициализирует новый экземпляр хеш-таблицы с заданным размером.
        Внутри хеш-таблицы создается список (__map) из узлов (Node), каждый из которых инициализируется как None.
        
        :arg size: int = 8 - По умолчанию размер равен 8.  
    """
    def __init__(self, size: int = 8):
        self.size: int = size
        self.__map: List[HashTable._Node] = [HashTable._Node(None, None)] * self.size

    """
        Этот метод удваивает размер хеш-таблицы и копирует все элементы из старой таблицы в новую, 
        высчитывая новый хэш код для каждого элемента.
        __setitem__ - прописывается явно, чтобы передать параметр is_rehash_call
    """
    def rehash(self) -> None:
        self.size = self.size * 2
        temp = self.__map
        self.__map: List[HashTable._Node] = [HashTable._Node(None, None)] * self.size
        for node in temp:
            current = node
            if current.key is not None:
                while current.next is not None:
                    if current.visible:
                        self.__setitem__(current.key, current.value, True)
                        self[current.key].visible = current.visible
                    current = current.next
                self.__setitem__(current.key, current.value, True)

    """
            Метод добавляет новый узел в хеш-таблицу.
            Args:
                :arg item(key: T, value: T, is_rehash_call: bool = False) - пара ключ-значение, необходимые для вставки
            Если ключ уже существует в хэш-таблице, то выкидываем ошибку
            Если таблица заполнена, она сначала удваивается в размере, и рехэшируется
            Если хэш-код уже существует, проверяем, есть ли у него потомки в цепи, и вставляем в самый конец,
            иначе просто вставляем элемент в бакет

        """
    def __setitem__(self, key: T, value: T, is_rehash_call: bool = False) -> None:
        item = HashTable._Node(key, value)

        for node in self.__map:
            if node.key == item.key:
                raise TheSameKeyException("item.key exists in Hash Table")

        if self.size == self._entities:
            self.rehash()

        hash_value = self._hash_code(str(item.key))

        if self.__map[hash_value].key is not None:
            temp = item
            found = self.__map[hash_value]
            while found.next is not None:
                found = found.next
            found.next = temp
        else:
            self.__map[hash_value] = item

        if not is_rehash_call:
            self._entities = self._entities + 1

    """
        Этот метод возвращает узел с указанным ключом из хеш-таблицы. Если такого ключа нет, он возвращает None.
        Args:
            :arg key(int) - Ключ искомого элемента
            :return Node | None
    """
    def __getitem__(self, key: T) -> _Node:

        hash_value = self._hash_code(str(key))

        if self.__map[hash_value].key == key:

            return self.__map[hash_value]

        else:
            found = self.__map[hash_value]

            while found is not None and found.key != key:
                found = found.next

            if found is not None and found.key == key:
                return found

        return None

    """
         Этот метод проверяет, содержит ли хеш-таблица указанный узел. 
         Переопределение in
         
         Args:
            :arg item: Node = искомый элемент
    """
    def __contains__(self, item: _Node) -> bool:
        hash_value = self._hash_code(str(item.key))

        if self.__map[hash_value].key == item.key:
            return True

        else:
            found = self.__map[hash_value]

            while found is not None and found.key != item.key:
                found = found.next

            if found is not None and found.key == item.key:
                return True

        return False
    """
        Этот метод ищет узел с указанным значением в хеш-таблице.
        При повторе значений, находит самый первый
        
    """
    def find_by_value(self, value: T) -> _Node:
        for node in self.__map:
            temp = node
            if temp.key is None:
                continue
            if temp.value == value:
                return temp
            else:
                while temp.next is not None:
                    if temp.next.value == value:
                        return temp.next
                    else:
                        temp = node.next

    """
        Этот метод вычисляет хеш-код для указанного значения методом Горнера
        Args: 
            :arg value(str) - ключ, по которому будет строиться хэш код
            :arg base: int = 4219 - база, по которой будет строиться хэш код, может быть любой
        
    """
    def _hash_code(self, value: str) -> int:
        return int(str(hash(value))) % self.size

    """
        Переопределение print 
        Метод возвращает строковое представление хеш-таблицы.
    """
    def __repr__(self) -> str:
        printable = "\n{\n"

        for node in self.__map:
            temp = node
            while temp.next is not None:

                if temp.visible:
                    printable += f'\t {temp}'
                if temp.key is not None:
                    printable += '\n'
                temp = temp.next
            if temp.next is None and temp.visible and temp.key is not None:
                printable += f'\t {temp}\n'

        printable += "\n}"

        return printable
    """
        Метод удаляет узел с указанным ключом из хеш-таблицы.
        Args: 
            :arg key(int) - ключ, по которому будет удаляться элемент
        По ключу 
    """

    def __delitem__(self, key: T) -> bool:

        if not self[key]:
            return False

        hash_value = self._hash_code(str(key))

        if self.__map[hash_value].key == key:
            self.__map[hash_value].visible = False
            return True

        else:
            found = self.__map[hash_value]

            while found is not None and found.key != key:
                found = found.next

            if found is None:
                return False
            else:
                found.visible = False
                return True

    def delete(self, key: T) -> bool:

        if not self[key]:
            return False

        hash_value = self._hash_code(str(key))

        if self.__map[hash_value].key == key:
            self.__map[hash_value].visible = False
            return True

        else:
            found = self.__map[hash_value]

            while found is not None and found.key != key:
                found = found.next

            if found is None:
                return False
            else:
                found.visible = False
                return True

def add_item(map: HashTable()) -> None:
    for i in range (0, 10000):
        map.__add__(i, f"item{i}")


def get_item(map: HashTable()) -> None:
    for i in range (0, 10000):
        map.__getitem__(i)

def delete_item(map: HashTable()) -> None:
    for i in range(10000, 0):
        map.delete(i)

if __name__ == "__main__":
    map = HashTable()
    add_item(map)
    print(map)
    get_item(map)
    delete_item(map)