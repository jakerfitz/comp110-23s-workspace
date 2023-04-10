"""3x unit test functions."""

__author__ = "730474841"

from exercises.ex05.utils import only_evens, sub, concat

def test_only_evens_edge():
    """Tests for an edge case in the only_evens function"""
    assert only_evens([1, 5, 3]) == []
def test_only_evens_use1():
    """Tests for a use case in the only_evens function"""
    assert only_evens([1, 2, 3]) == [2]
def test_only_evens_use2():
    """Tests for a use case in the only_evens function"""
    assert only_evens([4, 4, 4]) == [4, 4, 4]
def test_sub_edge():
    """Tests for an edge case in the sub function"""
    assert sub([], 0, 1) == []
def test_sub_use1():
    """Tests for a use case in the sub function"""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]
def test_sub_use2():
    """Tests for a use case in the sub function"""
    assert sub([5], -1, -1) == []
def test_concat_edge():
    """Tests for an edge case in the concat function"""
    assert concat([], []) == []
def test_concat_use1():
    """Tests for a use case in the concat function"""
    assert concat([1], [2]) == [1, 2]
def test_concat_use2():
    """Tests for a use case in the concat function"""
    assert concat([], [5]) == [5]