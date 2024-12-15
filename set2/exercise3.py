# -*- coding: UTF-8 -*-

"""
Welcome to exercise 3 of set 2.

Modify each function until the tests pass.
"""


def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    Look into modulo division using the '%' operator as one way of doing this.

    e.g. 4 % 2 = 0
        13 % 12 = 1
         3 % 2 = 1

    So if a_number modulo two is zero, then it's even.
    """
    return a_number %2 != 0

def fix_it(moves=True, should_move=True):
    """Decide what to do.

    Using the engineering flowchart (in week2 folder of the CODE1161-2019
    repo engineeringFlowchart.png) for the rules, return the apropriate
    response to the input parameters.
    Use conditional statements: if, else, elif etc.
    This function should return either:
    "WD-40"
    "Duct Tape"
    "No Problem"

    Most people write this function with 4 return statements.
    As an extra challenge, see if you can get that down to three.
    """
    if moves and should_move:
        return "No Problem"
    elif moves and not should_move:
        return "Duct Tape"
    elif not moves and not should_move:
        return "No Problem"
    elif not moves and should_move: 
        return "WD-40"
    

def loops_preview():
    """Make 8 poops.
    Using a for loop
    return a list of 8 items, each one a string with exacly one 💩 in it.
    E.g.: ['💩', '💩', '💩', '💩', '💩', '💩', '💩', '💩']
    """
    choc_list = []
    for i in range(8):
        choc_list.append("💩")
    return choc_list


def loops_1a():
    """Make 10 stars.

    Using a for loop
    return a list of 10 items, each one a string with exacly one star in it.
    E.g.: ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    """
    star_list = []
    for i in range(10):
        star_list.append("*")
    return star_list


def loops_1c(number_of_items=5, symbol="#"):
    """Respond to variables.

    Return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']

    Remember that you're being passed arguments here. Don't hard code the number
    or the symbol, let it be whatever it wants to be.
    """
    hash_list = []
    for i in range(number_of_items):
        hash_list.append(symbol)
    return hash_list


def loops_2_preview():
    """Make a big square 💩field.

    return a list of 4 items, each one a list of 4 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
            ['💩', '💩', '💩', '💩'],
          ]
    """
    field = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append("💩")
        field.append(row)
    return field


def loops_2():
    """Make a big square starfield.

    return a list of 10 items, each one a list of 10 items,
    each one of those, a string with exacly one star in it.
    E.g.: [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
          ]
    """
    field = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append("*")
        field.append(row)
    return field
        


def loops_3():
    """Make a rising block of numbers.

    Return this:
    [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
        ['3', '3', '3', '3', '3', '3', '3', '3', '3', '3'],
        ['4', '4', '4', '4', '4', '4', '4', '4', '4', '4'],
        ['5', '5', '5', '5', '5', '5', '5', '5', '5', '5'],
        ['6', '6', '6', '6', '6', '6', '6', '6', '6', '6'],
        ['7', '7', '7', '7', '7', '7', '7', '7', '7', '7'],
        ['8', '8', '8', '8', '8', '8', '8', '8', '8', '8'],
        ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
    ]
    remember that range(10) produces a list of numbers from 0...9
    So for every step produced by `for i in range(10):` i is a different number
    TIP: notice that this needs to to return strings of numbers,
         so call str(number) to cast.
    """
    number_square = []
    for i in range(10):
        number_row =[]
        for j in range(10):
            number_row.append(str(i))
        number_square.append(number_row)
    return number_square


def loops_4():
    """Make a block of numbers that rises left to right.

    Return this:
    [
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    """
    number_square = []
    for i in range(10):
        number_row =[]
        for j in range(10):
            number_row.append(str(j))
        number_square.append(number_row)
    return number_square


def loops_5():
    """Make the coordinates of the block.

    Return this:
    [
      ["(i0, j0)", "(i0, j1)", "(i0, j2)", "(i0, j3)", "(i0, j4)"],
      ["(i1, j0)", "(i1, j1)", "(i1, j2)", "(i1, j3)", "(i1, j4)"],
      ["(i2, j0)", "(i2, j1)", "(i2, j2)", "(i2, j3)", "(i2, j4)"],
      ["(i3, j0)", "(i3, j1)", "(i3, j2)", "(i3, j3)", "(i3, j4)"],
      ["(i4, j0)", "(i4, j1)", "(i4, j2)", "(i4, j3)", "(i4, j4)"],
      ["(i5, j0)", "(i5, j1)", "(i5, j2)", "(i5, j3)", "(i5, j4)"],
      ["(i6, j0)", "(i6, j1)", "(i6, j2)", "(i6, j3)", "(i6, j4)"],
      ["(i7, j0)", "(i7, j1)", "(i7, j2)", "(i7, j3)", "(i7, j4)"],
      ["(i8, j0)", "(i8, j1)", "(i8, j2)", "(i8, j3)", "(i8, j4)"],
      ["(i9, j0)", "(i9, j1)", "(i9, j2)", "(i9, j3)", "(i9, j4)"]
    ]

    TIP:
    If you've got num_bottles, e.g. num_bottles = 8
    You can construct strings either by concatinating them:
        "There are " + str(num_bottles) + " green bottles"
    or by using format:
        "There are {} green bottles".format(num_bottles)
    or, my favourite, f-strings:
        f"There are {num_bottles} green bottles"
    you'll come to see the pros and cons of each over time.
    """
    number_square = []
    for i in range(10):
        coordinate_row =[]
        for j in range(5):
            coordinate_row.append("(i{}, j{})".format(i, j))
        number_square.append(coordinate_row)
    return(number_square)



def loops_6():
    """Make a wedge of numbers.

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]
    You don't have to use a literal number in the range function.
    You can use a variable.
    TIP: look out for the starting condition.
    """
    wedge = []
    for i in range(10):
        row =[]
        for j in range(i + 1):
            row.append(str(j))
        wedge.append(row)
    return(wedge)


def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """
def loops_7():
    pyramid = []
    for i in range(5):
        row = []
        for j in range(9):
            if j >= 4 - i and j <= 4 + i:
                row.append('*')
            else:
                row.append(' ')
        pyramid.append(row)
    return pyramid

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    try:
        from helper import little_printer, minitest
        minitest(is_odd, [1], True)
        minitest(is_odd, [4], False)
        minitest(fix_it, [True, True], "No Problem")
        minitest(fix_it, [True, False], "WD-40")
        minitest(fix_it, [False, True], "Duct Tape")
        minitest(fix_it, [False, False], "No Problem")
        little_printer(loops_preview(), "loops_preview")
        little_printer(loops_1a(), "loops_1a")
        little_printer(loops_1c(4, "×°×"), "loops_1c")
        little_printer(loops_2_preview(), "loops_2_preview")
        little_printer(loops_2(), "loops_2")
        little_printer(loops_3(), "loops_3")
        little_printer(loops_4(), "loops_4")
        little_printer(loops_5(), "loops_5")
        little_printer(loops_6(), "loops_6")
        little_printer(loops_7(), "loops_7")
    except ModuleNotFoundError as e:
        print("⚠"*20, "\nWe're looking for a module that's missing. That's probably a problem that a tutor needs to figure out.\n")
        print(e)
        print("⚠"*20)
