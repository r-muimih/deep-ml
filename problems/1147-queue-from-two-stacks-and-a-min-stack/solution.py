def process_operations(operations):
    # FIFO queue built from two stacks
    inbox = []   # receives enqueued values
    outbox = []  # serves dequeues in FIFO order

    # Min-stack: each entry is (value, minimum of the stack up to this entry)
    mstack = []

    results = []

    for op in operations:
        name = op[0]

        if name == "enqueue":
            inbox.append(op[1])

        elif name == "dequeue":
            if not outbox:
                # Move everything over, reversing the order so the oldest item is on top
                while inbox:
                    outbox.append(inbox.pop())
            results.append(outbox.pop())

        elif name == "mpush":
            v = op[1]
            if mstack:
                current_min = min(v, mstack[-1][1])
            else:
                current_min = v
            mstack.append((v, current_min))

        elif name == "mpop":
            results.append(mstack.pop()[0])

        elif name == "mtop":
            results.append(mstack[-1][0])

        elif name == "mmin":
            results.append(mstack[-1][1])

    return results