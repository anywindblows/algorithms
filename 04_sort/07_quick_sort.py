def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    left = list(filter(lambda x: x < pivot, array))
    center = [x for x in array if x == pivot]
    right = list(filter(lambda x: x > pivot, array))

    return quick_sort(left) + center + quick_sort(right)


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(quick_sort(unsorted_array))


if __name__ == '__main__':
    main()
