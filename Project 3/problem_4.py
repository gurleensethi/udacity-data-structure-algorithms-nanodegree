def sort_012(input_list):
  pos_0 = 0
  pos_2 = len(input_list) - 1
  current = 0

  while current <= pos_2:
    if input_list[current] == 0:
      input_list[current] = input_list[pos_0]
      input_list[pos_0] = 0
      pos_0 += 1
      current += 1
      pass
    elif input_list[current] == 2:
      input_list[current] = input_list[pos_2]
      input_list[pos_2] = 2
      pos_2 -= 1
      pass
    else:
      current += 1
  
  return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])