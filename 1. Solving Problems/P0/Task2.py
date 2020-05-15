"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

numbers_and_time = dict()

longest = calls[0][0]
longest_time = int(calls[0][3])

for number1, number2, data, time in calls:
    numbers_and_time[number1] = int(
        time) + numbers_and_time.get(number1, 0)
    numbers_and_time[number2] = int(
        time) + numbers_and_time.get(number2, 0)

    if numbers_and_time[number1] > longest_time:
        longest = number1
        longest_time = numbers_and_time[number1]

    if numbers_and_time[number2] > longest_time:
        longest = number2
        longest_time = numbers_and_time[number2]

output = f'{longest} spent the longest time, {longest_time} seconds, on the phone during September 2016.'
print(output)

"""
Runtime Analysis:

The time complexity of this solution is O(n) where 'n' is the number of calls.
We iterate over the list of call records and keep the track of number and thier total duration.
Simultaneously we update the variable that keeps track of the number that spent the most time.
"""
