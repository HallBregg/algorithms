import pytest

from algorithms.sort import selection_sort


@pytest.mark.parametrize('input_list,result', [
    ([1, 4, 2, 5, 3], [1, 2, 3, 4, 5]),
    ([5, 4, 2, 3, 1], [1, 2, 3, 4, 5]),
    ([-2, 4, 2, 9], [-2, 2, 4, 9]),
    ([None], [None]),
])
def test_selection_sort(input_list, result):
    assert selection_sort(input_list) == result
