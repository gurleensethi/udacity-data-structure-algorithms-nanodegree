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


dd = DoublyLinkedList()
dd.append(1)
dd.append(2)
dd.append(3)
dd.print_list_tail()
