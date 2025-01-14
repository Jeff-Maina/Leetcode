'''
1154. Day of the Year
Easy

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

'''


def dayOfYear(date):
    y, m, d = map(int, date.split("-"))

    res = 0

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(m-1):
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            days[1] = 29
        else:
            days[1] = 28

        res += days[i]

    return res + d


print(dayOfYear("1900-05-02"))
