def simple_merge(array_one: list, array_two: list) -> list:
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


def main() -> None:
    list_one = [1, 3, 8, 9, 11]
    list_two = [2, 4, 8, 12, 15]
    print(simple_merge(list_one, list_two))


if __name__ == '__main__':
    main()
