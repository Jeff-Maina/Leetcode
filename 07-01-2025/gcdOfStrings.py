
def gcdOfStrings(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    res = []

    '''
    not sure it would help but you can reverse the range of the min l to 0 and break after finding the first value
    '''
    for i in range(1, l1+1):
        if l2 % i == 0 and l1 % i == 0:
            res.append(i)

    gcd = max(res)
    strGcd = str2[:gcd]

    if strGcd*int(l1/gcd) == str1 and strGcd*int(l2/gcd) == str2:
        return strGcd
    else:
        return ''


print(gcdOfStrings("AAAAAAAAA", "AAACCC"))
