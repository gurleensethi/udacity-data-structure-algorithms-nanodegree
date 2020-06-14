def maxSubArrayRecursive(arr, start, stop):
  if start == stop:
    return arr[start]

  middle = (start + stop) // 2

  left_sum = maxSubArrayRecursive(arr, start, middle)
  right_sum = maxSubArrayRecursive(arr, middle + 1, stop)

  pad_left_sum = arr[middle]
  pad_left_max = arr[middle]  

  for i in range(middle - 1, start - 1, -1):
    pad_left_sum += arr[i]
    if pad_left_sum > pad_left_max:
      pad_left_max = pad_left_sum

  pad_right_sum = arr[middle + 1]
  pad_right_max = arr[middle + 1]

  for i in range(middle + 2, stop + 1):
    pad_right_sum += arr[i]
    if pad_right_sum > pad_right_max:
      pad_right_max = pad_right_sum

  return max(pad_left_max + pad_right_max, max(left_sum, right_sum))

def maxSubArray(arr):
  return maxSubArrayRecursive(arr, 0, len(arr) - 1)

print(maxSubArray([-2, -5, 6, -2, -3, 1, 5, -6]))