import pytest

from algorithms.recursion import fibonacci


@pytest.mark.parametrize('input,expected', [
    (3, 2), (4, 3), (5, 5), (8, 21), (10, 55), (13, 233), (19, 4181)
])
def test_fibonacci(input, expected):
    assert fibonacci(input) == expected
