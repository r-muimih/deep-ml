def array_drills(op, data):
    if op == "ocean":
        res = []
        tallest = 0                      # heights are positive
        for i in range(len(data) - 1, -1, -1):
            if data[i] > tallest:
                res.append(i)
                tallest = data[i]
        res.reverse()
        return res

    if op == "toeplitz":
        for i in range(1, len(data)):
            for j in range(1, len(data[0])):
                if data[i][j] != data[i - 1][j - 1]:
                    return False
        return True

    if op == "diagonal":
        if not data or not data[0]:
            return []
        rows, cols = len(data), len(data[0])
        out = []
        for d in range(rows + cols - 1):
            # cells on anti-diagonal d, listed from the bottom-left end to the top-right end
            r_start = min(d, rows - 1)
            r_end = max(0, d - cols + 1)
            diag = [data[r][d - r] for r in range(r_start, r_end - 1, -1)]
            if d % 2 == 1:
                diag.reverse()           # odd: down-left (top-right to bottom-left)
            out.extend(diag)
        return out

    raise ValueError(f"unknown op: {op}")