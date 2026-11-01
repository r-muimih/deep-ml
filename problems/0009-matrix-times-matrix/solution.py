def matrixmul(a: list[list[int|float]],
              b: list[list[int|float]]) -> list[list[int|float]]:
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        return -1

    c = [[sum(a[i][k] * b[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(rows_a)]
    return c