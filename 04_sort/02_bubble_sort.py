def bubble_sort(array: list) -> list:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    return array


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(bubble_sort(unsorted_array))


if __name__ == '__main__':
    main()
