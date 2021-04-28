def factorial(n: int):
    assert n >= 0
    if n in (0, 1):
        return 1
    return n * factorial(n-1)
