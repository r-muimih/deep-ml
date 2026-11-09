class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def contains_permutation(s1, s2):
    # fixed-size window with character counts
    k = len(s1)
    if k == 0:
        return True
    if k > len(s2):
        return False

    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1
    for ch in s2[:k]:
        window[ord(ch) - 97] += 1

    # matches = number of letters (out of 26) whose counts agree
    matches = sum(1 for i in range(26) if need[i] == window[i])
    if matches == 26:
        return True

    for i in range(k, len(s2)):
        add = ord(s2[i]) - 97
        rem = ord(s2[i - k]) - 97

        # add the new right character
        if window[add] == need[add]:
            matches -= 1
        window[add] += 1
        if window[add] == need[add]:
            matches += 1

        # remove the old left character
        if window[rem] == need[rem]:
            matches -= 1
        window[rem] -= 1
        if window[rem] == need[rem]:
            matches += 1

        if matches == 26:
            return True
    return False


def reverse_between(values, left, right):
    # build nodes, reverse positions left..right by relinking, return the values
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next

    prev = dummy
    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next                   # first node of the segment
    for _ in range(right - left):
        nxt = curr.next                # move nxt to the front of the segment
        curr.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    out = []
    node = dummy.next
    while node:
        out.append(node.val)
        node = node.next
    return out


def combination_sum2(candidates, target):
    # sorted backtracking that skips duplicates at the same depth
    nums = sorted(candidates)
    res = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            res.append(path[:])
            return
        for i in range(start, len(nums)):
            if nums[i] > remaining:
                break                          # sorted: nothing further can fit
            if i > start and nums[i] == nums[i - 1]:
                continue                       # duplicate at the same depth
            path.append(nums[i])
            backtrack(i + 1, remaining - nums[i])
            path.pop()

    backtrack(0, target)
    return res
