import pytest

from algorithms.recursion import r_count


@pytest.mark.parametrize('input_list,expected', [
    (['asd', 1, 4, 'test'], 4),
    ([0, 0, 0, 0], 4),
    ([], 0),
    ([0, None, False], 3)
])
def test_r_count(input_list, expected):
    assert r_count(input_list) == expected
