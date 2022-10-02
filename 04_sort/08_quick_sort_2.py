def partition(array: list, pivot: int) -> tuple[list, list, list]:
    left, center, right = [], [], []

    for i in array:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            center.append(i)
        else:
            right.append(i)

    return left, center, right


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array

    pivot = array[len(array) // 2]
    left, center, right = partition(array, pivot)
    return quick_sort(left) + center + quick_sort(right)


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(quick_sort(unsorted_array))


if __name__ == '__main__':
    main()
