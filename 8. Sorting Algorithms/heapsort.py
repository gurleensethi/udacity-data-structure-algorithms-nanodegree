def heapsort(items):
    for i in range(len(items)):  
      heapify(items, len(items), len(items) - i - 1)

    for i in range(len(items) - 1, -1, -1):
      items[0], items[i] = items[i], items [0]
      heapify(items, i, 0)
    
def heapify(arr, n, position):    
    current = position
    left = 2 * current + 1
    right = 2 * current + 2    

    if left < n and arr[left] > arr[current]:
      current = left

    if right < n and arr[right] > arr[current]:
      current = right

    if current != position:
      temp = arr[current]
      arr[current] = arr[position]
      arr[position] = temp

      heapify(arr, n, current)

items = [4,1,10,5,6,6,19]
heapsort(items)
print(items)