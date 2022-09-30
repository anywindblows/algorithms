def cocktail_sort(array: list) -> list:
    swapped = True
    start = 0
    end = len(array) - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        end -= 1

        if not swapped:
            break
        swapped = False

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start += 1

    return array


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(cocktail_sort(unsorted_array))


if __name__ == '__main__':
    main()
