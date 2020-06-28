def knapsack_max_value_recur(knapsack_max_weight, items):
  return knapsack_max_recursive(knapsack_max_weight, items, len(items) - 1)

def knapsack_max_recursive(capacity, items, last_index):
  if capacity <= 0 or last_index < 0:
    return 0

  valueA = 0
  if items[last_index]['weight'] <= capacity:
    valueA = items[last_index]['value'] + knapsack_max_recursive(capacity - items[last_index]['weight'], items, last_index - 1)

  valueB = knapsack_max_recursive(capacity, items, last_index - 1)

  return max(valueA, valueB)

def knapsack_max_value(knapsack_max_weight, items):
  lookup = [0 for x in range(knapsack_max_weight + 1)]

  for item in items:
    for capacity in reversed(range(knapsack_max_weight + 1)):          
      if item['weight'] < capacity:
        lookup[capacity] = max(lookup[capacity], lookup[capacity - item['weight']] + item['value'])

  return lookup[-1]

items = [{ 'weight': 4, 'value': 3 }, { 'weight': 9, 'value': 1 }, { 'weight': 5, 'value': 6 }, { 'weight': 4, 'value': 3 }]
print(knapsack_max_value(10, items))
