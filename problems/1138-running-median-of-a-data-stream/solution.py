import heapq


def running_median(stream):
    lo = []  # max-heap (store negatives): lower half
    hi = []  # min-heap: upper half
    medians = []

    for x in stream:
        # Push through lo so every element in lo <= every element in hi
        heapq.heappush(lo, -x)
        heapq.heappush(hi, -heapq.heappop(lo))

        # Keep sizes balanced: len(lo) == len(hi) or len(lo) == len(hi) + 1
        if len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))

        if len(lo) > len(hi):
            medians.append(float(-lo[0]))
        else:
            medians.append((-lo[0] + hi[0]) / 2.0)

    return medians