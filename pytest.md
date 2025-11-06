# Running python tests with pytest

1.  In this section, we are going to be using _pytest_ to run automated tests on some code. The code we are going to be using is on the **arrays** folder. The functions that will be tested are in **arrays.py**, and the test code will go in **test_arrays.py**. Testing your code is extremely important, and it should be done WHILE you are writing it, rather than AFTER. 

2. Usual methods for testing code are doing some manual checks, such as running it over particular input files or variables and checking the results. This has limitations: it might fail to check some parts of the code, or it might fail to find errors that are not immediately obvious. In either case, it is also difficult to find exactly where your errors might be. 

3. To avoid those pitfalls, we should write a set of tests that use known inputs and check for matching with a set of expected outputs. We will write each test to run over as little of the code as possible, such that we can easily identify which parts of the code are failing. This type of test is called a "unit test", in contrast to "integration tests" that test multiple parts of the code at once. Tip: break long, complex functions with multiple control structures (e.g. if/else, for, while) into smaller functions that do one thing each to make your code easier to read, test, and maintain.

4. Let's start by looking into **arrays.py** and checking the **add_arrays()** function. It's a pretty simple function; it takes two arrays and add them up element-wise. Now, let's look at **test_add_arrays()** in **test_arrays.py**. How is testing being done here? Can you break it? What happens when you run `python arrays/test_arrays.py`?

5. The output of this test is not particularly useful. Imagine if you had five different functions with five different tests; would an output like `OK BROKEN OK BROKEN BROKEN` help much? Instead of that structure, we are going to use `assert` statements; `assert` is always followed by something boolean (i.e. something that will be either true or false). Empty lists, the number 0 and `None` are all false-y. If the boolean is true, nothing happens when `assert` is run; if it is false, an exception is raised. You can try running `assert 5 == 5` and `assert 5 == 6` in a python shell to see what happens. 

6. Now we are going to replace the if/else block in **test_add_arrays()** with an assert that looks like `assert output == expect`. What happens when you run `python arrays/test_arrays.py`? What if the test fails?

7. You see that now at least we get a specific line when the test fails; that's a good start! However, if we had multiple tests, code execution would be stopped at the exception thrown by `assert`. Also, we still need to explicitly call `test_add_arrays()` in that test file, which would be easy to forget, especially if we had a bunch of tests. That's where we are going to be using `pytest`!

8. Our first step is removing the call to `test_add_arrays()` from the end of **test_arrays.py**; pytest will take care of that for us. Now, in your terminal, just run `pytest`. What happened? What if the test fails?

9. `pytest` will find all files named `test_*.py` and `*_test.py` and all functions starting with names starting with `test` inside these files, and it will run those, one at a time, reporting the results of each. 

10. It's your turn; write a `test_subtract_arrays()` function that tests the `subtract_arrays()` function! What happens when you run `pytest` now?

11. Let's do the opposite now; write a `test_multiply_arrays()` function with the behavior you would expect to see from a `multiply_arrays()` function, and then write `multiply_arrays()` to make sure the tests pass! This is a process called _Test-driven development_ (TDD) - you start by writing your code requirements as tests, and then write code that passes those tests. It is a popular approach in certain kinds of software development.

