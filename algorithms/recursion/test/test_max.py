import pytest

from algorithms.recursion.max import r_max, r_max_no_len


@pytest.mark.parametrize('input,result', [
    ([1, 2, 3, 4, 10, 6], 10),
    ([12, 2, 3, 4, 10, 6], 12),
    ([], None),
    ([1], 1)
])
def test_r_max(input, result):
    assert r_max(input) == result


@pytest.mark.parametrize('input,result', [
    ([1, 2, 3, 4, 10, 6], 10),
    ([12, 2, 3, 4, 10, 6], 12),
    ([], None),
    ([1], 1)
])
def test_r_max_no_len(input, result):
    assert r_max_no_len(input) == result
