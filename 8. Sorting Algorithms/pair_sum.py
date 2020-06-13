def pair_sum(arr, target):
    arr.sort()

    i = 0
    j = len(arr) - 1

    while i < j:      
      sum = arr[i] + arr[j]
      if sum == target:
        return [arr[i], arr[j]]
      elif sum < target:
        i += 1
      else:
        j -= 1

    return [None, None]

input_list = [2, 7, 11, 15]
target = 9

print(pair_sum(input_list, target))