"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

possible_telemarketers = set()
not_telemarketers = set()

for number1, number2, time, duration in calls:
    not_telemarketers.add(number2)

    if number2 in possible_telemarketers:
        possible_telemarketers.remove(number2)

    if number1 not in not_telemarketers:
        possible_telemarketers.add(number1)

for number1, number2, time in texts:
    if number1 in possible_telemarketers:
        possible_telemarketers.remove(number1)

sorted_telemarketer_numbers = list(possible_telemarketers)
sorted_telemarketer_numbers.sort()

print("These numbers could be telemarketers: ")
for number in sorted_telemarketer_numbers:
    print(number)

"""
Runtime analysis:

The time complexity of this program is O(c + t) where c is the number of call records 
and t is the number of text records.

This comes down to O(n) where n is the total input.
"""
