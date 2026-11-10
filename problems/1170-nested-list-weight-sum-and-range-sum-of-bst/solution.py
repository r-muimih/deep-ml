def analyze(nested, tree, low, high):
    # ---- Nested list: top-down and inverse weighted sums ----
    top_down = 0
    total = 0          # plain sum of all integers
    max_depth = 0      # depth of the deepest integer

    stack = [(nested, 1)]
    while stack:
        lst, depth = stack.pop()
        for item in lst:
            if isinstance(item, list):
                stack.append((item, depth + 1))
            else:
                top_down += item * depth
                total += item
                if depth > max_depth:
                    max_depth = depth

    # weight (D - d + 1) = (D + 1) - d, so the sum is (D + 1) * total - top_down
    inverse = (max_depth + 1) * total - top_down

    # ---- BST range sum (iterative, with pruning) ----
    range_sum = 0
    stack = [tree]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        v, left, right = node
        if low <= v <= high:
            range_sum += v
            stack.append(left)
            stack.append(right)
        elif v < low:
            stack.append(right)   # everything in the left subtree is smaller still
        else:                     # v > high
            stack.append(left)    # everything in the right subtree is larger still

    return (top_down, inverse, range_sum)