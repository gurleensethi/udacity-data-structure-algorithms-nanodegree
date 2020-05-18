class QueueArray:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.front_index = -1
        self.queue_size = 0

    def enqueue(self, value):
        if (self.next_index) % len(self.arr) == self.front_index:
            self.__handle_queue_capacity_full()

        self.queue_size += 1
        self.arr[self.next_index] = value
        if self.front_index == -1:
            self.front_index = 0
        self.next_index = (self.next_index + 1) % len(self.arr)

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.is_empty():
            return None

        return self.arr[self.front_index]

    def dequeue(self):
        if self.front_index == -1:
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr)

        self.queue_size -= 1

        if self.queue_size == 0:
            self.front_index = -1
            self.next_index = 0

        return value

    def __handle_queue_capacity_full(self):
        new_arr = [0 for _ in range(len(self.arr) * 2)]

        temp_index = self.front_index
        temp_new_arr_index = self.front_index
        while True:
            new_arr[temp_new_arr_index] = self.arr[temp_index]
            temp_new_arr_index += 1
            temp_index = (temp_index + 1) % len(self.arr)

            if temp_index == self.next_index:
                break

        self.arr = new_arr
        self.next_index = temp_new_arr_index

    def print_queue(self):
        for i in self.arr:
            print(i)
