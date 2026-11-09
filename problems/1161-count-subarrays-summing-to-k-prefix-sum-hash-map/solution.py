def count_and_longest_subarrays(nums, k):
    # nums: list of ints, k: int
    # return a tuple (count, longest)
    prefix_counts = {0: 1}   # how many times each prefix sum has occurred
    first_index = {0: -1}    # earliest index where each prefix sum occurred
    prefix = 0
    count = 0
    longest = 0

    for i, x in enumerate(nums):
        prefix += x
        need = prefix - k
        if need in prefix_counts:
            count += prefix_counts[need]
            longest = max(longest, i - first_index[need])
        prefix_counts[prefix] = prefix_counts.get(prefix, 0) + 1
        first_index.setdefault(prefix, i)

    return (count, longest)