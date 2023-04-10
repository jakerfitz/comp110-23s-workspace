"""EX04_Utils to demonstrate many functions with pop and various while loops."""

__author__ = "730474841"


def all(numbers: list[int], num: int) -> bool:
    """Outputs if a # is the same as all other #s in list."""
    if len(numbers) == 0:
        return False
    while len(numbers) > 0:
        if (numbers.pop() != num):
            return False
    return True


def max(input: list[int]) -> int:
    """Returns the largest int in the list."""
    if len(input) == 0:
        raise ValueError("Max() arg is an empty list")
    max_value: int = input[0]
    idx: int = 0
    while (idx < len(input)):
        if input[idx] > max_value:
            max_value = input[idx]
        idx += 1
    return max_value


def is_equal(numlist1: list[int], numlist2: list[int]) -> bool:
    """Returns if lists are equal to one another."""
    idx: int = 0
    if len(numlist1) != len(numlist2):
        return False
    while idx < len(numlist1):
        if (numlist1.pop() != numlist2.pop()):
            return False
        idx += 1
    return True
