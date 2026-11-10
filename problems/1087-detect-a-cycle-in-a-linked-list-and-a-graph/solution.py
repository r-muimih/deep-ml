def _list_cycle_entry(ll_next):
    if not ll_next:
        return -1

    slow = fast = 0
    # Phase 1: Floyd's tortoise and hare, detect whether a cycle exists
    while True:
        if fast == -1 or ll_next[fast] == -1:
            return -1
        slow = ll_next[slow]
        fast = ll_next[ll_next[fast]]
        if fast == -1:
            return -1
        if slow == fast:
            break

    # Phase 2: find the entry node
    slow = 0
    while slow != fast:
        slow = ll_next[slow]
        fast = ll_next[fast]
    return slow


def _graph_has_cycle(graph):
    n = len(graph)
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    for start in range(n):
        if color[start] != WHITE:
            continue

        color[start] = GRAY
        stack = [(start, iter(graph[start]))]   # iterative DFS, no recursion limit issues

        while stack:
            node, it = stack[-1]
            advanced = False
            for nxt in it:
                if color[nxt] == GRAY:          # back edge (includes self-loops)
                    return True
                if color[nxt] == WHITE:
                    color[nxt] = GRAY
                    stack.append((nxt, iter(graph[nxt])))
                    advanced = True
                    break
            if not advanced:
                color[node] = BLACK
                stack.pop()

    return False


def detect_cycles(ll_next, graph):
    return (_list_cycle_entry(ll_next), _graph_has_cycle(graph))