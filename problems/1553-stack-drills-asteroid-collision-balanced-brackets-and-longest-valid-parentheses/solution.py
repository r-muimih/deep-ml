def asteroid_collision(asteroids):
    stack = []
    for a in asteroids:
        alive = True
        # Only a left-mover can hit a right-mover sitting on top of the stack
        while alive and a < 0 and stack and stack[-1] > 0:
            top = stack[-1]
            if top < -a:
                stack.pop()          # top explodes, a keeps going
            elif top == -a:
                stack.pop()          # both explode
                alive = False
            else:
                alive = False        # a explodes
        if alive:
            stack.append(a)
    return stack


def is_balanced(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack


def longest_valid_parentheses(s):
    stack = [-1]   # base: index of the last unmatched ')'
    best = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)      # new base: this ')' is unmatched
            else:
                best = max(best, i - stack[-1])
    return best