from typing import Any


class Deque:
    def __init__(self):
        self.items = list()

    def size(self) -> int:
        """Return deque size."""
        return len(self.items)

    def push_back(self, item: Any) -> None:
        """Add item to end of deque."""
        self.items.append(item)

    def pop_back(self) -> None:
        """Remove item from end of deque."""
        self.items.pop(-1)

    def push_front(self, item: Any) -> None:
        """Add item to head of deque."""
        self.items.insert(0, item)

    def pop_front(self) -> None:
        """Remove item from head of deque."""
        self.items.pop(0)


def main():
    deque = Deque()
    deque.push_back('value')
    deque.pop_back()
    deque.push_front('value')
    deque.pop_front()
    print(deque.items)


if __name__ == '__main__':
    main()
