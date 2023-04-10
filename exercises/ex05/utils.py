"""Furthering the list utility functions: practice writing unit tests for functions."""

__author__ = "730474841"


def only_evens(input: list[int]) -> list[int]:
    """Returns the even int(s) in the list."""
    result = []
    for num in input:
        if (num % 2 == 0):
            result.append(num)
    return result


def concat(numlist1: list[int], numlist2: list[int]) -> list[int]:
    """Generates a full list of all elements in first then second list."""
    full_list = []
    for num in numlist1:
        full_list.append(num)
    for num in numlist2:
        full_list.append(num)
    return full_list


def sub(numlist: list[int], start: int, end: int) -> list[int]:
    """Generates a subset list of a given list."""
    if start < 0:
        start = 0
    if (end > (len(numlist))):
        end = len(numlist)
    if (len(numlist) == 0) or (start >= end):
        return []
    sublist = []
    for num in range(start, end):
        sublist.append(numlist[num])
    return sublist