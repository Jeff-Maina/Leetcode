

def minimumAbsDifference(arr):
    arr = sorted(arr)

    d = {}

    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff in d:
            d[diff].append([arr[i-1], arr[i]])
        else:
            d[diff] = [[arr[i-1], arr[i]]]

    return d[min(d)]


print(minimumAbsDifference([40, 11, 26, 27, -20]))



# time limit exceeded


# def minimumAbsDifference2(arr):
#     arr.sort()

#     diff_arr = [(arr[i] - arr[i-1]) for i in range(1, len(arr))]

#     ans = [[arr[i], arr[i+1]]
#            for i in range(len(diff_arr)) if (arr[i+1]-arr[i]) == min(diff_arr)]

#     return ans
