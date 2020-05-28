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
