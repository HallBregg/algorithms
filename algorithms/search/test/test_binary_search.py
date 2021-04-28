import pytest

from algorithms.search.binary_search import binary_search


@pytest.mark.parametrize('input_list,item,result', [
    ([1, 2, 3], 1, 0),
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], 3, 2),
    ([1, 2, 3, 4, 5, 6, 7], 7, 6),
    ([1, 2, 3, 4, 5, 6, 7], 4, 3)
])
def test_binary_search(input_list, item, result):
    assert binary_search(input_list, item) == result


@pytest.mark.parametrize('input_list,item', [
    ([1, 2, 3], 0),
    ([1, 2, 3], 1.1),
    ([1, 2, 3], 4),
    ([1, 2, 3, 4, 5, 6, 7], 8),
    ([1, 2, 3, 4, 5, 6, 7], -1)
])
def test_binary_search_invalid(input_list, item):
    assert binary_search(input_list, item) is None