12. Now imagine you want to test multiple cases in `test_add_arrays()` - positive results, negative results, zero results, for example. You could change the code in that test function to create the `a`, `b` and `expect` arrays multiple times, and do one assertion per case. However, pytest allows for a simpler possibility: parameterizing inputs to your test. You can do this using the decorator [`@pytest.mark.parametrize()`](https://docs.pytest.org/en/stable/how-to/parametrize.html) before your test function. It takes two arguments: a string with the *names* of the parameters you want to pass to this function (comma separated), and a *list* containing *tuples* of values of the parameters you want to pass. So for a single case, it would look like `@pytest.mark.parametrize("a, b, expect", [([1, 2, 3], [4, 5, 6], [5, 7, 9])])`, and you could add extra tuples for additional test cases. Then all you need to do is add `a`, `b` and `expect` as arguments to your test function.

13. Try doing that for your test functions. What happens when you run `pytest` now? Can you find the errors in the `divide_arrays()` function with some clever testing? (hint: there are two errors)

14. So far, we have assumed that everything passed to our array functions is correct; that is rarely an assumption you can make in real life. What happens if you run `add_arrays("this is a string", 1)`? What about `add_arrays([1, 2], [1, 2, 3])`? 

15. It's time to add explicit exception handling to our functions. You will probably want to do `raise ValueError("array size mismatch")` for the case where arrays sizes are different, and `raise TypeError("arguments should be lists")` for when the arguments are not lists. 

16. Now, we can add new test functions named `test_add_arrays_error()` and so on, where we check if errors are being raised correctly. That is done by wrapping our function call with `with pytest.raises(ValueError)`, for example. What happens when you run `pytest` now? Add checks for both possible errors we came up with. What other cases can happen in e.g. `divide_arrays()`?

17. We have successfully found a way to separate the data to be tested from the code to be tested. `pytest` has an even better way to do that for more complex cases, for example, when you want multiple test functions using the same data. They are called [_fixtures_](https://docs.pytest.org/en/stable/explanation/fixtures.html#about-fixtures). A _fixture_ is defined as a function that returns something we want to use repeatedly in our tests. `pytest` provides [some fixtures out of the box](https://docs.pytest.org/en/stable/reference/fixtures.html), like the very useful `tmp_path` fixture that gives you a unique temporary location. But you can also create your own: fixtures can be used to set up test data, create mock objects, or perform any other setup tasks that are needed for your tests. To define a fixture, you use the decorator `@pytest.fixture` before a function. After defining a fixture, you can pass the name of the function as an argument in your test function, and that argument will assume the value that is returned by the fixture. 

18. Try creating a `pair_of_lists()` fixture and passing it to a test function. What happens when you run `pytest`? is `pair_of_lists()` run?


## Test coverage

1. When writing tests, it's important to know how much of your code is actually being tested by your test suite. This is called **code coverage**. Code coverage is a metric that tells you what percentage of your code is run ("covered") when your tests are executed. High coverage means most of your code is tested, while low coverage means there are many untested parts, where bugs could hide.

2. The most common tool for measuring code coverage in Python is [`coverage`](https://coverage.readthedocs.io/). You can run it from the command line to see how much of your code is covered by your tests.

3. To use `coverage` with ``pytest, run:
	```sh
	coverage run -m pytest
	```
	This will run your tests and collect coverage data.

4. To see a summary in your terminal, run:
	```sh
	coverage report
	```

5. To generate a detailed HTML report you can view in your browser, run:
	```sh
	coverage html
	```
	Then open the file `htmlcov/index.html` in your browser to explore which lines of code are covered and which are not.

6. Reviewing your coverage report can help you identify untested code and improve your test suite.

## More advanced testing

1. `pytest` offers extensive features to make testing your code easier, so check out [the `pytest` documentation](https://docs.pytest.org/en/stable/index.html). 

2. The [`unittest.mock` module](https://docs.python.org/3/library/unittest.mock.html) is also very useful for testing more complex code. It allows you to create mock objects needed by your code and then make assertions about how they have been used. You can even "patch" objects with your mocks. When unit testing, the idea is to test only the code that you own. Mocks are particularly useful for testing code that interacts with external systems, such as databases or web services.

3. There is also [the `pytest` "monkeypatching" fixture](https://docs.pytest.org/en/stable/how-to/monkeypatch.html), which allows you to safely set/delete an attribute, dictionary item or environment variable, or even modify `sys.path` for importing.

4. `pytest` has an extensive ecosystem of plugins that can help you with specific testing needs. For example, there are plugins for testing web applications, databases, and more. You can find a list of available plugins on the [pytest website](https://docs.pytest.org/en/stable/reference/plugin_list.html).

5. Finally, you can consider using [hypothesis](https://hypothesis.readthedocs.io/en/latest/), a property-based testing library that will generate random input data based on specified properties. This can help you find edge cases and unexpected behavior in your code that you might not have thought of when writing traditional unit tests.

## Automated testing

1. If you're using GitHub for your code repositories, you can set up automated testing so that your tests are run automatically whenever you push new code or open a pull request. This is done using GitHub Actions, which allows you to define workflows that run on specific events.

2. Let's look at the file at `.github/workflow/run_tests.yml`. This is a _Github Action_ file - it will specify actions that will happen on Github when you do some things on your repository. What is happening here? When it is triggered? Try using a file like this in one of your repositories (if you have one) or a fork of this repository, pushing a new commit to Github and checking the "actions" tab on your repository's page. 

3. Finally, try adding code coverage to your Github action. Did it work when a new commit was pushed? What was produced? 
