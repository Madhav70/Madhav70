def is_subset(a, b):
    """
    a, b: Python sets

    Returns:
        True if every element of a is also in b (a is a subset of b,
        written a subseteq b), False otherwise.
    """
    return a <= b


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    best_index = 0
    best_value = values[0]
    
    for i in range(1, len(values)):
        if values[i] > best_value:
            best_value = values[i]
            best_index = i
            
    return best_index
