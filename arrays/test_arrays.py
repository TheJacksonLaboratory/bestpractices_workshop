from arrays import add_arrays
import pytest

def test_add_arrays():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expect = [5, 7, 9]

    output = add_arrays(a, b)

    if output == expect:
        print("OK")
    else:
        print("BROKEN")


test_add_arrays()
