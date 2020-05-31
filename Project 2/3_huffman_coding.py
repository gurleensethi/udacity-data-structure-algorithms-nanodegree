import sys


class Node:

    def __init__(self, char, frequency, is_value_node):
        self.next = None
        self.left = None
        self.right = None
        self.char = char
        self.frequency = frequency

        # Represents if the node is a value node (leaf node in the tree)
        self.is_value_node = is_value_node


class PriorityQueue:

    def __init__(self):
        self.head = None
        self.item_count = 0

    def enqueue(self, node):
        self.item_count += 1

        if self.head == None:
            self.head = node
            return

        prev = None
        temp = self.head

        while temp and node.frequency >= temp.frequency:
            prev = temp
            temp = temp.next

        # Reached the end of list
        if temp == None:
            prev.next = node
        # Is the very first node
        elif prev == None:
            node.next = self.head
            self.head = node
        else:
            node.next = temp
            prev.next = node

    def dequeue(self):
        if self.head == None:
            return

        temp = self.head
        self.head = self.head.next
        self.item_count -= 1
        return temp

    def print_list(self):
        temp = self.head
        output = ""
        while temp:
            output += f"'{temp.char}':{temp.frequency}"
            if temp.next != None:
                output += " -> "
            temp = temp.next
        print(output)

    def is_empty(self):
        return self.item_count == 0

    def size(self):
        return self.item_count


def tree_preorder(node, letter_code_dict, path):
    if node == None:
        return

    if node.is_value_node:
        letter_code_dict[node.char] = path

    tree_preorder(node.left, letter_code_dict, path + "0")
    tree_preorder(node.right, letter_code_dict, path + "1")


def huffman_encoding(data):
    # Count the frequency of letters
    letter_count_dict = {}
    for c in data:
        if not c in letter_count_dict:
            letter_count_dict[c] = 0
        letter_count_dict[c] += 1

    # Add letter to priority queue
    queue = PriorityQueue()

    for key in letter_count_dict:
        queue.enqueue(Node(key, letter_count_dict[key], is_value_node=True))

    while queue.size() is not 1:
        node1 = queue.dequeue()
        node2 = queue.dequeue()

        node = Node(node1.char + node2.char, node1.frequency +
                    node2.frequency, is_value_node=False)
        node.left = node1
        node.right = node2
        queue.enqueue(node)

    letter_code_dict = {}

    for key in letter_count_dict.keys():
        letter_code_dict[key] = ''

    tree = queue.dequeue()

    tree_preorder(tree, letter_code_dict, '')

    encoded_data = ""

    for i in data:
        encoded_data += letter_code_dict[i]

    return encoded_data, tree


def huffman_decoding(data, tree):
    return ""


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "Elon Musk is great"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
