def iter_merge(array_one: list, array_two: list) -> list:
    merged_list, it1, it2 = list(), iter(array_one), iter(array_two)
    el1, el2 = next(it1, None), next(it2, None)
    while el1 is not None or el2 is not None:
        if el1 is None or (el2 is not None and el2 < el1):
            merged_list.append(el2)
            el2 = next(it2, None)
        else:
            merged_list.append(el1)
            el1 = next(it1, None)

    return merged_list


def main() -> None:
    list_one = [1, 3, 8, 9, 11]
    list_two = [2, 4, 8, 12, 15]
    print(iter_merge(list_one, list_two))


if __name__ == '__main__':
    main()
