"""Unit tests for the dictionary function."""

__author__ = "730474841"

from dictionary import invert, favorite_color, count


def test_invert_edge_case():
    """Tests for an edge case in the invert function."""
    assert invert({}) == {}
    

def test_invert_use_case1():
    """Tests for a use case in the invert function."""
    assert invert({"a": "z", "j": "f"}) == {"z": "a", "f": "j"}


def test_invert_use_case2():
    """Tests for a use case in the invert function."""
    assert invert({"Mike": "Randy", "Jack": "Boyles"}) == {"Boyles": "Jack", "Randy": "Mike"}


def test_favorite_color_edge_case():
    """Tests for an edge case in the favorite_color function."""
    assert favorite_color({}) == ""


def test_favorite_color_use_case1():
    """Tests for a use case in the favorite_color function."""
    assert favorite_color({"Landon": "red", "Rick": "blue", "Charles": "red"}) == "red"


def test_favorite_color_use_case2():
    """Tests for a use case in the favorite_color function."""
    assert favorite_color({"Robin": "green", "Jerry": "blue", "Chuck": "green", "Norris": "blue"}) == "green"


def test_count_edge_case():
    """Tests for an edge case in the count function."""
    assert count([]) == {}


def test_count_use_case1():
    """Tests for a use case in the count function."""
    assert count(["a", "b", "c", "a", "a"]) == {"a": 3, "b": 1, "c": 1}


def test_count_use_case2():
    """Tests for a use case in the count function."""
    assert count(["Mark", "Randy", "Michael", "Mark"]) == {"Mark": 2, "Michael": 1, "Randy": 1}