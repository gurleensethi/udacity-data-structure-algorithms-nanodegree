# Problem 3

The solution of problem is straight forward, if we arrange the
elements in a sorted order and pick ever other element for num1
and remaining element for num2 we have two numbers that have
maximum sum.

Since I not allowed to use internal sort function, I have implemented
merge sort to sort the required arrays. Merge sort has a time complexity of O(N log(N)).
Once the array is sorted we iterate over the sorted array to form the numbers. This takes
O(N) time.

Time complexity is O(N log(N) + N) which can be written as O(N log(N)).

The space complexity is O(N) as the space complexity of merge sort is O(N), also we have to
store the sorted array.
