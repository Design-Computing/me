# -*- coding: UTF-8 -*-
"""Modify each function until the tests the_answer = None

    return the_answer.

The command to run the tests is:

python ../course/set2/tests.py


In each function, where you see:

    the_answer = None

replace None with the actual answer.

"""


def add_1(a_number):
    """Return a number that is 1 bigger than number given.

    This isn't a trick!

    This is an example function to get you started.
    Run the tests now and this one should go green. Free marks!
    """
    the_answer = a_number + 1

    return the_answer


def add_5(a_number):
    """Return a number that is 5 bigger than number given.

    This isn't a trick!
    First thing to do is to remove the the_answer = None

    return the_answer. That's just tellign python that
    the empty block is intentional - it's python's "this page is intentionally
    left blank"
    Then you need to:
        return a_number plus five
    except expressed in python, not english
    """
    the_answer = None

    return the_answer


def adder(a_number, another_number):
    """Add two numbers.

    Same as above, but with any two numbers.
    """
    the_answer = None

    return the_answer


def shout(a_string):
    """Return a string in uppercase.

    look up the docs for string methods. Either in the official docs, here:
        https://docs.python.org/3/library/string.html
    or in any of the million places that google will give you.
    "python make a string uppercase" is a good starting search query.
    HINT: there are a few things with upper case in their description, but
          they all do different things. You'll need to actually read the
          docs to find out which one you actually need.
    """
    the_answer = None

    return the_answer


def really_shout(a_string):
    """Return a string in uppercase, with an exclamation mark on the end.

    In the spirit of being DRY (don't repeat yourself) reuse the shout() function
    from above.
    You could do this by copying the code, but the tests are checking to see
    that you've reused the function you already wrote.
    Look up how to 'concatinate' strings to make this happen.
    """
    the_answer = None

    return the_answer


def shout_with_a_number(a_string, a_number):
    """Return a string in uppercase with a space and a_number concatentated.
    E.g.
    >>> shout_with_a_number('hello', 42)
    'HELLO 42'

    HINT: Lookup how to cast a_number to a string or lookup how to use
          string formatting in python.
          There are a few ways to do this, so if you're looking for a
          challenge, see if you can make the test pass with at least two ways
          of doing the same job.
    """
    the_answer = None

    return the_answer


"""#################################
You don't need to worry about anything below here. 
It's there to easily test your code from inside this file 
so that you can use the debugger more easily.
   #################################"""


def minitest(f, args, expected):
    """Run a function with a list of args and print a response.

    This is a helper. Don't edit it.
    """
    result = f(*args)

    name = (f.__name__,)
    args = (str(args)[1:-1],)
    result = (result == expected,)
    expected = (expected,)
    print(f"expect {name}({args}) to be {expected} => {result}")
    return result == expected


if __name__ == "__main__":
    """This code runs when you run this file."""

    print(
        """
          This section does a quick test on your results and prints them nicely
          It's NOT the official tests, they are in tests.py as usual.
          Add to these tests if you want, give them arguments etc. to make sure that your
          code is robust to the situations that you'll see in action.

          the format is: minitest(function_name, [list, of, arguments], expected_result)

          REMEMBER: these aren't the tests that you submit, these are just
          there to keep you sane."""
    )

    minitest(add_1, [1], 2)
    minitest(add_5, [1], 6)
    minitest(add_5, [6], 11)
    minitest(add_5, [-3], 2)
    minitest(add_5, [0.5], 5.5)
    minitest(adder, [-0.5, -0.5], -1)
    minitest(adder, [2, 2], 4)
    minitest(adder, [2, -2], 0)
    minitest(shout, ["hello"], "HELLO")
    minitest(really_shout, ["hello"], "HELLO!")
    minitest(really_shout, [""], "!")
    minitest(really_shout, ["!"], "!!")
    minitest(shout_with_a_number, ("hello", 42), "HELLO 42")
    print("p.s. see note above these results")
