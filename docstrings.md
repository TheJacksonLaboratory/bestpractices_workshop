# Writing well-documented and clean code: docstrings and flake8

1. In this section, we are going to be looking at _docstrings_. Docstrings are an easy way to write reference documentation that is easy to read for both humans and computers. It includes comprehensive information about what your code does and how it does it, and it can be easily reused as part of computer-generated documentation packages such as sphinx.

2. For this guide, we will be following `numpy`'s style guide when it comes to docstrings. This guide has been adopted by a large portion of scientific Python packages, so if you decide to follow these guidelines you will quickly find that they will look like a lot of the the documentation on numpy, or pandas, or many other very popular packages.

3. Dosctrings are strings that describe a module, function or class. They can be directly accessed in Python (`object.__doc__`). For consistency purposes, we will always surround them with a triple double quote (""").

4. A good docstring should start with a one-line summary of what the object or function does. Try not to use any variable names or the name of the function in it to avoid redundancy!

5. After that, it's a good idea to have a next section with a few sentences describing your function/module/class in more detail. The idea here is to clarify functionality rather than discuss implementation details. Feel free to refer to parameter and function names, but you don't need to go into too much detail here; we will have a separate section describing the parameters.

6. Next, we should describe the function arguments and keywords. Make sure to mention their types and what each of them mean. Variable names should be enclosed in single backticks; that will ensure it will show up as code when using sphinx or other automated documentation generators. be as precise as possible when it comes to variable types and make sure to note is a specific argument is optional. When multiple input parameters have the same type, shape and description, feel free to combine them into a single descriptor.

7. Now, do the same for the return values of your function. If your function yields any values, then do the same for any yielded values. If your function raises any exceptions or warnings, make sure to have a _Raises_ and/or _Warns_ section as well.

8. If you would like to describe implementation details, this is a good place to put a _Notes_ section. If what you're doing includes equations, you can write them in LaTeX format. You can also add a _References_ section if you would like to point at specific papers where the implementation came from, for example.

9. It's good practice to include an _Examples_ section as well - this is just to show how your code would be used, not for testing! If your function has optional arguments or can be used in multiple ways, make sure to include multiple examples.

10. Now, put all the information you got together and write docstrings for the functions we have in `arrays.py`! As an example, I am adding an example docstring for `add_arrays()` below:
```
"""
    This function adds together each element of the two passed lists.
    Args:
        x : list
            The first list to add.
        y : list
            The second list to add.
    Returns:
        z : list
            The pairwise sums of ``x`` and ``y``.
    Examples:
        >>> add_arrays([1, 4, 5], [4, 3, 5])
        [5, 7, 10]
"""
```

11. Finally, while it's important to write code that _works_, it's also important to write code that can be easily maintained and understood; on that point, there are a set of guidelines outlined on [PEP 8](https://peps.python.org/pep-0008/) for the layout of your code, to improve readability and follow general conventions. Some specific software projects have their own style guidelines; the PEP 8 guidelines are very general ones.

12. There are A LOT of guidelines. I have not memorized them, and I do not expect anyone will. I have probably never run into many of them. So how do you make sure you are following them? Well, there are many tools for automatically checking your code against the guidelines. My go-to is `flake8`. You should already have it installed on your conda environment. Go ahead and run `flake8` on your repository directory and see if it returns anything. In general, the warnings raised by flake8 are pretty self-explanatory ("No newline at end of file", "Blank line contains whitespace"). In general, it is a good idea to do a flake8 pass on your code before committing or merging it!