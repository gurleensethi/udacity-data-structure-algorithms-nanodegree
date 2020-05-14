from datetime import date


daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    return year % 4 == 0


def nextDay(year, month, day):
    if day < 30:
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


def getDays(day, month, year):
    today = date.today()
    current_day = today.day
    current_month = today.month
    current_year = today.year


print(daysBetweenDates(1920, 8, 18, 2020, 8, 18))
