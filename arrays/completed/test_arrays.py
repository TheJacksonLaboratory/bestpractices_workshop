from arrays import add_arrays, subtract_arrays, multiply_arrays, divide_arrays
import pytest


@pytest.mark.parametrize("a, b, expect",
                         [([1, 2, 3], [4, 5, 6], [5, 7, 9]),
                          ([1, 2, 3], [-1, -2, -3], [0, 0, 0]),
                          ([1, 2, 3], [-10, -20, -30], [-9, -18, -27])
                          ])
def test_add_arrays(a, b, expect):

    output = add_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize("a, b, expect",
                         [([1, 2, 3], [4, 5, 6], [-3, -3, -3]),
                          ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
                          ([1, 2, 3], [-10, -20, -30], [11, 22, 33])
                          ])
def test_subtract_arrays(a, b, expect):
    output = subtract_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize("a, b, expect",
                         [([1, 2, 3], [4, 5, 6], [4, 10, 18]),
                          ([1, 2, 3], [0, 0, 0], [0, 0, 0]),
                          ([1, 2, 3], [-10, -20, -30], [-10, -40, -90])
                          ])
def test_multiply_arrays(a, b, expect):

    output = multiply_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize("a, b, expect",
                         [([3, 2, 1], [4, 5, 4], [0.75, 0.4, 0.25]),
                          ([0, 0, 0], [1, 2, 3], [0, 0, 0]),
                          ([6, -4, 3], [2, 2, -1], [3, -2, -3])
                          ])
def test_divide_arrays(a, b, expect):

    output = divide_arrays(a, b)

    assert output == expect


def test_add_arrays_errors():
    a = [1, 2]
    b = [1, 2, 3]
    with pytest.raises(ValueError):
        _ = add_arrays(a, b)
    a = 1
    b = "a"
    with pytest.raises(TypeError):
        _ = add_arrays(a, b)


def test_subtract_arrays_errors():
    a = [1, 2]
    b = [1, 2, 3]
    with pytest.raises(ValueError):
        _ = subtract_arrays(a, b)
    a = 1
    b = "a"
    with pytest.raises(TypeError):
        _ = subtract_arrays(a, b)


def test_multiply_arrays_errors():
    a = [1, 2]
    b = [1, 2, 3]
    with pytest.raises(ValueError):
        _ = multiply_arrays(a, b)
    a = 1
    b = "a"
    with pytest.raises(TypeError):
        _ = multiply_arrays(a, b)


def test_divide_arrays_errors():
    a = [1, 2]
    b = [1, 2, 3]
    with pytest.raises(ValueError):
        _ = divide_arrays(a, b)
    a = 1
    b = "a"
    with pytest.raises(TypeError):
        _ = divide_arrays(a, b)
    a = [1, 2, 3]
    b = [0, 2, 3]
    with pytest.raises(ZeroDivisionError):
        _ = divide_arrays(a, b)


@pytest.fixture
def pair_of_lists():
    return ([10, 20, 30], [40, 50, 60])


def test_add_arrays_with_fixture(pair_of_lists):
    expect = [50, 70, 90]
    output = add_arrays(pair_of_lists[0], pair_of_lists[1])
    assert expect == output
