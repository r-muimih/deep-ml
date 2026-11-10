class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def _build(digits):
    dummy = ListNode()
    cur = dummy
    for d in digits:
        cur.next = ListNode(d)
        cur = cur.next
    return dummy.next


def _to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def add_two_numbers(l1, l2):
    a, b = _build(l1), _build(l2)

    dummy = ListNode()
    tail = dummy
    carry = 0

    while a or b or carry:
        total = carry
        if a:
            total += a.val
            a = a.next
        if b:
            total += b.val
            b = b.next

        carry, digit = divmod(total, 10)
        tail.next = ListNode(digit)
        tail = tail.next

    return _to_list(dummy.next)