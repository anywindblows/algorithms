from typing import Any


class Queue:
    def __init__(self, queue_length: int):
        self.items = [None] * queue_length
        self.__queue_length = queue_length
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        """Determines if the queue is empty."""
        return self.size == 0

    def push(self, value: Any) -> None:
        """Add item to end of queue."""
        if self.size != self.__queue_length:
            self.items[self.tail] = value
            self.tail = (self.tail + 1) % self.__queue_length
            self.size += 1

    def pop(self) -> Any:
        """When extracting, the previously added element is removed."""
        if self.is_empty():
            return None
        pop_element = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.__queue_length
        self.size -= 1
        return pop_element


def main():
    queue = Queue(queue_length=5)
    queue.push('value')
    queue.pop()
    queue.push('new_value')
    print(queue.items)


if __name__ == '__main__':
    main()
