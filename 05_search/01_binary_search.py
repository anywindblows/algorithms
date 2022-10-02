from typing import Any


def binary_search(array: list, left: int, right: int, element: Any) -> Any:
    if len(array) == 1:
        return array[0]

    mid = (left+right) // 2

    if array[mid] == element:
        return mid

    if array[mid] < element:
        return binary_search(array, mid+1, right, element)
    else:
        return binary_search(array, left, mid, element)


def main() -> None:
    sorted_array = [1, 2, 3, 5, 7, 8, 11, 33, 88, 222, 883]
    search_element = 33
    print(binary_search(sorted_array, 0, len(sorted_array), search_element))


if __name__ == '__main__':
    main()
