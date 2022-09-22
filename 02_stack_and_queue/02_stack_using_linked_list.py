from typing import Any


class Stack:
    class Node:
        def __init__(self, value: Any):
            self.value = value
            self.next_value = None

        def __str__(self) -> str:
            return str(self.value)

    head: Node = None

    def push(self, item: Any) -> Node:
        """Add item to end of stack."""
        item = self.Node(value=item)

        if not self.head:
            self.head = item
            return item
        for node in self:
            if not node.next_value:
                node.next_value = item
        return item

    def pop(self) -> Node:
        """Delete last item in stack and return it."""
        prev_value = None
        for node in self:
            if node.next_value:
                prev_value = node
        pop_value = prev_value.next_value
        prev_value.next_value = None
        return pop_value

    def peek(self) -> Node:
        """Return last stack item."""
        for node in self:
            if not node.next_value:
                return node

    def size(self) -> int:
        """Return stack size."""
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
    stack = Stack()
    for element in range(10):
        stack.push(element)

    print(stack.pop())
    print(stack.peek())
    print(stack.size())


if __name__ == '__main__':
    main()
