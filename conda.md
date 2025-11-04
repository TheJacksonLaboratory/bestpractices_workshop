# Working with virtual environments and conda

## Installing conda

1. Before anything, open your terminal application (terminal on Mac, Command
Prompt/WSL prompt on Windows). If you are on Windows, I highly recommend using WSL (Windows Subsystem for Linux) for everything
    we are going to be doing here. These instructions will assume you are using WSL, but they apply to any terminal. Type `conda --version`. If you get a version output, you do not need to install anything. If you get an error, proceed to step 2.

2.  Conda is [an open-source package and environement management 
    system](https://conda.io/projects/conda/en/latest/index.html) for Python, R, and more. 
    There are several distributions or flavors and it can pull packages from many different sources
    called "channels". In this workshop we will use miniforge, which is the one I recommend to most people. 
    It is set up to use the community maintained ["conda-forge" channels](https://conda-forge.org/docs/user/introduction.html) which tend to have the most up-to-date packages for most platforms.  
    Go to the miniforge downloads page
    (<https://github.com/conda-forge/miniforge#miniforge3>).  
    If you are using Windows command prompt, install the executable for your system and proceed to step 5.  
    If you are using a Mac or WSL (or any Linux), copy the link to the version for your operating system (WSL users should copy the LINUX version) and proceed to step 3.

3.  On Linux, in your terminal, run `wget <address here>` with the link you just copied. 
    On macOS, in the Terminal run, `curl -L -O <address here>` with the link you just copied.
    (Note that the link should end in `.sh`.) This will download miniforge to the current directory.

4.  Run the `.sh` file you have just downloaded. This might require
    you to change its permissions (with `chmod +x <filename>`). This
    will install miniforge. Default directory is fine, if it asks if you
    want to run `conda init` say "yes".

5.  Open a NEW terminal window. If you see `(base)` at the beginning of
    your prompt, you have installed it successfully. You can also run `conda --version` and see if you get a version output.

## Environments: how do they work?

1.  The `(base)` at the beginning of the line indicates which conda
    environment is currently active. You can think of each environment
    as its own "mini-computer" for python purposes: it will have its own
    version of python, with its own packages. Conda takes care of all
    dependencies and so on.

2.  **VERY IMPORTANTLY, DO NOT INSTALL THINGS ON THE BASE ENVIRONMENT.**
    It's a sure way to make things more confusing for yourself. Anything
    you do should have its own environment. You should never be doing
    any work on your base environmen: it's the environment conda uses
    to run itself.

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
    do `conda create -n bestpractices python=3.10`. Activate your new
    environment and try `python --version`. Also try `which python`.
    This should show you a path within the newly created environment,
    under your user, rather than in a system location like
    `/bin` or `/usr/bin`.

7.  Now try running `python` and then `import numpy as np`. This
    will fail, since we do not have numpy installed in this environment.
    Exit python (run `exit()` command).

8.  One of the packages installed in this environment, together with
    python, is *pip*. Let's go ahead and do `pip install numpy`. Try
    running step 7 again. It should work now.

9.  Now let's deactivate and delete this environment again. Do 
    `conda deactivate` and `conda remove -n bestpractices --all`.

10. This time, we will try to create a conda environment for the
    *environment.yml* in this repository. Navigate to where you cloned
    the workshop repository in your terminal and have a look at the
    contents of *environment.yml*. 

11. Now, try running `conda env create -f environment.yml`. Try
    activating the `bestpractices_final` (why is this the name?) environment and running 
    `python --version`. Try running `conda list` to see all the installed 
    packages. Everything listed at environment.yml should be there, along with all
    dependencies. 
