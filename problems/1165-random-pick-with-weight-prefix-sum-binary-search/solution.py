from bisect import bisect_right
from itertools import accumulate


def random_pick_with_weight(weights, r):
    prefix = list(accumulate(weights))
    target = r * prefix[-1]
    idx = bisect_right(prefix, target)
    # Guard against floating point edge cases pushing idx past the end
    return min(idx, len(weights) - 1)