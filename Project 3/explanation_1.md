# Problem 1

My first approach was to start a counter set to zero 0,
increment it and check if sqaure of counter is equal to number or not.
While it did work, it didn't had time complexity if O(log(N)).

To gain the time complexity of O(log(N)), I used binary search.
Do a binary search with start equal to 1 and end equal to the number.
Calculate to the square of mid and check if it is equal to the number,
if the square is less than number, move start to mid (as we need a larger number),
if it is greater, move the end to mid (as we need a smaller number).
Binary search has a time complexity of O(log(N)).

The space complexity is O(1).
