# My first approach was to start a counter set to zero 0,
# increment it and check if sqaure of counter is equal to number or not.
# While it did work, it didn't had time complexity if O(log(N)).
#
# To gain the time complexity of O(log(N)), I used binary search.
# Do a binary search with start equal to 1 and end equal to the number.
# Calculate to the square of mid and check if it is equal to the number,
# if the square is less than number, move start to mid (as we need a larger number),
# if it is greater, move the end to mid (as we need a smaller number).
# Binary search has a time complexity of O(log(N)).
#
# The space complexity is O(1).

def sqrt(number):
  # Base case
  if number == 0 or number == 1:
    return number

  begin = 1
  end = number
  
  # Binary search for the value
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