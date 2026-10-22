
def summation(f, lo, hi):
    total = 0

    for i in range(lo, hi + 1):
        total = total + f(i)

    return total
