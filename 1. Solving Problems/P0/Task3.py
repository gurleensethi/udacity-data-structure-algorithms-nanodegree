import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

codes = set()
b2b_calls = 0
outgoing_banglore_calls = 0

for number1, number2, time, duration in calls:
    if number1.startswith("(080)"):
        if number2.startswith("("):
            codes.add(number2[1:number2.index(")")])
        elif " " in number2 and (number2[0] == '7' or number2[0] == '8' or number2[0] == '9'):
            codes.add(number2[0:4])
        elif number2.startswith("140"):
            codes.add("140")

    if number1.startswith("(080)"):
        outgoing_banglore_calls += 1

    if number1.startswith("(080)") and number2.startswith("(080)"):
        b2b_calls += 1

print("The numbers called by people in Bangalore have codes:")
sorted_codes = list(codes)
sorted_codes.sort()
for code in sorted_codes:
    print(code)

percentage = round((b2b_calls /
                    outgoing_banglore_calls) * 100, 2)

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
