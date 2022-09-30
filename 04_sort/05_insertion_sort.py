def insertion_sort(array: list) -> list:
    for i in range(len(array)-1):
        temp = array[i]
        j = i - 1
        while j >= 0 and temp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp
    return array


def main():
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(insertion_sort(unsorted_array))


if __name__ == '__main__':
    main()
