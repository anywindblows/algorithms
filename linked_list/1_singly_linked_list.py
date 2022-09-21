from typing import Any


class LinkedList:
    class Node:
        def __init__(self, value: Any):
            self.value = value
            self.next_value = None

        def __str__(self) -> str:
            return str(self.value)

    head: Node = None

    def append(self, element: Any) -> Node:
        """Adds an element to the end of the list."""
        element = self.Node(value=element)

        if not self.head:
            self.head = element
            return element

        for node in self:
            if not node.next_value:
                node.next_value = element
        return element

    def __len__(self) -> int:
        length: int = 0
        for _ in self:
            length += 1
        return length

    def __iter__(self) -> 'LinkedList':
        self.next = self.head
        return self

    def __next__(self) -> Node:
        current = self.next
        if current:
            self.next = current.next_value
            return current
        else:
            raise StopIteration

    def __str__(self) -> str:
        string = '['
        for index, element in enumerate(self):
            if index == 0:
                string += str(element)
                continue
            string += f', {element}'
        string += ']'
        return string


def main() -> None:
    linked_list = LinkedList()

    for element in range(10):
        linked_list.append(element)

    print(len(linked_list))
    print(linked_list)


if __name__ == '__main__':
    main()
