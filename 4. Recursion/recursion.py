def sum_integers(n):
    if n == 0:
        return 0
    return n + sum_integers(n - 1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def reverse_string(input):
    if not input:
        return ""
    return reverse_string(input[1:]) + input[0]


def is_palindrome(input):
    if len(input) == 0 or len(input) == 1:
        return True
    first_char = input[0]
    last_char = input[-1]
    return first_char == last_char and is_palindrome(input[1:-1])
