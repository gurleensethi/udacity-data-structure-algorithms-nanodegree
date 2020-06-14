def sort_012(input_list):
  zero_index = 0
  two_index = len(input_list) - 1

  current = 0

  while current <= two_index:
    if input_list[current] == 0:
      input_list[current] = input_list[zero_index]
      input_list[zero_index] = 0
      current += 1
      zero_index += 1
    elif input_list[current] == 2:
      input_list[current] = input_list[two_index]
      input_list[two_index] = 2
      two_index -= 1
    else:
      current += 1

items = [1,0,2,0,1,1,1,0,0,0,2,1,0]
sort_012(items)
print(items)