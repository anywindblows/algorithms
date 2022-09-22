from typing import Any


class LinkedList:
    class Node:
        def __init__(self, value: Any):
            self.value = value
            self.prev_value = None
            self.next_value = None

        def __str__(self) -> str:
            return str(self.value)

    __head: Node = None

    def append(self, element: Any) -> Node:
        """Adds an element to the end of the list."""
        element = self.Node(value=element)

        if not self.__head:
            self.__head = element
            return element

        for node in self:
            if not node.next_value:
                node.next_value = element
                element.prev_value = node

        return element

    def get(self, index: int) -> Node:
        """Gets an element by its index."""
        if not isinstance(index, int):
            raise ValueError('index must be "int" type')
        for idx, value in enumerate(self):
            if idx == index:
                return value
            continue
        raise IndexError('list index out of range')

    def insert_after(self, index: int, value: Any) -> Node:
        """Get element by index and inset value after."""
        element = self.Node(value=value)
        get_element = self.get(index=index)

        element.next_value = get_element.next_value
        element.prev_value = get_element
        get_element.next_value = element

        return element

    def __reversed__(self) -> 'LinkedList':
        """Reverse list."""
        prev = None
        current = self.__head

        while current:
            next_ = current.next_value
            current.next_value = prev
            prev = current
            current = next_
        self.__head = prev
        return self

    def __len__(self) -> int:
        """Return list length."""
        length: int = 0
        for _ in self:
            length += 1
        return length

    def __iter__(self) -> 'LinkedList':
        self.next = self.__head
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

    linked_list.insert_after(index=0, value='insert_after')

    print(linked_list)
    print(len(linked_list))
    print(reversed(linked_list))
    print(linked_list.get(index=0))


if __name__ == '__main__':
    main()
