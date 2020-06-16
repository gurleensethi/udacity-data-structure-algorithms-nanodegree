def simple_binary_search(input_list, start, end, number):

  while start <= end:
    mid = (start + end) // 2

    if input_list[mid] == number:
      return mid
    elif input_list[mid] > number:
      end = mid - 1
    else:
      start = mid + 1

  return -1

def rotated_array_search(input_list, number):
    # Find the rotation point in array using binary search
    start = 0
    end = len(input_list) - 1

    rotation_point = -1

    while start <= end:
      mid = (start + end) // 2      

      if mid - 1 >= start and input_list[mid - 1] > input_list[mid]:
        rotation_point = mid - 1
        break
      elif mid + 1 <= end and input_list[mid + 1] < input_list[mid]:
        rotation_point = mid
        break
      elif input_list[start] > input_list[mid]:
        end = mid - 1
      else:
        start = mid + 1

    if rotation_point != -1:
      first_half_result = simple_binary_search(input_list, 0, rotation_point, number)
      second_half_result = simple_binary_search(input_list, rotation_point + 1, len(input_list) - 1, number)      
      return second_half_result if first_half_result == -1 else first_half_result
    else:
      return simple_binary_search(input_list, 0, len(input_list) - 1, number)
    
      

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]    
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[2, 3, 4, 5, 6, 7, 8, 1], 1])
test_function([[0, 1, 2, 3, 4, 5, -3, -2, -1], 10])