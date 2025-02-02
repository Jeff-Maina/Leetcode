'''
1732. Find the Highest Altitude
Easy

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
'''


def largestAltitude(gain):
    alts = [0]*(len(gain)+1)

    c = 0

    for i in range(1,len(alts)):
        c += gain[i-1]
        alts[i] = c

    return max(alts)

print(largestAltitude([-5,1,5,0,-7]))
