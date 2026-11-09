def max_profit_single(prices):
    # running minimum and best gap
    best = 0
    lowest = float("inf")
    for p in prices:
        if p < lowest:
            lowest = p
        elif p - lowest > best:
            best = p - lowest
    return best


def max_profit_unlimited(prices):
    # sum of positive day-to-day rises
    total = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total += prices[i] - prices[i - 1]
    return total


def house_robber(nums):
    # f(i) = max(f(i - 1), f(i - 2) + nums[i]) with two variables
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1


def single_non_duplicate(nums):
    # binary search on pair parity
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if mid % 2 == 1:
            mid -= 1          # force mid to the start of a potential pair
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2      # pair intact, answer is to the right
        else:
            hi = mid          # pair broken, answer is at mid or to the left
    return nums[lo]