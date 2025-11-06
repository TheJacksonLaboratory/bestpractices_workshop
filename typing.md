# Writing type-safe and readable code: Python type hints

1. In this section, we will look at _type hints_. Type hints are a way to annotate your Python code with information about the expected types of variables, function arguments, and return values. *Python is dynamically typed, so this is not required.* However, type hints help both humans and tools understand your code, catch bugs early, and improve code readability and maintainability. Type hints are part of the Python standard library since Python 3.5. For more details, see [PEP484 which introduced type hints](https://peps.python.org/pep-0484/) and the [`typing` module documentation](https://docs.python.org/3/library/typing.html). Importantly, type hints **do not change the runtime behavior of your code**; they are simply annotations.

2. Why use type hints?
    - **Clarity:** Type hints make it clear what types your functions expect and return.
    - **Early error detection:** Tools like `mypy` can check your code for type errors before you run it.
    - **Better IDE support:** Many editors use type hints for autocompletion and inline documentation.

3. Type hints use the `:` syntax for variables and function arguments, and `->` for return types. For example:
    ```python
    # Variable annotation
    a: int = 5

    # Function annotation
    def add(x: int, y: int) -> int:
        """
        Return the sum of two integers.

        Parameters
        ----------
        x : int
            First integer to add.
        y : int
            Second integer to add.

        Returns
        -------
        int
            The sum of `x` and `y`.

        Examples
        --------
        >>> add(2, 3)
        5
        """
    ```

4. Examples of common types you may use in Python 3.9 and later:
    - `int`, `float`, `str`, `bool`: Basic types
    - `list`, `dict`, `set`, `tuple`: Collection types. 

    These can be combined using bracket notation like: `list[int]`, `dict[str, float]`, etc.

    You can also import additional types from the [`typing` module](https://docs.python.org/3/library/typing.html#) or other modules you use

5. Type hints are not enforced at runtime, but you can use tools like [`mypy`](https://mypy-lang.org/) to check your code for type errors. To check your code, run:
    ```
    mypy your_script.py
    ```
    Mypy will report any type mismatches it finds, helping you catch bugs before they happen.

6. If you want to learn more, check out:
    - [Python typing documentation](https://docs.python.org/3/library/typing.html)
    - [mypy Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
