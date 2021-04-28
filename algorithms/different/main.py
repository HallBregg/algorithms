def nwd(x, y):
    """
    Euclid’s algorithm. (Największy wspólny dzielnik :)
    """
    mod = x % y
    if mod == 0:
        return y
    x, y = y, mod
    return nwd(x, y)
