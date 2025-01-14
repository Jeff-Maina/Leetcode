def areAlmostEqual(s1, s2):

    A = []
    B = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            A.append(s1[i])
            B.append(s2[i])

    print(A,B)

    if len(A) == len(B) == 0:
        return False

    if len(A) == len(B) == 2:
        if A[0] == B[1] and B[0] == A[1]:
            return True

    return False


print(areAlmostEqual('kelb', 'kelb'))
