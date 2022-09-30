def comb_sort(array: list) -> list:
    swapped = True
    shrink_factor: float = 1.247
    gaps = len(array)

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_factor)
        swapped = False
        i = 0
        while gaps + i < len(array):
            if array[i] > array[i + gaps]:
                array[i], array[i + gaps] = array[i + gaps], array[i]
                swapped = True
            i += 1

    return array


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(comb_sort(unsorted_array))


if __name__ == '__main__':
    main()
