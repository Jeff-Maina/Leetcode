def licenseKeyFormatting(s, k):
    word = s.replace("-", "").upper()

    rem = len(word) % k
    
    pre = word[:rem] if rem != 0 else word[:k]
    rw = word[rem:] if rem != 0 else word[k:]

    suf = ''

    for i in range(k, len(rw)+1, k):
        suf += '-' + rw[:i][-k:]


    return pre + suf


print(licenseKeyFormatting("2-4A0r7-4k", 3))


# most efficient leetcode solution
def licenseKeyFormatting(self, s, k):
    s = s.replace('-', '').upper()
    if len(s) % k != 0:
        s_list = [s[0:len(s) % k]]
    else:
        s_list = []
    s_list = s_list + [s[i:i+k] for i in range(len(s) % k, len(s), k)]
    
    return '-'.join(s_list)
