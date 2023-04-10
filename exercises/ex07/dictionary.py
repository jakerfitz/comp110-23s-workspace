"""Coninued integration of writing for unit tests: invert, favorite_color, and count."""

__author__ = "730474841"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Makes the key and value inverted."""
    output: dict[str, str] = {}
    for key in input:
        value = input[key]
        if value in output:
            raise KeyError(f"{value} has already been entered!")
        output[value] = key
    return output


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds the common favorite color."""
    color_count: dict[str, str] = {}
    for name in color_dict:
        color = color_dict[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    max_num_color: int = 0
    common_color: str = ""

    for color in color_count:
        num_counter: int = 0
        if color_count[color] > num_counter:
            count = color_count[color]
            if count > max_num_color:
                max_num_color = count
                common_color = color
    return common_color


def count(rand_list: list[str]) -> dict[str, int]:
    """Creates dict based on number of times a given key value is found in a given list."""
    final_d: dict[str, int] = {}
    for vals in rand_list:
        if vals in final_d:
            final_d[vals] += 1
        else:
            final_d[vals] = 1
    return final_d