def finder(input1: dict[str, int]) -> list[int]:
    list1: list[str]
    for i in input1:
        if (input1[i] % 2 == 0) and (input[i] < 18):
            list1.append(i)
    return list1