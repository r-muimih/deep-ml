from collections import deque


def vertical_order(values):
    if not values or values[0] is None:
        return []

    n = len(values)
    columns = {}                       # column index -> list of values
    queue = deque([(values[0], 0)])    # (node value, column)
    i = 1                              # next unread position in `values`

    while queue:
        val, col = queue.popleft()
        columns.setdefault(col, []).append(val)

        # The next two entries are this node's left and right children
        if i < n:
            if values[i] is not None:
                queue.append((values[i], col - 1))
            i += 1
        if i < n:
            if values[i] is not None:
                queue.append((values[i], col + 1))
            i += 1

    return [columns[c] for c in sorted(columns)]