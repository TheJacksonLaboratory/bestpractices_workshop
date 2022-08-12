# Working with virtual environments and conda

## Installing miniconda

1.  If you are on Windows, I highly recommend using WSL2 for everything
    we are going to be doing here (except github stuff). These
    instructions will assume you are using WSL2.

2.  Go to the miniconda downloads page
    (<https://docs.conda.io/en/latest/miniconda.html>) and copy the link
    to the version for your OS (note that if you are using WSL, you
    should copy the one for LINUX).

3.  On your terminal, do `wget <address here>`. This will download
    miniconda to the current directory.

4.  Run the `.sh` file you have just downloaded. This might require
    you to change its permissions (with `chmod +x <filename>`). This
    will install miniconda. Default directory is fine, if it asks if you
    want to run `conda init` say "yes".

5.  Open a new terminal window. If you see `(base)` at the beginning of
    your prompt, you have installed it successfully.

## Environments: how do they work?

1.  The `(base)` at the beginning of the line indicates which conda
    environment is currently active. You can think of each environment
    as its own "mini-computer" for python purposes: it will have its own
    version of python, with its own packages. Conda takes care of all
    dependencies and so on.

2.  **VERY IMPORTANTLY, DO NOT INSTALL THINGS ON THE BASE ENVIRONMENT.**
    It's a sure way to make things more confusing for yourself. Anything
    you do should have its own environment. You should never be doing
    any work on your base environment.

3.  So first of all, let's try to create a new, "clean" environment.
    Type `conda create -n bestpractices`. This will create a new
    environment named "bestpractices". Go ahead and do `conda activate
    bestpractices` - this should change the beginning of your prompt
    to `(bestpractices)`. We're now inside this new environment.

4.  Try running `python`. It won't work. Why?

5.  Let's deactivate this empty environment and delete it. Do `conda
    deactivate` and `conda remove --all -n bestpractices`. Try running
    `conda env list` and you will see you have no environments.

6.  Now let's try to create an environment *with* Python. Go ahead and
    do `conda create -n bestpractices python=3.7`. Activate your new
    environment and try `python --version`.

7.  Now try running `python` and then `import numpy as np`. This
    will fail, since we do not have numpy installed in this environment.
    Exit python.

8.  One of the packages installed in this environment, together with
    python, is *pip*. Let's go ahead and do `pip install numpy`. Try
    running step 7 again. It should work now.

9.  Now let's deactivate and delete this environment again. Do 
    `conda deactivate` and `conda remove --all -n bestpractices`.

10. This time, we will try to create a conda environment for the
    *environment.yml* in this repository. Navigate to where you cloned
    the workshop repository in your terminal and have a look at the
    contents of *environment.yml*. 

11. Now, try running `conda env create -f environment.yml`. Try
    activating the bestpractices environment and running 
    `python --version`. Try running `pip freeze` to see all the installed 
    packages. Everything listed at environment.yml should be there. 
