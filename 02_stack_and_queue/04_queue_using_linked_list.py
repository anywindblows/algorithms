from typing import Any


class Queue:
    class Node:
        def __init__(self, value: Any) -> None:
            self.value = value
            self.next_value = None

        def __str__(self) -> str:
            return str(self.value)

    head: Node = None

    def push(self, item: Any) -> Node:
        """Add item to end of queue."""
        item = self.Node(value=item)

        if not self.head:
            self.head = item
            return item
        for node in self:
            if not node.next_value:
                node.next_value = item
        return item

    def pop(self) -> Node:
        """Delete and return first item in queue."""
        if self.head:
            queue_head = self.head
            self.head = self.head.next_value
            return queue_head
        raise IndexError('pop from empty list')

    def peek(self) -> Node:
        """Return fist element in queue."""
        if self.head:
            return self.head
        raise IndexError('list index out of range')

    def size(self) -> int:
        """Return queue size."""
        length: int = 0
        for _ in self:
            length += 1
        return length

    def __iter__(self):
        self.next = self.head
        return self

    def __next__(self):
        current = self.next

        if current:
            self.next = current.next_value
            return current
        else:
            raise StopIteration


def main():
    queue = Queue()
    for element in range(10):
        queue.push(element)

    print(queue.pop())
    print(queue.peek())
    print(queue.size())


if __name__ == '__main__':
    main()
