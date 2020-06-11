class Heap:
  def __init__(self, initial_size):
    self.array = [None for _ in range(initial_size)]
    self.next_index = 0

  def __double_array(self):
    temp = self.array
    self.array = [None for _ in range(len(temp) * 2)]
    for index, value in enumerate(temp):
      self.array[index] = value

  def insert(self, value):
    if self.next_index == len(self.array):
      self.__double_array()

    self.array[self.next_index] = value

    index = self.next_index

    while index > 0:
      parent_index = (index - 1) // 2

      if self.array[parent_index] > self.array[index]:
        temp = self.array[parent_index]
        self.array[parent_index] = self.array[index]
        self.array[index] = temp
        index = parent_index
      else:
        break

    self.next_index += 1

  def remove(self):
    if self.next_index == 0:
      return None

    value_to_return = self.array[0]

    self.array[0] = self.array[self.next_index - 1]

    self.next_index -= 1

    temp_index = 0

    while True:
      child_one_index = (2 * temp_index) + 1
      child_two_index = (2 * temp_index) + 2      
      value = self.array[temp_index]

      if child_one_index >= self.next_index:
        break

      child_one = self.array[child_one_index]
      child_two = self.array[child_two_index]
      
      if child_one < child_two and value > child_one:
        temp = self.array[child_one_index]
        self.array[child_one_index] = self.array[temp_index]
        self.array[temp_index] = temp
        temp_index = child_one_index
      elif child_two < child_one and value > child_two:
        temp = self.array[child_two_index]
        self.array[child_two_index] = self.array[temp_index]
        self.array[temp_index] = temp
        temp_index = child_two_index
      else:
        break        

    return value_to_return

heap = Heap(1)
for i in [10, 20, 40, 15, 30, 70, 60, 75, 50]:
  heap.insert(i)  

while heap.next_index != 0:
  print(heap.remove())  