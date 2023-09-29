from enum import Enum
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable

T = TypeVar('T')

class IndexOutOfBoundException(Exception):
    pass

@dataclass
class Cat:
    """
        Пример обычной модели данных
        Args:
            :arg name: (str) - имя
            :arg age(int) - возраст

    """
    name: str
    age: int
    """
        Строковое представление модели
    """
    def __str__(self):
        return f"Cat[{self.name}, {self.age}]"


class Direction(Enum):
    """
        Перечисление направления сдвига
        Args:
            :var FORWARD - указание, на перемещёние вперёд (вправо)
            :var BACKWARD - указание, на перемещёние назад (влево)
    """
    FORWARD = 'forward'
    BACKWARD = 'backward'


@dataclass
class Node(Generic[T]):
    """
       Узел списка
       Args:
           :arg data(T) - данные, хранящиеся в узле
           :arg next_ptr(T) - указатель на следующий элемент в списке
           :arg prev_ptr(T) - указатель на предыдущий элемент в списке

   """
    data: T
    next_ptr: Optional['Node[T]'] = None
    prev_ptr: Optional['Node[T]'] = None



class LinkedList(Generic[T]):
    """
    Реализация двусвязного списка
    Args:
        :arg _length(int) - размер списка
        :arg _head(Optional['Node[T]']) - указатель на первый элемент (head, голову)
        :arg _tail(Optional['Node[T]']) - указатель на последний элемент (tail, хвост)

    """
    def __init__(self):
        self._length: int = 0
        self._head: Optional['Node[T]'] = None
        self._tail: Optional['Node[T]'] = None

    """
        Получение длины списка
    """
    def get_size(self) -> int:
        return self._length

    """
            Проверка наличия индекса в списке
            :param index(int) - искомый индекс
            :return bool - находится ли индекс в списке

            Если индекс больше или равен длине или он меньше нуля, то возвращаем False, иначе True
        """
    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    """
        Проверка на пустоту списка. Если длина равно нулю, то список пустой
    """

    def is_empty(self) -> bool:
        return self._length == 0

    """
        Добавление элемента в конец списка
    
        Args:
            :param data(T) - Значение ноды
        
        Если длина списка 0, т е это первый элемент, то он же и является и головой и хвостом,
        поэтому просто записываем значение в ноду и сохраняем, увеличив длинну списка
        Иначе делаем разрыв с сохранением ссылок
        В ссылку на следующий элемент ставим нашу ноду, на предыдущий ставим нынешний хвост, 
        а потом в хвост ставим ноду
    """

    def push_tail(self, data: T) -> None:
        node = Node[T](data)
        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return
        self._tail.next_ptr = node
        node.prev_ptr = self._tail
        self._tail = node
        self._length += 1

    """
        Добавление элемента в конец списка
        
        Args:
            :param data(T) - Значение ноды

        Если длина списка 0, т е это первый элемент, то он же и является и головой и хвостом,
        поэтому просто записываем значение в ноду и сохраняем, увеличив длинну списка
        Иначе делаем разрыв с сохранением ссылок
        В ссылку на следующий элемент ставим текущую голову, в текущей голове ссылаемся назад на ноду и подменяем голову
        
    """

    def push_head(self, data: T) -> None:
        node = Node[T](data)

        if self._length <= 0:
            self._head = node
            self._tail = node
            self._length += 1
            return

        node.next_ptr = self._head
        self._head.prev_ptr = node
        self._head = node
        self._length += 1

    """
        Добавление элемента в список по индексу и без
    
        Args:
            :param data(T) - Значение ноды
            :param index(int) - индекс элемента
    
        Если длина списка больше нуля, тогда проверяем есть ли индекс в списке, при неудаче кидаем ошибку
        Далее если нам указали нулевой индекс или не указали вовсе, считаем, что это вставка в голову, 
        поэтому вызываем соответствующую функцию
        
        Если указан крайний индекс, то это равноценно вставке в хвост,
        поэтому вызываем соответствующую функцию
        
        Иначе запускаем цикл, поке не найдём ноду с необходимым индексом
        Сохраняем ноду для вставки, ставим ей ссылку на некст ноду найдённой ноде, 
        ставим предшествующей ноде, ссылку на следующую ноду на ту, что будем вставлять
        ставим вставляемой ноде ссылку на предыдущую ноду как в ноде, которую мы заменили
        и в той ноде, что мы заменили по индексу ставим ссылку на предыдущую ноду вставляемую ноду
    """
    def __add__(self, data: T, index: int = 0) -> None:
        if self._length > 0:
            ok: bool = self._check_range(index)
            if not ok:
                raise IndexOutOfBoundException("-")

        if index == 0:
            self.push_head(data)
            return
        elif index == self._length - 1:
            self.push_tail(data)
            return

        node = self._head
        for i in range(0, index):
            node = node.next_ptr

        insert_node = Node[T](data)
        insert_node.next_ptr = node
        node.prev_ptr.next_ptr = insert_node
        insert_node.prev_ptr = node.prev_ptr
        node.prev_ptr = insert_node
        self._length += 1

    """
        Нахождение элемента по индексу

        Args:
            :param index(int) - индекс элемента

        Если длина списка больше нуля, тогда проверяем есть ли индекс в списке, при неудаче кидаем ошибку

        Если указан крайний индекс, то это равноценно голове или хвосту,
        поэтому вызываем соответствующие функции и возвращаем их результат

        Иначе запускаем цикл, поке не найдём ноду с необходимым индексом
        и возвращаем результат
    """
    def __getitem__(self, index: int) -> T:

        if not self._check_range(index):
            raise IndexOutOfBoundException("-")

        if index == 0:
            return self.head()
        elif index == self._length - 1:
            return self.tail()

        node = self._head
        for i in range(0, index):
            node = node.next_ptr
        return node.data

    """
        Перегрузка оператора in

        Args:
            :param item(T) - элемент

        Запускается цикл, поке не найдём ноду с необходимым индексом
        Если такая нода найдена - True, иначе - False
    """

    def __contains__(self, item: T) -> bool:
        node = self._head
        for i in range(0, self._length):
            if node.data == self.__getitem__(i):
                return True
            node = node.next_ptr
        return False

    """
        Удаление элемента по индексу

        Args:
            :param key(int) - index 


        Если длина списка больше 0, метод проверяет, находится ли указанный индекс в допустимом диапазоне. 
        Если нет, он вызывает исключение IndexOutOfBoundException.
        
        Если ключ равен 0, метод удаляет первый элемент списка. Если после удаления список становится пустым, метод обнуляет head и tail и возвращает True.
        
        Если ключ не равен 0, метод проходит по списку до элемента, предшествующего элементу, который нужно удалить.
        
        Если ключ равен self._length - 1, метод удаляет последний элемент списка.
        
        В противном случае метод удаляет элемент из середины списка.
        
        В конце метод уменьшает длину списка на 1 и возвращает True.
    """

    def __delitem__(self, key: int = 0) -> bool:

        if self._length > 0:
            if not self._check_range(key):
                raise IndexOutOfBoundException("-")

        if key == 0:
            node = self._head
            if node.next_ptr is None:
                self._length: int = 0
                self._head: Optional['Node[T]'] = None
                self._tail: Optional['Node[T]'] = None
                return True
            self._head = node.next_ptr
            self._head.prev_ptr = None
            del node
            self._length -= 1
            return True

        node = self._head
        for i in range(0, key - 1):
            node = node.next_ptr

        if key == self._length - 1:
            self._tail.prev_ptr = None
            self._tail = node
            self._tail.next_ptr = None
            self._length -= 1
            return True

        delete_node = node.next_ptr
        node.next_ptr = delete_node.next_ptr
        node.next_ptr.prev_ptr = delete_node.prev_ptr
        self._length -= 1
        return True

    """
        Метод применяет функцию func к каждому элементу в списке, начиная с головы списка и двигаясь вперед.  
        :param func: Callable[[T], None] = передаваемая фукнция  
    """
    def for_each(self, func: Callable[[T], None]) -> None:
        if self._head is not None:
            node = self._head
            func(node.data)
            while node.next_ptr is not None:
                node = node.next_ptr
                func(node.data)

    """
        Метод применяет функцию func к каждому элементу в списке, начиная с хвоста списка и двигаясь назад.
        :param func: Callable[[T], None] = передаваемая фукнция
    """
    def reverse_for_each(self, func: Callable[[T], None]) -> None:
        if self._tail is not None:
            node = self._tail
            func(node.data)
            while node.next_ptr is not None:
                node = node.next_ptr
                func(node.data)

    """
        Метод циклически сдвигает элементы списка на n позиций в указанном направлении. 
        Если n равно 0, список пуст или n кратно длине списка, метод ничего не делает и возвращает управление. 
        Если n отрицательное число, метод меняет направление сдвига и делает n положительным числом. 
        Затем метод выполняет сдвиг, добавляя элементы в начало или конец списка и удаляя их из противоположного конца.
        Args:
            :param direction: Direction - перечисление, определяет в какую сторону надо сдвигать элементы
            :param n: int - шаги сдивига
        
    """

    def shift(self, direction: Direction, n: int) -> None:

        if n == 0 or self.is_empty() or n % self._length == 0:
            return

        if direction == Direction.FORWARD and n < 0:
            direction = Direction.BACKWARD
            n = abs(n)
        elif direction == Direction.BACKWARD and n < 0:
            direction = Direction.FORWARD
            n = abs(n)

        match direction:
            case Direction.FORWARD:
                for i in range(0, n):
                    self.push_head(self._tail.data)
                    self.__delitem__(self._length - 1)
                return
            case Direction.BACKWARD:
                for i in range(0, n):
                    self.push_tail(self._head.data)
                    self.__delitem__(0)
                return

    """
        Метод возвращает строковое представление списка. Он проходит по всему списку и добавляет данные каждого узла в строку.
    """
    def __str__(self) -> str:
        node = self._head
        list_str = "List[ "
        if self._head is not None:
            for i in range(0, self._length):
                list_str += f"{node.data} "
                node = node.next_ptr
        list_str += "]"
        return list_str

    """
        Метод возвращает данные головного узла списка.
    """
    def head(self) -> T:
        return self._head.data

    """
        Метод возвращает данные хвостового узла списка.
    """
    def tail(self) -> T:
        return self._tail.data


def add_item(llist: LinkedList[Cat]()) -> None:
    llist.__add__(Cat(f"Max{1}", 7 + 1))
    llist.__add__(Cat(f"Max{1}", 7 + 1))
    llist.__add__(Cat(f"Max{1}", 7 + 1))
    for i in range (0, 10000):
        llist.__add__(Cat(f"Max{i}", 7 + i), int(llist.get_size()/2))

def add_item_to_head(llist: LinkedList[Cat]()) -> None:
    for i in range (0, 10000):
        llist.__add__(Cat(f"Max{i}", 7 + i), i)

def get_item(llist: LinkedList[Cat]()) -> None:
    for i in range (0, 10000):
        llist.__getitem__(i)

def delete_item(llist: LinkedList[Cat]()) -> None:
    for i in range (10000, 0):
        llist.__delitem__(i)


def shift_list(llist: LinkedList[Cat]()) -> None:
    for i in range (0, 10000):
        llist.shift(Direction.FORWARD, 2)

if __name__ == "__main__":
    linked_list = LinkedList[Cat]()

    add_item(linked_list)
    get_item(linked_list)
    shift_list(linked_list)
    delete_item(linked_list)
    add_item_to_head(linked_list)


    print(linked_list)