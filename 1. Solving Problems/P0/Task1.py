import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numbers = set()

for entry in texts:
    numbers.add(entry[0])
    numbers.add(entry[1])

for entry in calls:
    numbers.add(entry[0])
    numbers.add(entry[1])

print(
    f"There are {len(numbers)} different telephone numbers in the records.")
