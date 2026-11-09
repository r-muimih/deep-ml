def binary_search_closest(arr, target):
    # arr is sorted in non-decreasing order
    # return an integer index (or -1 for empty arr)
    if not arr:
        return -1

    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    # lo is the first index with arr[lo] >= target (or the last index if none)
    if lo > 0 and abs(arr[lo - 1] - target) <= abs(arr[lo] - target):
        return lo - 1
    return lo