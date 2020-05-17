class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackUsingArray:
    def __init__(self, initial_size=10):
        self.arr = [0] * initial_size
        self.next_index = 0
        self.num_elements = 0

    def push(self, item):
        if self.next_index == len(self.arr):
            self.__handle_stack_capacity_full()

        self.arr[self.next_index] = item
        self.next_index += 1
        self.num_elements += 1

    def __handle_stack_capacity_full(self):
        new_arr = [0] * (2 * len(self.arr))

        for index, item in enumerate(self.arr):
            new_arr[index] = item

        self.arr = new_arr

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None

        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.num_elements += 1

    def is_empty(self):
        return self.head == None

    def size(self):
        return self.num_elements

    def pop(self):
        if self.is_empty():
            return None
        node = self.head
        self.head = self.head.next
        self.num_elements -= 1
        return node.value

    def peek(self):
        if self.head == None:
            return None
        return self.head.value


def equation_checker(equation):
    stack = Stack()

    for i in equation:
        if i == '(':
            stack.push()
        elif i == ')':
            if stack.pop() == None:
                return False

    return stack.is_empty()
