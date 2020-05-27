class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        temp = self.bucket_array[bucket_index]

        while temp is not None:
            if temp.key == key:
                temp.value = value
                return
            temp = temp.next

        new_node = LinkedListNode(key, value)
        new_node.next = self.bucket_array[bucket_index]
        self.bucket_array[bucket_index] = new_node

        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_bucket_index(key)

        temp = self.bucket_array[bucket_index]

        while temp is not None:
            if temp.key == key:
                return temp.value
            temp = temp.next

        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_cofficient = 1

        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_cofficient
            hash_code = hash_code % num_buckets
            current_cofficient *= self.p
            current_cofficient = current_cofficient % num_buckets

        return hash_code % num_buckets

    def size(self):
        return self.num_entries


map = HashMap()
map.put(1, 'Testing')
map.put(2, 'Testing')
map.put(1, 'Updated value')
print(map.get(1))
print(map.get(2))
print(map.get(34))
