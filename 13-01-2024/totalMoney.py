'''
1716. Calculate Money in Leetcode Bank
Easy

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
'''


def totalMoney(n):
    total = 0
    w = 0

    for i in range(n):
        r = i % 7 + 1
        if i % 7 == 0:
            w = int(i/7)

        total += (r+w)

    return total

print(totalMoney(20))
