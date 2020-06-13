def mergesort(items):  
  if len(items) <= 1:
    return items

  left = mergesort(items[0 : len(items) // 2])
  right = mergesort(items[len(items) // 2 :])

  merge_result = merge(left, right)
  
  return merge_result

def merge(left, right):
  if left == right:
    return left

  copy_array = []
  i = 0
  j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      copy_array.append(left[i])
      i += 1
    else:
      copy_array.append(right[j])
      j += 1

  copy_array += left[i:]
  copy_array += right[j:]

  return copy_array

print(mergesort([4,23,54,3,32,54,65,23,54,7,68,6,45]))