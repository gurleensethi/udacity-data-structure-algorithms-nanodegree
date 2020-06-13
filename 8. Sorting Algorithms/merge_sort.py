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

def case_sort(string):
  lower_case = []
  upper_case = []

  for s in string:
    if ord(s) >= 97 and ord(s) <= 122:
      lower_case.append(s)
    else:
      upper_case.append(s)
    
  lower_case.sort()
  upper_case.sort()

  result = ""
  i = 0
  j = 0

  for s in string:
    if ord(s) >= 97 and ord(s) <= 122:
      result += lower_case[i]
      i += 1
    else:
      result += upper_case[j]
      j += 1

  return result


case_sort('fedRTSersUXJ')