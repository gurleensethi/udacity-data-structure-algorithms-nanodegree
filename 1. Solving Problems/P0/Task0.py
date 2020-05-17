import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

text = texts[0]
call = calls[len(calls) - 1]

print(f'First record of texts, {text[0]} texts {text[1]} at time {text[2]}')
print(
    f'Last record of calls, {call[0]} calls {call[1]} at time {call[2]}, lasting {call[3]} seconds')
