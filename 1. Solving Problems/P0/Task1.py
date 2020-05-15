"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

telephones = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for entry in texts:
        telephones.add(entry[0])
        telephones.add(entry[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for entry in calls:
        telephones.add(entry[0])
        telephones.add(entry[1])

output = f"There are {len(telephones)} different telephone numbers in the records."
print(output)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


"""
Runtime Analysis:

The time taken for the entire program is O(t + c), where 't' is the number of text records
and 'c' is the number of call records. The reason is we have to iterate over both the lists.
"""
