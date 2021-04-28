import pytest

from algorithms.recursion import r_sum


@pytest.mark.parametrize('input_list,expected', [
    ([1, 2, 3, 4], 10),
    ([1, 2, 3, 4, 0], 10),
    ([], 0),
    ([0, 0, 1], 1),
])
def test_r_sum(input_list, expected):
    assert r_sum(input_list) == expected
