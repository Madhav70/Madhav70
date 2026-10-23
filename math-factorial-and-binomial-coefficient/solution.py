def factorial(n):
    """
    n: a non-negative integer

    Returns:
        n! = n * (n-1) * ... * 1, the product of every integer from 1 to
        n. factorial(0) is 1 (the empty-product convention).
    """
    total = 1 
    # Start range at 1 so we don't multiply by 0
    for i in range(1, n + 1):
        total = total * i
    return total


def n_choose_k(n, k):
    if k < 0 or k > n:
        return 0
    
    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    
    # Return the integer division directly
    return numerator // denominator


def sum_of_combinations(n):
    total = 0
    for i in range(n + 1):
        total = n_choose_k(n, i) + total
    return total
