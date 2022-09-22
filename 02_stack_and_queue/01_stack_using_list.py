from typing import Any


class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item: Any) -> None:
        """Add item to end of stack."""
        self.items.append(item)

    def pop(self) -> Any:
        """Delete last item in stack and return it."""
        return self.items.pop()

    def peek(self) -> Any:
        """Return last stack item."""
        return self.items[-1]

    def size(self) -> int:
        """Return stack size."""
        return len(self.items)


def main() -> None:
    stack = Stack()
    for element in range(10):
        stack.push(element)

    print(stack.pop())
    print(stack.peek())
    print(stack.size())


if __name__ == '__main__':
    main()
