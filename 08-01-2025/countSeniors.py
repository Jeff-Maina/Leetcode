'''
You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

The first ten characters consist of the phone number of passengers.
The next character denotes the gender of the person.
The following two characters are used to indicate the age of the person.
The last two characters determine the seat allotted to that person.
Return the number of passengers who are strictly more than 60 years old.

'''


def countSeniors(details):

    count = 0

    for n in range(len(details)):

        age = details[n][11]+details[n][12]

        if age > '60':
            count += 1

    return count


print(countSeniors(["1313579440F2036","2921522980M5644"]))

'''

comparing the strings is faster than converting it to int for every word

'''

# 8:45 - 8:46