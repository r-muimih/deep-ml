from collections import deque


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def _build(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    n, i = len(values), 1
    while queue and i < n:
        node = queue.popleft()
        if i < n:
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < n:
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def _diameter_and_max_path(root):
    # Iterative post-order: build a parents-after-children order.
    order, stack = [], [root]
    while stack:
        node = stack.pop()
        order.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    height = {}   # id(node) -> number of nodes on longest downward path
    down = {}     # id(node) -> best downward path sum starting at node
    diameter = 0
    best = float("-inf")

    for node in reversed(order):
        lh = height[id(node.left)] if node.left else 0
        rh = height[id(node.right)] if node.right else 0
        ld = max(0, down[id(node.left)]) if node.left else 0
        rd = max(0, down[id(node.right)]) if node.right else 0

        height[id(node)] = 1 + max(lh, rh)
        down[id(node)] = node.val + max(ld, rd)

        diameter = max(diameter, lh + rh)
        best = max(best, node.val + ld + rd)

    return diameter, best


def _inorder(root):
    out, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def _serialize(root):
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        if node is None:
            out.append("N")
        else:
            out.append(str(node.val))
            stack.append(node.right)   # right first so left is popped first
            stack.append(node.left)
    return ",".join(out)


def tree_drills(values):
    root = _build(values)
    if root is None:
        return {"diameter": 0, "max_path_sum": 0, "inorder": [], "serialized": "N"}

    diameter, max_sum = _diameter_and_max_path(root)
    return {
        "diameter": diameter,
        "max_path_sum": max_sum,
        "inorder": _inorder(root),
        "serialized": _serialize(root),
    }