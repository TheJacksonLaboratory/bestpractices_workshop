from arrays_completed import add_arrays, subtract_arrays, multiply_arrays, divide_arrays
import pytest


@pytest.mark.parametrize(
    ("a", "b", "expect"),
    [
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        ([1, 2, 3], [-1, -2, -3], [0, 0, 0]),
        ([1, 2, 3], [-10, -20, -30], [-9, -18, -27]),
    ],
)
def test_add_arrays(a, b, expect):
    output = add_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize(
    ("a", "b", "expect"),
    [
        ([1, 2, 3], [4, 5, 6], [-3, -3, -3]),
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        ([1, 2, 3], [-10, -20, -30], [11, 22, 33]),
    ],
)
def test_subtract_arrays(a, b, expect):
    output = subtract_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize(
    ("a", "b", "expect"),
    [
        ([1, 2, 3], [4, 5, 6], [4, 10, 18]),
        ([1, 2, 3], [0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [-10, -20, -30], [-10, -40, -90]),
    ],
)
def test_multiply_arrays(a, b, expect):
    output = multiply_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize(
    ("a", "b", "expect"),
    [
        ([3, 2, 1], [4, 5, 4], [0.75, 0.4, 0.25]),
        ([0, 0, 0], [1, 2, 3], [0, 0, 0]),
        ([6, -4, 3], [2, 2, -1], [3, -2, -3]),
    ],
)
def test_divide_arrays(a, b, expect):
    output = divide_arrays(a, b)

    assert output == expect


@pytest.mark.parametrize(
    ("a", "b", "error"),
    [
        ([1, 2], [1, 2, 3], ValueError),
        (1, "a", TypeError),
    ],
)
def test_add_arrays_errors(a, b, error):
    with pytest.raises(error):
        add_arrays(a, b)


@pytest.mark.parametrize(
    ("a", "b", "error"),
    [
        ([1, 2], [1, 2, 3], ValueError),
        (1, "a", TypeError),
    ],
)
def test_subtract_arrays_errors(a, b, error):
    with pytest.raises(error):
        subtract_arrays(a, b)


@pytest.mark.parametrize(
    ("a", "b", "error"),
    [
        ([1, 2], [1, 2, 3], ValueError),
        (1, "a", TypeError),
    ],
)
def test_multiply_arrays_errors(a, b, error):
    with pytest.raises(error):
        multiply_arrays(a, b)


@pytest.mark.parametrize(
    ("a", "b", "error"),
    [
        ([1, 2], [1, 2, 3], ValueError),
        (1, "a", TypeError),
        ([1, 2, 3], [0, 2, 3], ZeroDivisionError),
    ],
)
def test_divide_arrays_errors(a, b, error):
    with pytest.raises(error):
        divide_arrays(a, b)


@pytest.fixture
def pair_of_lists():
    return ([10, 20, 30], [40, 50, 60])


def test_add_arrays_with_fixture(pair_of_lists):
    expect = [50, 70, 90]
    output = add_arrays(pair_of_lists[0], pair_of_lists[1])
    assert expect == output
