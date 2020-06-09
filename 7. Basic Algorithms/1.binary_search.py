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

def recursive_binary_search(target, source, left=0):
	if len(source) == 0:
		return None
	center = (len(source) - 1) // 2
	if source[center] == target:
		return center + left
	elif source[center] < target:
		return recursive_binary_search(target, source[center + 1:], left + center + 1)
	else:
		return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
  index = binary_search(source, target)

  if not index:
    return None

  while source[index] == target:
    if index == 0:
      return 0
    if source[index - 1] == target:
      index -= 1
    else:
      return index

find_first(7, [1,3,5,7,7,7,8,11,12,13,14,15])