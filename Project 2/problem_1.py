# To solve this problem I have used a combination of HashMap and DoublyLinkedList.
#
# For HashMap, I have used the internal dictionary of Python as it serves the purpose.
# Hash Map allows for instant access of elements so they are appropriate for fetching
# any value corresponding to a key. They are also good for instant insertion. Both
# access and insertion in Hash Maps are O(1).
#
# Hash Map maintains no sequence, elements are inserted based on their 'hash' values.
#
# An LRU cache requires a sequence to be present, the elements need to be sequenced in
# such a way that one end represents the most recent used element and the other represents
# least recently used.
#
# A possibility is to make the values inside HashMap nodes of a LinkedList, the head
# of the list could represent the most recently used element, whereas the last element would represent
# the least recently used. As a user retrieves an element, it is moved to the top of the list. When we
# want to insert a new element, and the cache is at full capacity, we traverse the list and remove the
# last element. This however makes the insertion O(n), where n is the cache capacity.
#
# To solve this, instead of using a LinkedList, I have used a DoublyLinkedList. With a DoublyLinkedList,
# we have access to the last element in the list and we can remove it instantly. Also, we can instantly
# move an element to the head without needing any traversal, keeping the time complexity of operations O(1).
#
# This helps us achieve the time complexity O(1) for all operations.

# A node used in DoublyLinkedList
class DoubleListNode:

    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.previous = None
        self.next = None

    def __repr__(self):
        return f"DoubleListNode: Value = {self.value}"


class LRU_Cache(object):

    def __init__(self, capacity, debug=False):
        self.cache = {}
        self.capacity = capacity
        self.list_head = None
        self.list_tail = None

        # Used for printing the logs
        self.debug = debug

    def __log(self, message):
        if self.debug:
            print("[LRU_Cache]", message)

    def get(self, key):
        if key in self.cache:
            # Move the item to the top and make it
            # head of the list.

            accessed_node = self.cache[key]
            self.__log(f"{accessed_node} accessed, moving it to the head")

            # Do these opeartions only if it is not the head
            # already
            if accessed_node is not self.list_head:
                # Remove the node from existing chain
                node_prev = accessed_node.previous
                node_next = accessed_node.next
                node_prev.next = node_next

                # Because this node can be the last
                # which makes node_next null.
                if node_next is not None:
                    node_next.previous = node_prev

                accessed_node.next = self.list_head
                accessed_node.previous = None
                self.list_head.previous = accessed_node
                self.list_head = accessed_node

            return accessed_node.value

        # Nothing found
        return -1

    def set(self, key, value):
        new_node = DoubleListNode(key, value)
        self.__log(f"Inserting {new_node}")

        # If this is the first element being inserted
        # Set the head and tail equal to it.
        if len(self.cache) is 0:
            self.list_head = new_node
            self.list_tail = new_node
            self.cache[key] = new_node
            return

        # We have reached the cache limit.
        # Remove the element present at the tail of list
        if len(self.cache) is self.capacity:
            node_to_delete = self.list_tail
            self.__log(f"Capacity reached, removing {node_to_delete}")
            previous_of_tail = self.list_tail.previous

            # The element at tail is the last element
            # (Only happens when cache capacity is 1)
            if previous_of_tail is None:
                self.list_head = None
                self.list_tail = None
            else:
                self.list_tail.previous = None
                self.list_tail = previous_of_tail
                self.list_tail.next = None

            self.cache.pop(node_to_delete.key)

        # Insert the new element at the head of list
        new_node.next = self.list_head
        self.list_head.previous = new_node
        self.list_head = new_node
        self.cache[key] = new_node


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

# returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.get(3))
print(our_cache.get(4))  # returns 4
our_cache.set(7, 7)
print(our_cache.get(2))  # returns -1
