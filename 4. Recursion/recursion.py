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


def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
    num_list = list(str(num))
    if len(num_list) == 1:
        chars = get_characters(int(num_list[0]))
        if len(chars) == 0:
            return [""]
        return list(get_characters(int(num_list[0])))

    current_str_arr = keypad(int("".join(num_list[1:])))
    chars_in_num = list(get_characters(int(num_list[0])))

    str_arr = []

    for i in current_str_arr:
        for j in chars_in_num:
            str_arr.append(j + i)

    return str_arr


def deep_reverse(l):
    for index, i in enumerate(l):
        if type(i) == list:
            l[index] = deep_reverse(i)
    l.reverse()
    return l


def print_integers(n):
    if (n == 0):
        return
    print(n)
    print_integers(n - 1)


def subsets(arr):
    if len(arr) == 0:
        return [[]]  # returns : [["element"]]

    result = subsets(arr[1:])  # contains : [["element"]]
    output = []
    element = arr[0]
    for i in result:
        output.append([element] + i)
    output.extend(result)

    return output


def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n - 1) + (n - 1)


def last_index_sol(arr, target, i):
    if len(arr) == i:
        return -1
    index = last_index_sol(arr, target, i + 1)
    if arr[i] == target and index is -1:
        return i
    return index


def last_index(arr, target):
    return last_index_sol(arr, target, 0)


print(last_index([1, 2, 3, 1], 4))
