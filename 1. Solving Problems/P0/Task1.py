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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

telephones = set()

for entry in texts:
    telephones.add(entry[0])
    telephones.add(entry[1])

for entry in calls:
    telephones.add(entry[0])
    telephones.add(entry[1])

output = f"There are {len(telephones)} different telephone numbers in the records."
print(output)
"""
Runtime Analysis:

The time taken for the entire program is O(t + c), where 't' is the number of text records
and 'c' is the number of call records. The reason is we have to iterate over both the lists.
"""
