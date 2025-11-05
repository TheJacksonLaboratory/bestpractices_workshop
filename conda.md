# Working with virtual environments and conda

1. To work with Python projects, it's a good idea to use virtual environments. **Virtual environments allow you to create isolated spaces for your Python projects, each with its own set of packages and dependencies.** This way, you can avoid conflicts between different projects that may require different versions of the same package. This is particularly important in scientific computing, where you may have a long-running project that you need to keep working with, while also wanting to be able to start something new with its own dependencies.

2. At the heart of a Python environment are:
    - A Python interpreter: a specific version of Python that will be used to execute your code
    - An environment management tool: a tool to create, manage, and switch between different environments
    - A package management tool: a tool to install, update, and remove packages within an environment

3. [`Conda`](https://conda.org) is a tool that combines all three of these functionalities. It allows you to create and manage virtual environments, manage different versions of Python, and install packages. Conda is particularly popular in the scientific Python community due to its ability to handle complex system-level dependencies, such as GPU support, and its support for packages outside of the Python ecosystem (such as R, C libraries, etc).

4. There are other tools that can be used to manage virtual environments, such as [`venv`](https://docs.python.org/3/library/venv.html) (built into Python) and newer ones like [`uv`](https://docs.astral.sh/uv/) and [`pixi`](https://pixi.sh/latest/). These use a **project** oriented approach, where the environment is tied to a specific project directory. Conda, on the other hand creates and manages environments centrally, independently of any specific directory. At the end of the day, it's a matter of preference and use case, but the key take home message is to actually **always use virtual environments for your projects!**

## Installing conda, *if you don't have it already*

1.  There are several distributions of `conda` and it can pull packages from many different sources
    called "channels". In this workshop we will use the [conda-forge](https://conda-forge.org) distribution called "miniforge" (or "miniforge3"). 
    Go to the conda-forge downloads page:
    [https://conda-forge.org/download/](https://conda-forge.org/download/).  
    Download the installer for your operating system (Mac, Windows, Linux) and architecture (x86_64/amd64 or arm64/aarch64) and follow the installation instructions on that page.
    Note: When prompted whether to "automatically initialize conda", I recommend saying "yes". And on Windows, I recommend checking the options to “Create start menu shortcuts” and “Add Miniforge3 to my PATH environment variable”.

2.  Open a NEW terminal window. If you see `(base)` at the beginning of
    your prompt, you have installed it successfully. You can also run `conda --version` and see if you get a version output.

## Environments: how do they work?

1.  The `(base)` at the beginning of the line indicates which conda
    environment is currently active: the `base` environment. 
    Each environment will have its own version of Python, with its own 
    packages. Conda takes care of all dependencies and so on. 

2.  **VERY IMPORTANTLY, DO NOT INSTALL THINGS ON THE BASE ENVIRONMENT.**
    It's a sure way to make things more confusing for yourself. Anything
    you do should have its *own environment*. You should never be doing
    any work on your base environment: it's the environment `conda` uses
    to run itself, so a conflict or problem there can break your entire `conda`
    installation.

3.  So first of all, let's try to create a new, "clean" environment.
    Type `conda create -n bestpractices`. This will create a new
    environment named "bestpractices" (`-n` is shorthand for `--name`).
    Go ahead and do `conda activate bestpractices` - this should change
    the beginning of your prompt to `(bestpractices)`. We're now inside
    this new environment.
    *Always remember to activate the environment you want to use or 
    make changes to!* 

4.  Try running `python`. It probably didn't work. Why?

5.  Let's deactivate this empty environment and delete it. Do `conda
    deactivate` and `conda remove -n bestpractices --all`. Try running
    `conda env list` and you will see you have no environments.

6.  Now let's try to create an environment *with* Python. Go ahead and
    do `conda create -n bestpractices python=3.13` (or pick a version
    of your choice). Activate your new environment and try `python --version`. 
    Also try `which python`.
    This should show you a path within the newly created environment,
    under your user, rather than in a system location like
    `/bin` or `/usr/bin`.

7.  Now try running `python` and then `import numpy as np`. This
    should fail, but why?

## Installing packages in your environment

1. With a `conda` environment active, you have two options for installing Python packages:
    - Using `conda` itself: `conda install numpy`  

        This will install the package from the active conda channel, in this case `conda-forge`.
        It can be used to install packages that go beyond just Python! For a listing, see:
        [https://conda-forge.org/packages/](https://conda-forge.org/packages/)

    - Using the Python package installer `pip`: `pip install numpy`  

        This will install Python packages from [PyPI (the Python Package Index)](https://pypi.org). 
        
    Generally, you can use either method, but *mixing* them can sometimes lead to conflicts.
    If you do use both, try to install what you need using `conda` first and then use `pip` for
    packages that are not available via `conda`.

2.  Try running step 7 from above again. It should work now.

3.  Now let's deactivate and delete this environment again. Do 
    `conda deactivate` and `conda remove -n bestpractices --all`.

4.  This time, we will try to create an environment using the
    *environment.yml* in this repository. Navigate to where you cloned
    the workshop repository in your terminal and have a look at the
    contents of *environment.yml*. 

5. Now, try running `conda env create -f environment.yml`. Try
    activating the `bestpractices_final` (why is this the name?) environment and running 
    `python --version`. Try running `conda list` to see all the installed 
    packages. Everything listed at environment.yml should be there, along with all
    dependencies. 

## Some advice on projects and dependencies

Beyond using virtual environments, here are some best practices when it comes to managing dependencies for your projects:
- Keep track of every package for every module you import from in your code! Maintain either an `environment.yml` (for `conda`) or a `requirements.txt` file (for `pip`) that lists all of the dependencies needed to run your code.
- For *reproducibility*, it's a good idea to specify (pin) the *specific versions* of your dependencies you are using in your environment files.
- For *portability* and ability to incorporate your code into other projects, avoid pinning versions  strictly: pin to the minimum version required for the functionality you need.
- In addition to your environment file, for maximal reproducibility, consider generating **a lock file**, which specifies the *exact versions of all packages and their dependencies* in your environment. This can be done with `conda` using [conda-lock](https://github.com/conda/conda-lock) or with `pip` using [pip-tools](https://github.com/jazzband/pip-tools/). (Additionally, both `uv` and `pixi` automatically generate lock files.)
- If you will be sharing your code or expect others to run it, consider making a Python package. Check out the [pyOpenSci Python Package Guide](https://www.pyopensci.org/python-package-guide/index.html) for more details on how to do that!
    