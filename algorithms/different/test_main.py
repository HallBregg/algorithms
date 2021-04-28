import pytest

from algorithms.different.main import nwd


@pytest.mark.parametrize('x,y,result', [
    (1680, 640, 80),
    (4, 2, 2),
    (2, 2, 2),
    (0, 2, 2),
    (-10, 6, 2),
    (-12, 6, 6)
])
def test_nwd(x, y, result):
    assert nwd(x, y) == result
