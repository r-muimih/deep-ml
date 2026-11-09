def first_n_fibonacci(n):
    # Return a list of the first n Fibonacci numbers
    if n <= 0:
        return []
    
    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    
    return fibs[:n]