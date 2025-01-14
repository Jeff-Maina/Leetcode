'''
2446. Determine if Two Events Have Conflict
Easy
Topics
Companies
Hint
You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.
'''
from datetime import datetime


def haveConflict(event1, event2):
    s1, e1 = event1
    s2, e2 = event2

    # overlapping instances if s2 or e2 are within the range s1 -> e1
    # if s2 < s1 and e2 > e1

    if (s1 <= s2 <= e1) or (s1 <= e2 <= e1):
        return True

    if s2 < s1 and e2 > e1:
        return True
    else:
        return False


print(haveConflict(["15:19", "17:56"],
                   ["14:11", "20:02"]))
