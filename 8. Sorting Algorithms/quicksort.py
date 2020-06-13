def quicksort(items):
  pivot_sort(items, 0, len(items) - 1)

def pivot_sort(items, start, end):
  if start >= end:
    return

  pivot_index = end
  pivot_value = items[pivot_index]

  left_index = start

  while pivot_index != left_index:
    left_value = items[left_index]
    
    if left_value > pivot_value:
      items[left_index] = items[pivot_index - 1]
      items[pivot_index - 1] = items[pivot_index]
      items[pivot_index] = left_value
      pivot_index -= 1
    else:
      left_index += 1
  
  pivot_sort(items, start, pivot_index - 1)
  pivot_sort(items, pivot_index + 1, end)

items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)