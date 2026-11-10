class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def _reverse_iterative(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next      # save the rest of the list
        cur.next = prev     # flip the pointer
        prev = cur          # advance prev
        cur = nxt           # advance cur
    return prev


def _reverse_recursive(head):
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head
    new_head = _reverse_recursive(head.next)
    head.next.next = head   # make the next node point back to this one
    head.next = None        # this node becomes the tail
    return new_head


def reverse_linked_list(values, method="iterative"):
    head = _build(values)

    if method == "iterative":
        head = _reverse_iterative(head)
    elif method == "recursive":
        head = _reverse_recursive(head)
    else:
        raise ValueError("method must be 'iterative' or 'recursive'")

    return _to_list(head)