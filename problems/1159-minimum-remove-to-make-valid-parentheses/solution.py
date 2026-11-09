def min_remove_to_make_valid(s):
    # s is a string of lowercase letters, '(' and ')'
    # Return a valid string after removing the fewest parentheses
    remove = set()
    stack = []                      # indices of unmatched '('
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()         # matched with the latest open paren
            else:
                remove.add(i)       # no open paren to match: drop it
    remove.update(stack)            # leftover '(' are unmatched: drop them
    return "".join(ch for i, ch in enumerate(s) if i not in remove)