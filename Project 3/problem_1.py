def sqrt(number):
  # Base case
  if number == 0 or number == 1:
    return number

  begin = 1
  end = number
  
  while begin <= end:
    mid = (begin + end) // 2
  
    square = mid * mid

    if square == number:
      return mid
    elif square < number:
      begin = mid + 1
    else:
      end = mid - 1

  return end

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(30)) else "Fail")
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (1 == sqrt(3)) else "Fail")