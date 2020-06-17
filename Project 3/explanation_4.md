# Problem 4

If we insert all the 0s at the start of the array and all the 2s at the end
of the array, the 1s will automatically be in the center.

To solve this problem in one iteration we have to maintain two pointers.
One for insertion of 0s and the other for 2s.

We set the insertion location of 0s at the beginning and 2s at the end.
Then we start iterating over the array, if we see a zero we swap it with the
0s pointer and increment the 0s insertion pointer.
If we see a two we swap it with the 2s pointer and decrement the 2s insertion pointer.
We do this until we have crossed over the 2s pointer.

The result is a sorted array in just one iteration.
Time complexity is O(N) and space complexity is O(1).
