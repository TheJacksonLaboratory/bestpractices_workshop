def add_arrays(x, y):
    """
    This function adds together each element of the two passed lists.
    Args:
        x : list
            The first list to add.
        y : list
            The second list to add
    Returns:
        z : list
            The pairwise sums of ``x`` and ``y``.
    Examples:
        >>> add_arrays([1, 4, 5], [4, 3, 5])
        [5, 7, 10]
"""
    if type(x) != list or type(y) != list:
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")

    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ + y_)

    return z


def subtract_arrays(x, y):
    """
    This function subtracts each element of the two passed lists.
    Args:
        x : list
            The list from where values will be subtracted.
        y : list
            The list with values from be subtracted from the first.
    Returns:
        z : list
            The pairwise subtractions of ``x`` and ``y``.
    Examples:
        >>> add_arrays([4, 7, 5], [2, 3, 5])
        [2, 4, 0]
"""
    if type(x) != list or type(y) != list:
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ - y_)

    return z


def multiply_arrays(x, y):
    """
    This function multiplies each element of the two passed lists.
    Args:
        x : list
            The first list to multiply.
        y : list
            The second list to multiply
    Returns:
        z : list
            The pairwise multiplications of ``x`` and ``y``.
    Examples:
        >>> add_arrays([1, 4, 5], [4, 3, 5])
        [4, 12, 25]
"""
    if type(x) != list or type(y) != list:
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ * y_)

    return z


def divide_arrays(x, y):
    """
    This function divides two passed lists element-wise.
    Args:
        x : list
            The list with numerators.
        y : list
            The list with denominators.
    Returns:
        z : list
            The pairwise divisions of ``x`` and ``y``.
    Examples:
        >>> add_arrays([6, 4, 5], [4, 2, 5])
        [1.5, 2, 1]
"""
    if type(x) != list or type(y) != list:
        raise TypeError("arguments should be arrays")
    if len(x) != len(y):
        raise ValueError("array size mismatch")
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ / y_)

    return z
