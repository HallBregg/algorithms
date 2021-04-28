import pytest


from algorithms.recursion import factorial


@pytest.mark.parametrize('input,expected', [
    (4, 24),
    (5, 120),
    (1, 1),
    (0, 1),
    (2, 2),
    (3, 6)
])
def test_factorial(input, expected):
    assert factorial(input) == expected


@pytest.mark.parametrize('input', [
    (-1), (-10), (-2)
])
def test_factorial_invalid(input):
    with pytest.raises(AssertionError):
        factorial(input)
