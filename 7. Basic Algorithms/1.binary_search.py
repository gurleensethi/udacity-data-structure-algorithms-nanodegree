def binary_search(array, target):  
  start = 0
  end = len(array) - 1

  while start < end:
    middle = (start + end) // 2

    if array[middle] == target:
      return middle
    elif target > array[middle]:
      start = middle + 1
    else:
      end = middle - 1
    
  return -1

def binary_search_recursive(array, target, start_index, end_index):
    if end_index < start_index:
      return -1

    middle_index = (start_index + end_index) // 2

    if array[middle_index] == target:
      return middle_index
    elif target > array[middle_index]:
      return binary_search_recursive(array, target, middle_index + 1, end_index)
    else:
      return binary_search_recursive(array, target, start_index, middle_index - 1)
