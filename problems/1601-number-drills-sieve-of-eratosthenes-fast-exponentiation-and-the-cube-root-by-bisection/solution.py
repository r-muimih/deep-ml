def sieve(n):
    # primes <= n, ascending
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for m in range(p * p, n + 1, p):
                is_prime[m] = False
        p += 1
    return [i for i, flag in enumerate(is_prime) if flag]


def fast_pow(x, n):
    # repeated squaring, negative n allowed, rounded to 6 decimals
    if n < 0:
        x = 1.0 / x
        n = -n
    result = 1.0
    base = x
    while n:
        if n & 1:
            result *= base
        base *= base
        n >>= 1
    return round(result, 6)


def cube_root(x, tol=1e-9):
    # bisection on t**3 - x, rounded to 6 decimals
    lo = -max(1.0, abs(x))
    hi = max(1.0, abs(x))
    while hi - lo >= tol:
        mid = (lo + hi) / 2
        if mid ** 3 < x:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2, 6)