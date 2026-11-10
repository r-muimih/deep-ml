import heapq


def merge_two_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        # <= takes from a on ties, which keeps the merge stable
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def _heap_walk(lists):
    """Yield all elements across the lists in ascending order, lazily."""
    heap = [(lst[0], idx, 0) for idx, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    while heap:
        value, idx, pos = heapq.heappop(heap)
        yield value
        nxt = pos + 1
        if nxt < len(lists[idx]):
            heapq.heappush(heap, (lists[idx][nxt], idx, nxt))


def merge_k_sorted(lists):
    return list(_heap_walk(lists))


def kth_smallest(lists, k):
    if k <= 0:
        return None
    for count, value in enumerate(_heap_walk(lists), start=1):
        if count == k:
            return value
    return None
