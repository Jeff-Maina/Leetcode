'''
1360. Number of Days Between Two Dates
Easy

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.'''


def daysBetweenDates(date1, date2):
    def isLeap(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if date1 > date2:
        date1, date2 = date2, date1

    y1, m1, d1 = map(int, date1.split("-"))
    y2, m2, d2 = map(int, date2.split("-"))

    result = 0

    for year in range(y1, y2):
        result += 365 + isLeap(year)

    days[1] = 29 if isLeap(y1) else 28
    
    result -= sum(days[ : m1 - 1]) + d1
    days[1] = 29 if isLeap(y2) else 28
    result += sum(days[ : m2 - 1]) + d2
    return result

        


print(daysBetweenDates("2019-06-29", "2019-06-30"))
