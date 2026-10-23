def count_comparisons_linear_search(arr, target):
    """
    arr: a list of numbers
    target: the number to search for

    Returns:
        A tuple (found, comparisons), where found is a bool indicating if 
        the target was found, and comparisons is the exact count of 
        element-to-target comparisons performed.
    """
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return (True, comparisons)
    return (False, comparisons)


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers sorted in ascending order
    target: the number to search for

    Returns:
        A tuple (found, comparisons), where found is a bool indicating if 
        the target was found, and comparisons is the exact count of 
        element-to-target comparisons performed while halving the search space.
    """
    comparisons = 0
    lo = 0
    hi = len(sorted_arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        
        if sorted_arr[mid] == target:
            return (True, comparisons)
        elif sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return (False, comparisons)
