import copy


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


def add_one(input):
    if len(input) == 1:
        new_num = input[0] + 1
        if new_num > 9:
            return [new_num // 10, new_num % 10]
        else:
            return [new_num]

    new_arr = add_one(input[1:])
    if len(new_arr) == len(input):
        new_num = new_arr[0] + input[0]
        return [new_num // 10, new_num % 10] + new_arr[1:]
    return [input[0]] + new_arr


def permute(input):
    if len(input) <= 1:
        return [input]  # Returns[[element]]

    result = permute(input[1:])
    element = input[0]
    new_arr = []
    for index, j in enumerate(result):
        sub_arr = []
        for i in range(len(result[0]) + 1):
            copied_arr = copy.deepcopy(j)
            copied_arr.insert(i, element)
            sub_arr.append(copied_arr)
        new_arr += sub_arr
    return new_arr


def permutations(input):
    if len(input) <= 1:
        return [input[0]]  # Returns[element]

    result = permutations(input[1:])  # Contains => [str, str, ...]
    element = input[0]
    new_arr = []
    for index, j in enumerate(result):
        sub_arr = []
        for i in range(len(result[0]) + 1):
            sub_arr.append(j[0:i] + element + j[i:])
        new_arr += sub_arr
    return new_arr
