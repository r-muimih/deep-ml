import heapq
from collections import Counter


def top_k_frequent(nums, k):
    if k <= 0:
        return []
    counts = Counter(nums)
    # nsmallest with key (-freq, value) gives highest frequency first,
    # and the smaller value first on ties. Uses a size-k heap internally.
    best = heapq.nsmallest(k, counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [val for val, _ in best]


def k_closest_points(points, k):
    if k <= 0:
        return []
    # Squared distance preserves ordering and avoids floating point error.
    # Tuple key (dist, x, y) handles the tie-breaking rules.
    best = heapq.nsmallest(
        k,
        points,
        key=lambda p: (p[0] * p[0] + p[1] * p[1], p[0], p[1]),
    )
    return [[p[0], p[1]] for p in best]