def min_operations(target):
  steps = 0

  while target > 0:
    if target % 2 == 0:
      target = target // 2
    else:
      target = target - 1
    
    steps += 1
  
  return steps

print(min_operations(69))