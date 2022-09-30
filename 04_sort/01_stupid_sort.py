def stupid_sort(array: list) -> list:
    counter: int = 0
    while counter < len(array)-1:
        if array[counter] > array[counter+1]:
            array[counter], array[counter+1] = array[counter+1], array[counter]
            counter = 0
        else:
            counter += 1
    return array


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(stupid_sort(unsorted_array))


if __name__ == '__main__':
    main()
