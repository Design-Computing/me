"""
This file has some helpful functions that are reused in other files. You don't 
need to look in this file, but you're welcome to if you want to see some more 
python in action.
"""


def minitest(f, args, expected):
    """Run a function with a list of args and print a response.

    This is a helper. Don't edit it.
    """
    result = f(*args)

    name = f.__name__
    args = str(args)[1:-1]
    result_correct = result == expected
    expected = expected
    # TODO: #14 use colorama in these to make them look really readable
    if result == None:
        print(
            f"\nExpect {name}({args}) to be {expected}, "
            "but it's None, maybe you haven't started it yet"
        )
    else:
        result_message = "✅" if result_correct else f"❌👎👎👎👎👎👎👎👎 you returned {result}"
        print(f"\nExpect {name}({args}) to be {expected} 👉 {result_message}")
        return result == expected


def little_printer(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    print(f"🔎 {exercise_name}")
    if some_kind_of_list is not None:
        if (
            type(some_kind_of_list) is list
            and len(some_kind_of_list) > 1
            and type(some_kind_of_list[0]) is list
        ):
            # true, nested list
            print("  [")
            for sub_list in some_kind_of_list:
                print(f"    {sub_list}")
            print("  ]\n")
        elif type(some_kind_of_list) is list and len(some_kind_of_list) > 1:
            # flat list
            print(f"  {some_kind_of_list}\n")
        else:
            print(some_kind_of_list)
    else:
        print("\tMaybe you haven't got to this one yet?")
