# Problem 2

I have used binary search to solve this problem.
Initially I tried modifying binary search's selection criteria, but it didn't work.

The problem is easy to solve if we run binary search by breaking the array into,
two parts from the point where it is rotated.

Finding the rotation point by linear search would result in O(N) time.
I used binary search itself to search the rotation point in the array,
thus taking O(log(N)) time to search.

Once the rotation point has been found we can use binary search on both
the halfs of the array. This will take O(log(N)) for each half.

The total time complexity is O(log(N)) + O(log(N)) + O(log(N)) = O(3log(N))
we drop the constant when N is very large so the complexity is O(log(N)).

Space complexity is O(1) as we are not using any extra array, and for methods
we are passing the reference of array rather than a sub-array copy of it.
