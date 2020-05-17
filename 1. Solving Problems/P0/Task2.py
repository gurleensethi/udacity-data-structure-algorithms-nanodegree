import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

number_time_dict = dict()

lcall = calls[0][0]
ltime = int(calls[0][3])

for number1, number2, data, time in calls:
    number_time_dict[number1] = int(
        time) + number_time_dict.get(number1, 0)

    if number_time_dict[number1] > ltime:
        lcall = number1
        ltime = number_time_dict[number1]

    number_time_dict[number2] = int(
        time) + number_time_dict.get(number2, 0)

    if number_time_dict[number2] > ltime:
        lcall = number2
        ltime = number_time_dict[number2]

print(f'{lcall} spent the longest time, {ltime} seconds, on the phone during September 2016.')
