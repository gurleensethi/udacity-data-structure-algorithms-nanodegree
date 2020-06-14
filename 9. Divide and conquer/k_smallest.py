def k_smallest(arr, k):
  smaller = []
  middle = []
  larger = []

  pivot = arr[len(arr) // 2]

  for i in arr:
    if i < pivot:
      smaller.append(i)
    elif i > pivot:
      larger.append(i)
    else:
      middle.append(i)

  if k < len(smaller):
    return k_smallest(smaller, k)
  elif k > (len(smaller) + len(middle)):
    return k_smallest(larger, k - (len(smaller) + len(middle)))
  else:
    return pivot

print(k_smallest([4,2,245,7,43,34,4,5,2,213,56], 9))
