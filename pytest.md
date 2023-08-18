# Running python tests with pytest

1.  In this section, we are going to be using _pytest_ to run automated tests on some code. The code we are going to be using is on the **arrays** folder. The functions that will be tested are in **arrays.py**, and the test code will go in **test_arrays.py**. Testing your code is extremely important, and it should be done WHILE you are writing it, rather than AFTER. 

2. Usual methods for testing code are doing some manual checks, such as running it over particular input files or variables and checking the results. This has limitations: it might fail to check some parts of the code, or it might fail to find errors that are not immediately obvious. In either case, it is also difficult to find exactly where your errors might be. 

3. To avoid those pitfalls, we should write a set of tests that use known inputs and check for matching with a set of expected outputs. We will write each test to run over as little of the code as possible, such that we can easily identify which parts of the code are failing. This is usually an individual function.

4. Let's start by looking into **arrays.py** and checking the **add_arrays()** function. It's a pretty simple function; it takes two arrays and add them up element-wise. Now, let's look at **test_add_arrays()** in **test_arrays.py**. How is testing being done here? Can you break it? What happens when you run `python arrays/test_arrays.py`?

5. The output of this test is not particularly useful. Imagine if you had five different functions with five different tests; would an output like `OK BROKEN OK BROKEN BROKEN` help much? Instead of that structure, we are going to use `assert` statements; `assert` is always followed by something boolean (i.e. something that will be either true or false). Empty lists, the number 0 and `None` are all false-y. If the boolean is true, nothing happens when `assert` is run; if it is false, an exception is raised. You can try running `assert 5 == 5` and `assert 5 == 6` in a python shell to see what happens. 

6. Now we are going to replace the if/else block in **test_add_arrays()** with an assert that looks like `assert output == expect`. What happens when you run `python arrays/test_arrays.py`? What if the test fails?

7. You see that now at least we get a specific line when the test fails; that's a good start! However, if we had multiple tests, code execution would be stopped at the exception thrown by `assert`. Also, we still need to explicitly call `test_add_arrays()` in that test file, which would be easy to forget, especially if we had a bunch of tests. That's where we are going to be using `pytest`!

8. Our first step is removing the call to `test_add_arrays()` from the end of **test_arrays.py**; pytest will take care of that for us. Now, in your terminal, just run `pytest`. What happened? What if the test fails?

9. `pytest` will find all files named `test_*.py` and `*_test.py` and all functions starting with names starting with `test` inside these files, and it will run those, one at a time, reporting the results of each. 

10. It's your turn; write a `test_subtract_arrays()` function that tests the `subtract_arrays()` function! What happens when you run `pytest` now?

11. Let's do the opposite now; write a `test_multiply_arrays()` function with the behavior you would expect to see from a `multiply_arrays()` function, and then write `multiply_arrays()` to make sure the tests pass! This is a process called _Test-driven development_ (TDD) - you start by writing your code requirements as tests, and then write code that passes those tests. It is a popular approach in certain kinds of software development.

12. Now imagine you want to test multiple cases in `test_add_arrays()` - positive results, negative results, zero results, for example. You could change the code in that test function to create the `a`, `b` and `expect` arrays multiple times, and do one assertion per case. However, pytest allows for a simpler possibility: using _fixtures_. That uses the decorator `@pytest.mark.parametrize()` before your test function. It takes two arguments: a string with the names of the parameters you want to pass to this function, and a list containing the values of the parameters you want to pass. So for a single case, it would look like `@pytest.mark.parametrize("a, b, expect", [([1, 2, 3], [4, 5, 6], [5, 7, 9])])`, and you could add extra tuples in there.

13. Try doing that for your test functions. Don't forget to add `a`, `b` and `expect` as arguments to your test function! What happens when you run `pytest` now? Can you find the errors in the `divide_arrays()` function with some clever testing? (hint: there are two errors)

14. So far, we have assumed that everything passed to our array functions is correct; that is rarely an assumption you can make in real life. What happens if you run `add_arrays("this is a string", 1)`? What about `add_arrays([1, 2], [1, 2, 3])`? 

15. It's time to add explicit exception handling to our functions. You will probably want to do `raise ValueError("array size mismatch")` for the case where arrays sizes are different, and `raise TypeError("arguments should be lists")` for when the arguments are not lists. 

16. Now, we can add new test functions named `test_add_arrays_error()` and so on, where we check if errors are being raised correctly. That is done by wrapping our function call with `with pytest.raises(ValueError)`, for example. What happens when you run `pytest` now? Add checks for both possible errors we came up with. What other cases can happen in e.g. `divide_arrays()`?

17. We have successfully found a way to separate the data to be tested from the code to be tested. Pytest has an even better way to do that for more complex cases (for example, when you want multiple test functions using the same data). They are called _fixtures_. A _fixture_ is defined as a function that returns the data we want to use; you use the decorator `@pytest.fixture` before the function to indicate that. After defining a fixture, you can simple use the name of the function as an argument in your test function, and that argument will assume the value that is returned by the fixture. 

18. Try creating a `pair_of_lists()` fixture and passing it to a test function. What happens when you run `pytest`? is `pair_of_lists()` run?

19. Now try running `coverage run -m pytest` followed by `coverage html` and `coverage report`. What happens? What do the results mean? Try opening the `htmlcov/index.html` file in a browser and browsing it for details.

# Optional tasks
20. Finally, let's look at the file at `.github/workflow/run_tests.yml`. This is a _Github Action_ file - it will specify actions that will happen on Github when you do some things on your repository. What is happening here? When it is triggered? Try using a file like this in one of your repositories (if you have one) or a fork of this repository, pushing a new commit to Github and checking the "actions" tab on your repository's page. 

21. Finally, try adding code coverage to your Github action. Did it work when a new commit was pushed? What was produced? 
