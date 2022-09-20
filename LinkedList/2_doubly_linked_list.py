class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.prev_value = None
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
        element.prev_value = end
        return element

    def reverse(self) -> None:
        """Reverse list."""
        prev = None
        current = self.head

        while current:
            next_ = current.next_value
            current.next_value = prev
            prev = current
            current = next_
        self.head = prev

    def get(self, index):
        """Gets an element by its index."""
        element = self.head
        while index:
            if not element:
                raise IndexError('list index out of range')
            element = element.next_value
            index -= 1
        return element

    def insert_after(self, element, index):
        """Insert element after index elem."""
        element = self.Node(value=element)
        previous_element = self.get(index=index)
        element.next_value = previous_element.next_value
        previous_element.next_value = element
        return element

    def insert_before(self, element, index):
        """Insert element before index elem."""
        element = self.Node(value=element)
        next_element = self.get(index=index)
        previous_element = self.get(index=index-1)

        element.prev_value = next_element.prev_value
        element.next_value = next_element
        next_element.prev_value = element
        previous_element.next_value = element

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

    for element in range(1, 11):
        linked_list.append(element)

    for elements in linked_list:
        print(elements)


if __name__ == '__main__':
    main()
