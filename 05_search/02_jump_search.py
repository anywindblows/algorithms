from math import sqrt
from typing import Any


def jump_search(array: list, element: Any) -> Any:
    length = len(array)
    jump = int(sqrt(length))
    left, right = 0, 0

    while left < length and array[left] <= element:
        right = min(length - 1, left + jump)
        if array[left] <= element <= array[right]:
            break
        left += jump
    if left >= length or array[left] > element:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and array[i] <= element:
        if array[i] == element:
            return i
        i += 1
    return -1


def main() -> None:
    sorted_array = [1, 2, 3, 5, 7, 8, 11, 33, 88, 222, 883]
    search_element = 33
    print(jump_search(sorted_array, search_element))


if __name__ == '__main__':
    main()
