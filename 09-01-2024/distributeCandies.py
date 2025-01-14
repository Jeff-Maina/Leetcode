def distributeCandies(candies, num_people):
    # candies required to proceed for each to get one
    t = candies
    turn = 0
    i = 1

    h = {}

    while candies > num_people:
        if i > num_people:
            turn += num_people
            i = 1

        c = (i + turn)

        if i not in h:
            h[i] = c
        else:
            h[i] += c

        print(f'on turn {turn} person-{i} received {c} candy')

        i += 1
        candies -= c

    res = []

    for i in range(1, num_people+1):
        # print(i)

        if i in h:
            res.append(h[i])
        else:
            s = sum([i for i in h.values()])
            res.append(t - s)

    return h, res


# we loop the users while giving them either +1 or all the candies left
# link to solution - https://algo.monster/liteproblems/1103

def distributeCandies2(candies, n):
    ans = [0]*n
    i = 0

    while candies:
        ans[i % n] += min(candies, i+1)
        candies -= min(candies, i+1)

        i += 1

    return ans


print(distributeCandies2(34, 3))
