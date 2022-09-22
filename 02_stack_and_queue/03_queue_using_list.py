from typing import Any


class Queue:
    def __init__(self):
        self.items = list()

    def push(self, item: Any) -> None:
        """Add item to end of queue."""
        self.items.append(item)

    def pop(self) -> None:
        """Delete and return first item in queue."""
        if self.items:
            queue_head = self.items[0]
            self.items.pop(0)
            return queue_head
        raise IndexError('pop from empty list')

    def peek(self) -> Any:
        """Return fist element in queue."""
        if self.items:
            return self.items[0]
        raise IndexError('list index out of range')

    def size(self) -> int:
        """Return queue size."""
        return len(self.items)


def main():
    queue = Queue()
    for element in range(10):
        queue.push(element)

    print(queue.pop())
    print(queue.peek())
    print(queue.size())


if __name__ == '__main__':
    main()
