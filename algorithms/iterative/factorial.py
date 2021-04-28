def factorial(n: int):
    assert n >= 0
    if n in (0, 1):
        return 1
    else:
        factorial_value = 1
        for i in range(1, n + 1):
            factorial_value *= i
        return factorial_value
