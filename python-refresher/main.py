from datetime import date

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    return year % 4 == 0


def getDays(day, month, year):
    today = date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year

    days = 0
    days += daysOfMonth[month] - day
    days += current_day

    if isLeapYear(year) and (current_month == 2 or month == 2):
        days += 1

    if year == current_year:
        if month == current_month:
            return current_day - day

        for i in range(month + 1, current_month):
            if i == 2 and isLeapYear(year):
                days += 1
            days += daysOfMonth[i]

        return days

    temp_month = month + 1
    temp_year = year

    while temp_year != current_year or temp_month != month:
        if isLeapYear(temp_year) and temp_month == 2:
            days == 0
        days += daysOfMonth[temp_month]

        temp_month += 1

        if temp_month == 12:
            temp_month = 0
            temp_year += 1

    return days


print(getDays(18, 8, 1996))
