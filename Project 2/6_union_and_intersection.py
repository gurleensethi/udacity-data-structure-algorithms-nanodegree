# To solve this problem I have used 'set', which is a hash based
# data structure to keep track of unique elements. This problem can
# be solved with a Hash map as well, with no change in time complexity.
#
# Union
# -----
# Traverse the List1 and add all elements in a temporary set.
# Traverse the List2 and check if the element exists in temporary set.
# If it does not exists, add it to the final set.
#
# We have to traverse both the lists only once. So the time complexity
# is O(m+n), where m is length of list1 and n is length of list2.
# The space complexity is O(m+n), where m is length of list1 and n is
# the length of resulting set, which in worst case cannot be larger
# than the combined length of both lists.
#
# Intersection
# ------------
# Just like union we first iterate list1 and add all of its elements into
# a temporary set.
# Then we iterate over list2 and check if the element exists in temporary set.
# If it exists, add it to the final array.
#
# We have to traverse both the lists only once. So the time complexity
# is O(m+n), where m is length of list1 and n is length of list2.
# The space complexity is O(m+n), where m is length of list1 and n is
# the length of resulting array, which in worst case cannot be larger
# than the smaller list.
#
#
# To optimize space complexity in both cases, we can set the list1 to the
# larger of two lists, this way we would initally copy the smaller list
# into the temporary set.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    result = []
    value_set = set()

    temp = llist_1.head

    while temp:
        result.append(temp.value)
        value_set.add(temp.value)
        temp = temp.next

    temp = llist_2.head

    while temp:
        if not temp.value in value_set:
            result.append(temp.value)
        temp = temp.next

    return result


def intersection(llist_1, llist_2):
    result = set()
    value_set = set()

    temp = llist_1.head

    while temp:
        value_set.add(temp.value)
        temp = temp.next

    temp = llist_2.head

    while temp:
        if temp.value in value_set:
            result.add(temp.value)
        temp = temp.next

    return list(result)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))
