import heapq


def lastStoneWeight(stones):

    stones.sort()

    l = len(stones)

    if l == 2:
        return stones[1] - stones[0]

    while len(stones) > 1:
        d = heapq.nlargest(2, stones)
        print(d)
        if len(d) < 2:
            break

        if d[0] == d[1]:
            stones.remove(d[0])
            stones.remove(d[1])

            print(f'removed {d[0]} and {d[1]} to have {stones}')

        if d[1] < d[0]:
            stones.remove(d[1])
            stones.remove(d[0])

            stones.append((d[0] - d[1]))

            print(
                f'removed {d[0]}, {d[1]} and added {(d[0]-d[1])} to have {stones}')

    if len(stones) == 0:
        return 0
    else:
        return stones[0]


# 0ms runtime - genius


def lastStoneWeight2(stones):

    maxHeap = []

    # heaps place the min heap as the root and therefore we change them to negative to reverse this

    for stone in stones:
        maxHeap.append(-stone)

    heapq.heapify(maxHeap)

    while len(maxHeap) > 1:

        # heappop is normally used to find the smallest item and return it but since we used negatives the largest will be returned
        #  we convert it back to positive by appending a minus sign

        largest = -heapq.heappop(maxHeap)
        next_largest = -heapq.heappop(maxHeap)

        if largest != next_largest:
            d = largest - next_largest

            heapq.heappush(maxHeap,-d)

    return -maxHeap[0] if maxHeap else 0

print(lastStoneWeight2([9, 3, 2, 10]))
