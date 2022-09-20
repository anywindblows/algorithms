class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next_value = None

        def __str__(self):
            return str(self.value)

    head: Node = None

    def append(self, element) -> Node:
        """Adds an element to the end of the list."""
        element = self.Node(value=element)
        if not self.head:
            self.head = element
            return element

        end = self.head
        while end.next_value:
            end = end.next_value
        end.next_value = element
        return element

    def __len__(self):
        length = 0
        if not self.head:
            return length

        while self.head.next_value:
            length += 1
            self.head = self.head.next_value
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


def main() -> None:
    linked_list = LinkedList()

    for element in range(10):
        linked_list.append(element)

    for elements in linked_list:
        print(elements)


if __name__ == '__main__':
    main()
