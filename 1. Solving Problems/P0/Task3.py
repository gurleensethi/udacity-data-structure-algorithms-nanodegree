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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

area_codes = set()
banglore_to_banglore_calls = 0
outgoing_banglore_calls = 0

for number1, number2, time, duration in calls:
    if number1.startswith("(080)"):
        if number2.startswith("("):
            area_codes.add(number2[1:number2.index(")")])
        elif " " in number2 and (number2[0] == '7' or number2[0] == '8' or number2[0] == '9'):
            area_codes.add(number2[0:4])
        elif number2.startswith("140"):
            area_codes.add("140")

    if number1.startswith("(080)"):
        outgoing_banglore_calls += 1

    if number1.startswith("(080)") and number2.startswith("(080)"):
        banglore_to_banglore_calls += 1

print("The numbers called by people in Bangalore have codes:")
sorted_area_codes = list(area_codes)
sorted_area_codes.sort()
for code in sorted_area_codes:
    print(code)

percentage = round((banglore_to_banglore_calls /
                    outgoing_banglore_calls) * 100, 2)

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
Runtime analysis:

The time complexity of this solution is O(n) where n is the number of call records.
We iterate through the list of call records once to find the area codes called by banglore numbers,
and the percentage of banglore to banglore calls.

If we condiser the list.sort() method, then the total time complexity becomes O(n log(n))
"""
