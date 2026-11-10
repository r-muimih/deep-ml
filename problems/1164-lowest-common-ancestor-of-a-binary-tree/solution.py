from collections import deque


def lowest_common_ancestor(tree, p, q):
    if not tree or tree[0] is None:
        return None

    # Rebuild the tree implicitly via BFS, recording each node's parent.
    # Values are unique, so values can serve as node identifiers.
    parent = {tree[0]: None}
    queue = deque([tree[0]])
    n, i = len(tree), 1

    while queue and i < n:
        node = queue.popleft()
        if i < n:
            if tree[i] is not None:
                parent[tree[i]] = node
                queue.append(tree[i])
            i += 1
        if i < n:
            if tree[i] is not None:
                parent[tree[i]] = node
                queue.append(tree[i])
            i += 1

    # Collect p and all of its ancestors (a node counts as its own ancestor).
    ancestors = set()
    cur = p
    while True:
        ancestors.add(cur)
        cur = parent[cur]
        if cur is None:
            break

    # Walk up from q; the first node that is also an ancestor of p is the LCA.
    cur = q
    while cur not in ancestors:
        cur = parent[cur]
    return cur