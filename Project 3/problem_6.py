# To solve this problem we have to iterate over the unsorted array
# once and maintain two variables minimum and maximum, whenever we see a
# value that is less that the minimum or greater that the maximum we
# update the variables accordingly.
#
# Time complexity is O(N) and space complexity is O(1).

def get_min_max(ints):
    minimum = ints[0]
    maximum = ints[0]

    for i in ints:
      if i < minimum:
        minimum = i
      
      if i > maximum:
        maximum = i

    return (minimum, maximum)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")