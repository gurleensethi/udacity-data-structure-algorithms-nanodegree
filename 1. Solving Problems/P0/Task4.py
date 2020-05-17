import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

telemarketers = set()
not_telemarketers = set()

for number1, number2, time, duration in calls:
    not_telemarketers.add(number2)

    if number2 in telemarketers:
        telemarketers.remove(number2)

    if number1 not in not_telemarketers:
        telemarketers.add(number1)

for number1, number2, time in texts:
    if number1 in telemarketers:
        telemarketers.remove(number1)

sorted_telemarketer = list(telemarketers)
sorted_telemarketer.sort()

print("These numbers could be telemarketers: ")
for number in sorted_telemarketer:
    print(number)
