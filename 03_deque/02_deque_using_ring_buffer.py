from typing import Any


class Deque:
    def __init__(self, deque_length: int):
        self.items = [None] * deque_length
        self.__deque_length = deque_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        """Determines if the queue is empty."""
        return self.size == 0

    def push_back(self, value: Any) -> None:
        """Add item to end of deque."""
        if self.size != self.__deque_length:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.__deque_length
            self.size += 1
        else:
            raise OverflowError

    def pop_back(self) -> Any:
        """Remove item from end of deque."""
        if self.is_empty():
            raise IndexError
        item = self.items[self.tail - 1]
        self.items[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.__deque_length
        self.size -= 1
        return item

    def push_front(self, value: Any) -> None:
        """Add item to head of deque."""
        if self.size != self.__deque_length:
            self.items[self.head - 1] = value
            self.head = (self.head - 1) % self.__deque_length
            self.size += 1
        else:
            raise OverflowError

    def pop_front(self) -> Any:
        """Remove item from head of deque."""
        if self.is_empty():
            raise IndexError
        item = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.__deque_length
        self.size -= 1
        return item


def main():
    deque = Deque(5)
    deque.push_back('value')
    deque.pop_back()
    deque.push_front('value')
    deque.pop_front()
    print(deque.items)


if __name__ == '__main__':
    main()
