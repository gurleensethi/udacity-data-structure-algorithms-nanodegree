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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_text = texts[0]
output = f'First record of texts, {first_text[0]} texts {first_text[1]} at time {first_text[2]}'
print(output)

last_call = calls[len(calls) - 1]
output = f'Last record of calls, {last_call[0]} calls {last_call[1]} at time {last_call[2]}, lasting {last_call[3]} seconds'
print(output)

"""
Runtime Analysis:

The time take by this program is O(1), considering that indexing a list for first and last position takes a
constant amount of time regardless the number of entries in it.

However, if you take into consideration the code that is required read and build the list, the complexity goes
to O(n), because we have to read n number of lines.
"""
