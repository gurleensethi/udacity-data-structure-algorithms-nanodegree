# For solving this problem I have used the combination of Priority Queue and Tree.
#
# I have a single Node that can act as a node of queue and tree at the same time.
#
# Encoding
# --------
# For priority queue I have used a simple linked list, in which items are inserted
# using the insertion sort paradigm, i.e. whenever an item is inserted, we iterate
# over the list and find an appropriate index for it.
# This makes the time complexity of insertion in our Priority Queue O(N).
#
# First, we have to interate over the list of string of length L and count characters.
# This adds a complexity of O(L).
#
# We insert the characters into the priortiy queue. Let's say we have
# 'N' number of unique characters. The insertion of this would take O(N*(N + 1)/2), which
# can be written as O(N^2). The reason being, in the worst case, the insertion can take upto
# the size of queue, the size of queue goes from 1,2...N-1,N. This equals the sum of first N
# integers.
#
# Once our priority queue is ready, we start the process of dequeing the lowest two terms,
# combining them and adding the result back to the queue. The deque operation takes constant O(1)
# time. If there are N elements in the queue, we have to do this for N-1 times until we have only
# one element remaining, which represents the tree. Just as above this takes 1,2...N-2,N-1 in the worst
# case of insertion in queue. So the time complexity of this operation can be written as O(N^2).
#
# With the tree ready, we have to build our table that represents the code for each unique character
# in our string. I have used pre order traversal to keep track of path and visit leaf nodes. Time
# complexity of pre order traversal is O(N) where N is the total number of nodes in the tree.
#
# Once we have our table built, we iterate over the original string, for each character lookup the
# corresponding code and append it to output string.
#
# Decoding
# --------
# Give the encoded string and source tree, we can decode the string in O(L) where L is the length of
# encoded string.

import sys


class Node:

    def __init__(self, char, frequency):
        # Makes the node act as a node of linked list
        self.next = None

        # Makes the node act as a node of a tree
        self.left = None
        self.right = None

        self.char = char
        self.frequency = frequency

    def is_leaf_node(self):
        return self.left == None and self.right == None


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

        # Using the method of insertion sort
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

    if node.is_leaf_node():
        letter_code_dict[node.char] = path

    tree_preorder(node.left, letter_code_dict, path + "0")
    tree_preorder(node.right, letter_code_dict, path + "1")


def huffman_encoding(data):
    if not data or not data.strip():
        return "", None

    # Count the frequency of letters
    letter_count_dict = {}
    for c in data:
        if not c in letter_count_dict:
            letter_count_dict[c] = 0
        letter_count_dict[c] += 1

    # Add letter to priority queue
    queue = PriorityQueue()

    for key in letter_count_dict:
        queue.enqueue(Node(key, letter_count_dict[key]))

    while queue.size() is not 1:
        node1 = queue.dequeue()
        node2 = queue.dequeue()

        frequency_sum = node1.frequency + node2.frequency
        node = Node(None, frequency_sum)
        node.left = node1
        node.right = node2
        queue.enqueue(node)

    letter_code_dict = {}

    for key in letter_count_dict.keys():
        letter_code_dict[key] = ''

    tree = queue.dequeue()

    # If there is only one character
    if tree.is_leaf_node():
        new_node = Node(None, tree.frequency)
        new_node.left = tree
        tree = new_node

    tree_preorder(tree, letter_code_dict, '')

    encoded_data = ""

    for i in data:
        encoded_data += letter_code_dict[i]

    return encoded_data, tree


def huffman_decoding(data, tree):
    if not data or not data.strip() or not tree:
        return ""

    temp = tree
    output = ""
    index = 0

    while index < len(data):
        if data[index] == '0':
            temp = temp.left
        else:
            temp = temp.right

        if temp.is_leaf_node():
            output += temp.char
            # Move back to tree root
            temp = tree

        index += 1

    return output


if __name__ == "__main__":
    codes = {}

    print("Test 1")
    print("------")
    a_great_sentence = "Languages in increasing awesomeness: JavaScript, Python, Java, Go, C"

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

    print("Test 2")
    print("------")
    a_great_sentence = ""

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    if encoded_data:
        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("Test 3")
    print("------")
    a_great_sentence = "A"

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
