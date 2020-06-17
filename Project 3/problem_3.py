# The solution of problem is straight forward, if we arrange the
# elements in a sorted order and pick ever other element for num1 
# and remaining element for num2 we have two numbers that have
# maximum sum.
#
# Since I not allowed to use internal sort function, I have implemented
# merge sort to sort the required arrays. Merge sort has a time complexity of O(N log(N)).
# Once the array is sorted we iterate over the sorted array to form the numbers. This takes
# O(N) time.
#
# Time complexity is O(N log(N) + N) which can be written as O(N log(N)).
#
# The space complexity is O(N) as the space complexity of merge sort is O(N), also we have to
# store the sorted array.

def merge_sort(input_list, start, end):
  if start == end:
    return [input_list[start]]

  middle = (start + end) // 2

  left = merge_sort(input_list, start, middle)
  right = merge_sort(input_list, middle + 1, end)

  temp_left = 0
  temp_right = 0

  result = []

  while temp_left < len(left) and temp_right < len(right):
    if left[temp_left] < right[temp_right]:
      result.append(left[temp_left])
      temp_left += 1
    else:
      result.append(right[temp_right])
      temp_right += 1

  while temp_left < len(left):
      result.append(left[temp_left])
      temp_left += 1

  while temp_right < len(right):
      result.append(right[temp_right])
      temp_right += 1

  return result

def rearrange_digits(input_list):    
    if len(input_list) == 0:
      return []
  
    sorted_list = merge_sort(input_list, 0, len(input_list) - 1)
    
    num1 = "0"
    num2 = "0"

    for i in range(len(sorted_list) -1, -1, -1):
      if i % 2 == 0:
        num1 += str(sorted_list[i])
      else:
        num2 += str(sorted_list[i])

    return int(num1), int(num2)

def test_function(test_case):    
    output = rearrange_digits(test_case[0])
    solution = test_case[1]    
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 1, 3, 1, 3, 5], [531, 431]]) # Event array length
test_function([[1, 4, 1, 3, 1, 3, 5], [5311, 431]]) # Odd array length
test_function([[4], [4]]) # Only one number
test_function([[], []]) # Only one number