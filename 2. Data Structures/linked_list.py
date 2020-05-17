class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


head = Node(2)
head.next = Node(1)


head = Node(2)
temp = head
for i in [1, 4, 3, 5]:
    temp.next = Node(i)
    temp = temp.next


def print_linked_list(head):
    current_node = head

    while head is not None:
        print(head.value)
        head = head.next


def create_linked_list(input_list):
    head = None
    temp = None
    for i in input_list:
        if head == None:
            temp = head = Node(i)
        else:
            temp.next = Node(i)
            temp = temp.next
    return head


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return

        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node.next = Node(value)

    def prepend(self, value):
        temp_node = Node(value)
        temp_node.next = self.head
        self.head = temp_node

    def search(self, value):
        temp_node = self.head

        while temp_node is not None:
            if temp_node.value == value:
                break
            temp_node = temp_node.next

        return temp_node

    def remove(self, value):
        temp_node = self.head
        prev_node = None

        while temp_node is not None and temp_node.value is not value:
            prev_node = temp_node
            temp_node = temp_node.next

        if temp_node == None:
            return None

        if temp_node == self.head:
            self.head = self.head.next
            return

        prev_node.next = temp_node.next

    def pop(self):
        if self.head == None:
            return None

        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.value

    def insert(self, value, pos):
        temp_node = self.head
        prev_node = None
        count = pos

        while temp_node is not None and count is not 0:
            prev_node = temp_node
            temp_node = temp_node.next
            count -= 1

        new_node = Node(value)
        new_node.next = temp_node

        if temp_node == None and prev_node == None:
            self.head = new_node
        elif temp_node == self.head:
            self.head = new_node
        else:
            prev_node.next = new_node

    def size(self):
        count = 0
        temp_node = self.head

        while temp_node is not None:
            count += 1
            temp_node = temp_node.next

        return count

    def print_list(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def to_list(self):
        result = []

        temp_node = self.head

        while temp_node is not None:
            result.append(temp_node.value)
            temp_node = temp_node.next

        return result

    def reverse(self):
        if self.head == None:
            return None

        current_node = self.head
        next_node = self.head
        previous_node = None

        while next_node is not None:
            next_node = next_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

        return self


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.tail = self.head = DoubleNode(value)
            return

        node = DoubleNode(value)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node

    def print_list_head(self):
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def print_list_tail(self):
        temp_node = self.tail

        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.previous


def iscircular(linked_list):
    if linked_list.head == None:
        return False

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while slow_runner is not None and fast_runner is not None:
        slow_runner = slow_runner.next

        fast_runner = fast_runner.next
        if fast_runner is not None:
            fast_runner = fast_runner.next

        if slow_runner == fast_runner and slow_runner is not None and fast_runner is not None:
            return True

    return False


class NestedLinkedList(LinkedList):

    def merge(self, list1, list2):
        start_node = temp_node = None

        temp1 = list1.head if list1 else None
        temp2 = list2.head if list2 else None

        while temp1 or temp2:
            if temp1:
                if not temp_node:
                    start_node = temp_node = Node(temp1.value)
                else:
                    temp_node.next = Node(temp1.value)
                    temp_node = temp_node.next

            if temp2:
                if not temp_node:
                    start_node = temp_node = Node(temp2.value)
                else:
                    temp_node.next = Node(temp2.value)
                    temp_node = temp_node.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        linked_list = LinkedList()
        linked_list.head = start_node
        return linked_list

    def flatten(self):
        temp_node = self.head
        linked_list = LinkedList()
        while temp_node:
            linked_list = self.merge(linked_list, temp_node.value)
            temp_node = temp_node.next
        return linked_list


def add_one(arr):
    carry = 1
    for i in range(len(arr)):
        arr[len(arr) - 1 - i] += carry
        carry = int(arr[len(arr) - 1 - i] / 10)
        arr[len(arr) - 1 - i] = int(arr[len(arr) - 1 - i] % 10)
        if i == len(arr) - 1 and carry:
            arr.insert(0, carry)

    return arr


def max_sum_subarray(arr):
    sum = arr[0]
    max_sum = arr[0]

    for i in arr[1:]:
        sum = max(sum + i, i)
        max_sum = max(max_sum, sum)

    return max_sum


def nth_row_pascal(n):
    if n == 0:
        return [1]

    current_row = [1]

    for i in range(1, n + 1):
        new_arr = [1] * (i + 1)
        for j in range(i + 1):
            if j == 0 or j == i:
                new_arr[j] = 1
            else:
                new_arr[j] = current_row[j - 1] + current_row[j]
        current_row = new_arr

    return current_row


def even_after_odd(head):
    start = head
    prev_node = head
    temp_node = head
    end = head
    odd = None
    odd_end = None

    if not head or not head.next:
        return head

    while end.next:
        end = end.next

    while temp_node:
        if temp_node.value % 2 == 0:
            if temp_node == start:
                start = temp_node.next
                if odd == None:
                    odd = odd_end = temp_node
                else:
                    odd_end.next = temp_node
                    odd_end = odd_end.next
                temp_node = temp_node.next
                odd_end.next = None
            else:
                prev_node.next = temp_node.next
                if odd == None:
                    odd = odd_end = temp_node
                else:
                    odd_end.next = temp_node
                    odd_end = odd_end.next
                temp_node = temp_node.next
                odd_end.next = None
        else:
            prev_node = temp_node
            temp_node = temp_node.next

    prev_node.next = odd

    return start


def skip_i_delete_j(head, i, j):
    if i == 0:
        return None

    skip = i
    delete = j

    temp_node = head
    prev_node = None

    while temp_node:
        if skip == 0:
            while delete and temp_node:
                temp_node = temp_node.next
                delete -= 1
            prev_node.next = temp_node

            skip = i
            delete = j
        else:
            skip -= 1
            prev_node = temp_node
            temp_node = temp_node.next


def swap_nodes(head, left_index, right_index):
    prev_one = None
    temp_one = head
    prev_two = None
    temp_two = head

    while left_index and right_index:
        prev_one = temp_one
        temp_one = temp_one.next
        prev_two = temp_two
        temp_two = temp_two.next
        left_index -= 1
        right_index -= 1

    while left_index:
        prev_one = temp_one
        temp_one = temp_one.next
        left_index -= 1

    while right_index:
        prev_two = temp_two
        temp_two = temp_two.next
        right_index -= 1

    temp_one_next = temp_one.next

    if temp_one.next == temp_two:
        temp_one.next = temp_two.next
        temp_two.next = temp_one
        prev_one.next = temp_two
    else:
        temp_one.next = temp_two.next
        prev_two.next = temp_one
        temp_two.next = temp_one_next
        prev_one.next = temp_two


ll = LinkedList()

for i in range(0, 13):
    ll.append(i)

swap_nodes(ll.head, 2, 4)
ll.print_list()
