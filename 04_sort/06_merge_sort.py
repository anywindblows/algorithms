def merge_sort(array: list) -> list:
    if len(array) == 1:
        return array
    pass


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(merge_sort(unsorted_array))


if __name__ == '__main__':
    main()
