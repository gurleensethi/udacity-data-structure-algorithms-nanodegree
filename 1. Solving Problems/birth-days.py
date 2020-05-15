from datetime import date


daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


def nextDay(year, month, day):
    days_in_month = daysOfMonth[month - 1]

    if isLeapYear(year) and month == 2:
        days_in_month += 1

    if day < days_in_month:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def isDateLess(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    elif month1 < month2:
        return True
    else:
        return day1 < day2


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0

    temp_year = year1
    temp_month = month1
    temp_day = day1

    assert isDateLess(year1, month1, day1, year2, month2, day2)

    while isDateLess(temp_year, temp_month, temp_day, year2, month2, day2):
        days += 1
        temp_year, temp_month, temp_day = nextDay(
            temp_year, temp_month, temp_day)

    return days


today = date.today()
current_day = today.day
current_month = today.month
current_year = today.year


print(daysBetweenDates(1996, 8, 18, current_year, current_month, current_day))
