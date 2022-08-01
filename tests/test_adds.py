import pytest
from src import add_functions


def test_add_one():
    assert add_functions.add_one(1) == 2
