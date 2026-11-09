def evaluate_expression(s):
    # s is a string arithmetic expression
    # return the integer result
    stack = []          # saved (stack, sign) contexts for parentheses
    terms = []          # finished additive terms in the current level
    num = 0
    op = '+'            # operator waiting to be applied to num
    i, n = 0, len(s)

    def apply(op, num):
        if op == '+':
            terms.append(num)
        elif op == '-':
            terms.append(-num)
        elif op == '*':
            terms.append(terms.pop() * num)
        else:  # '/'
            prev = terms.pop()
            q = abs(prev) // abs(num)           # truncate toward zero
            terms.append(q if (prev < 0) == (num < 0) else -q)

    while i < n:
        ch = s[i]
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '(':
            stack.append((terms, op))           # save current level
            terms, op, num = [], '+', 0
        elif ch in '+-*/)':
            apply(op, num)
            num = 0
            if ch == ')':
                value = sum(terms)
                terms, op = stack.pop()         # restore outer level
                num = value                     # the parenthesised value is the next operand
            else:
                op = ch
        i += 1

    apply(op, num)
    return sum(terms)