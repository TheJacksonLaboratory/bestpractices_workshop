def add_arrays(x, y):
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ + y_)

    return z


def subtract_arrays(x, y):
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ - y_)

    return z


def multiply_arrays(x, y):
    """TODO: Write this function."""
    pass


def divide_arrays(x, y):
    z = []
    for x_, y_ in zip(x, y):
        z.append(x_ // y_)

    return
