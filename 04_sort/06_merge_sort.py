def merge_list(array_one: list, array_two: list) -> list:
    merged_list = list()
    i, j = 0, 0
    while i < len(array_one) and j < len(array_two):
        if array_one[i] < array_two[j]:
            merged_list.append(array_one[i])
            i += 1
        else:
            merged_list.append(array_two[j])
            j += 1
    merged_list += array_one[i:]
    merged_list += array_two[j:]

    return merged_list


def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array
    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge_list(left, right)


def main() -> None:
    unsorted_array = [0, 17, 3, 1, 22, 7, 9, 4, 5, 8, 11]
    print(merge_sort(unsorted_array))


if __name__ == '__main__':
    main()
