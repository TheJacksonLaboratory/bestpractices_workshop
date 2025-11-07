def add_arrays(x, y):
    """Add two lists element-wise.

    Parameters
    ----------
    x : list
        The first list to add.
    y : list
        The second list to add.

    Returns
    -------
    list
        The pairwise sums of `x` and `y`.

    Examples
    --------
    >>> add_arrays([1, 4, 5], [4, 3, 5])
    [5, 7, 10]

    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")

    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ + y_)

    return z


def subtract_arrays(x, y):
    """Subtract two lists element-wise.

    Parameters
    ----------
    x : list
        The list from which values will be subtracted.
    y : list
        The list with values to subtract from the first.

    Returns
    -------
    list
        The pairwise subtractions of `x` and `y`.

    Examples
    --------
    >>> subtract_arrays([4, 7, 5], [2, 3, 5])
    [2, 4, 0]

    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ - y_)

    return z


def multiply_arrays(x, y):
    """Multiply two lists element-wise.

    Parameters
    ----------
    x : list
        The first list to multiply.
    y : list
        The second list to multiply.

    Returns
    -------
    list
        The pairwise multiplications of `x` and `y`.

    Examples
    --------
    >>> multiply_arrays([1, 4, 5], [4, 3, 5])
    [4, 12, 25]

    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ * y_)

    return z


def divide_arrays(x, y):
    """Divide two lists element-wise.

    Parameters
    ----------
    x : list
        The list with numerators.
    y : list
        The list with denominators.

    Returns
    -------
    list
        The pairwise divisions of `x` and `y`.

    Examples
    --------
    >>> divide_arrays([6, 4, 5], [4, 2, 5])
    [1.5, 2, 1]

    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ / y_)

    return z
