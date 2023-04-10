def zip(keys: list[str], values: list[int]) -> dict[str,int]:
    """produces a dictionary with items of the first list and the corresponding items at the same index of the second list"""
    dictionary = {}

    if (len(keys) != len(values)) or (len(keys) == 0) or (len(values) == 0):
        return dictionary
    
    for those in range(len(keys)):
        dictionary[keys[those]] = values[those]

    return dictionary