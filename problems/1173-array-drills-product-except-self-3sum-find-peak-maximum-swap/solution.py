def array_drills(op, *args):
    if op == "product":
        nums = args[0]
        n = len(nums)
        out = [1] * n
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out

    if op == "3sum":
        nums = sorted(args[0])
        res = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

    if op == "peak":
        a = args[0]
        lo, hi = 0, len(a) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < a[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    if op == "maxswap":
        digits = list(str(args[0]))
        last = {d: i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                j = last.get(str(bigger), -1)
                if j > i:
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return int(args[0])

    if op == "merge":
        nums1, m, nums2, n = args
        a, b = nums1[:m], nums2[:n]
        i = j = 0
        out = []
        while i < m and j < n:
            if a[i] <= b[j]:
                out.append(a[i]); i += 1
            else:
                out.append(b[j]); j += 1
        out.extend(a[i:])
        out.extend(b[j:])
        return out

    raise ValueError(f"unknown op: {op}")