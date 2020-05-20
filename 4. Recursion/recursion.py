def sum_integers(n):
    if n == 0:
        return 0
    return n + sum_integers(n - 1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
