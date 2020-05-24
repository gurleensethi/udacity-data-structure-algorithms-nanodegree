from collections import deque
from math import pow


class Node:

    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.right

    def set_right_child(self, node):
        self.right = node

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree:

    def __init__(self, value=None):
        self.root = None
        if value is not None:
            self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        return new_node.get_value() - node.get_value()

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            compare_result = self.compare(temp, new_node)
            if compare_result == 0:
                return
            elif compare_result > 0:
                if temp.get_right_child() == None:
                    temp.set_right_child(new_node)
                    break
                else:
                    temp = temp.get_right_child()
            else:
                if temp.get_left_child() == None:
                    temp.set_left_child(new_node)
                    break
                else:
                    temp = temp.get_left_child()

    def insert_with_recurssion_sol(self, node, new_node):
        if node is None:
            return new_node
        compare_result = self.compare(node, new_node)

        if compare_result == 0:
            return node
        elif compare_result > 0:
            node.set_right_child(self.insert_with_recurssion_sol(
                node.get_right_child(), new_node))
        else:
            node.set_left_child(self.insert_with_recurssion_sol(
                node.get_left_child(), new_node))

        return node

    def insert_with_recurssion(self, new_value):
        new_node = Node(new_value)
        self.root = self.insert_with_recurssion_sol(self.root, new_node)

    def search(self, value):
        temp = self.root

        while temp is not None:
            compare_result = temp.get_value() - temp.get_value()

            if compare_result == 0:
                return True
            elif compare_result > 0:
                temp = temp.get_right_child()
            else:
                temp = temp.get_left_child()

        return False

    def delete(self, value):
        to_delete = self.root
        prev = None

        while to_delete is not None:
            if to_delete.get_value() == value:
                break
            elif value - to_delete.get_value() > 0:
                prev = to_delete
                to_delete = to_delete.get_right_child()
            else:
                prev = to_delete
                to_delete = to_delete.get_left_child()

        if to_delete is None:
            return

        if to_delete.get_left_child() == None and to_delete.get_right_child() == None:
            if to_delete == self.root:
                self.root = None
                return

            if prev.get_left_child() == to_delete:
                prev.set_left_child(None)
            else:
                prev.set_right_child(None)
        elif to_delete.get_left_child() == None and to_delete.get_right_child() != None:
            if to_delete == self.root:
                self.root = to_delete.get_right_child()
                return

            if prev.get_left_child() == to_delete:
                prev.set_left_child(to_delete.get_right_child())
            else:
                prev.set_right_child(to_delete.get_right_child())
        elif to_delete.get_left_child() != None and to_delete.get_right_child() == None:
            if to_delete == self.root:
                self.root = to_delete.get_left_child()
                return

            if prev.get_left_child() == to_delete:
                prev.set_left_child(to_delete.get_left_child())
            else:
                prev.set_right_child(to_delete.get_left_child())

            if to_delete == self.root:
                self.root = prev
        else:
            prev_right_most = to_delete
            right_most = to_delete.get_left_child()
            while right_most.get_right_child() is not None:
                prev_right_most = right_most
                right_most = right_most.get_right_child()

            right_most.set_right_child(to_delete.get_right_child())

            if prev_right_most != to_delete:
                prev_right_most.set_right_child(right_most.get_left_child())
                right_most.set_left_child(to_delete.get_left_child())

            if prev == None:
                self.root = right_most
            else:
                if prev.get_left_child() == to_delete:
                    prev.set_left_child(right_most)
                else:
                    prev.set_right_child(right_most)


class Stack:

    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) == 0:
            return None
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0


tree = Tree(5)
tree.insert_with_recurssion(2)
tree.insert_with_recurssion(1)
tree.insert_with_recurssion(3)
tree.insert_with_recurssion(7)
tree.insert_with_recurssion(6)
tree.insert_with_recurssion(8)


def pre_order_recursive(node):
    if node is None:
        return
    print(node.get_value())
    pre_order_recursive(node.get_left_child())
    pre_order_recursive(node.get_right_child())


def pre_order_with_stack(node):
    stack = Stack()

    stack.push(tree.get_root())

    while not stack.is_empty():
        node = stack.pop()

        print(node.get_value())

        if node.has_right_child():
            stack.push(node.get_right_child())

        if node.has_left_child():
            stack.push(node.get_left_child())


def in_order_recursive(node):
    if node is None:
        return
    in_order_recursive(node.get_left_child())
    print(node.get_value())
    in_order_recursive(node.get_right_child())


def in_order_stack(node):
    stack = Stack()

    current = node

    while not stack.is_empty() or current is not None:
        while current is not None:
            stack.push(current)
            current = current.left

        node = stack.pop()
        print(node.value)
        current = node.right


def post_order_recursive(node):
    if node is None:
        return
    post_order_recursive(node.get_left_child())
    post_order_recursive(node.get_right_child())
    print(node.get_value())


def post_order_stack(node):
    stack = Stack()

    current = node
    prev_popped = None

    while not stack.is_empty() or current is not None:
        while current is not None:
            stack.push(current)
            current = current.left

        node = stack.top()

        if node.has_right_child() and node.get_right_child() is not prev_popped:
            current = node.right
        else:
            node = stack.pop()
            print(node.get_value())
            prev_popped = node


def bfs(tree):
    node = tree.get_root()

    if node is None:
        return

    q = deque()
    q.appendleft(node)

    current_level = 0
    nodes_to_next_level = pow(2, current_level)

    output = ""
    should_print = True

    while len(q) != 0:
        node = q.pop()

        if node is None:
            output += "|" if output is not "" else ""
            output += "<empty>"
        else:
            output += "|" if output is not "" else ""
            output += str(node.get_value())
            q.appendleft(node.get_left_child())
            q.appendleft(node.get_right_child())
            should_print = True

        nodes_to_next_level -= 1

        if nodes_to_next_level == 0:
            current_level += 1
            nodes_to_next_level = pow(2, current_level)
            if should_print:
                print(output)
            output = ""
            should_print = False


def diameter_of_binary_tree(root):
    if root == None:
        return 0

    left_value = diameter_of_binary_tree(root.get_left_child())
    right_value = diameter_of_binary_tree(root.get_right_child())

    return (left_value if left_value > right_value else right_value) + 1


def path_from_root_to_node(root, data):
    l = []

    temp = root

    while temp is not None:
        l.append(temp.get_value())
        if temp.get_value() == data:
            break
        elif data > temp.get_value():
            temp = temp.get_right_child()
        else:
            temp = temp.get_left_child()

    if temp == None:
        return []
    return l


print(path_from_root_to_node(tree.get_root(), 6))
