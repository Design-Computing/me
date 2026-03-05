# -*- coding: UTF-8 -*-

"""LIST OPERATIONS AND COMPREHENSIONS

This exercise covers essential list operations in Python:
- Slicing: accessing parts of lists
- Append vs Extend: adding items to lists
- list comprehensions: elegant way to create lists

These are fundamental Python skills you'll use constantly!
"""

from set7.pets import pets


# =============================================================================
# PART 1: SLICING
# =============================================================================


def first_ten_pets() -> list[str]:
    """Return the first 10 pets from the pets list.

    Hint: Use slicing with [:10]

    Returns:
        list: First 10 pets
    """
    pass


def last_five_pets() -> list[str]:
    """Return the last 5 pets from the pets list.

    Hint: You can use negative indices! [-5:]

    Returns:
        list: Last 5 pets
    """
    pass


def pets_from_4_to_10() -> list[str]:
    """Return pets from index 4 to 10 (exclusive).

    Remember: [start:end] doesn't include the end index

    Returns:
        list: Pets from index 4 to 9
    """
    pass


def middle_pets() -> list[str]:
    """Return the middle 20 pets.

    Hint: The list has 40 items. Middle 20 means skip first 10, take next 20.
    You can use [10:30]

    Returns:
        list: Middle 20 pets
    """
    pass


def moving_middle_pets() -> list[str]:
    """Return the middle 20 pets from a list of unknown length.

    Hint: The list has an unknown number of items. To get the middle 20, you
    need to calculate the start and end indices based on the length of the list.

    Returns:
        list: Middle 20 pets
    """
    pass


def reverse_pets() -> list[str]:
    """Return the pets list in reverse order.

    Hint: Use [::-1] to reverse a list!
    The -1 means "step backwards"

    Returns:
        list: All pets in reverse order
    """
    pass


def every_third_pet() -> list[str]:
    """Return every third pet from the list.

    Hint: [::3] means "start at beginning, step by 3"

    Returns:
        list: Every 3rd pet
    """
    pass


# =============================================================================
# PART 2: APPEND VS EXTEND
# =============================================================================


def append_example() -> list[str]:
    """Demonstrate append by adding a single item to a list.

    Use .append() to add the string "hamster" to the my_pets list.
    Then append another string "rabbit".

    Returns:
        list: A list with four items ["cat", "dog", "hamster", "rabbit"]
    """
    my_pets = ["cat", "dog"]

    return my_pets


def extend_example() -> list[str]:
    """Demonstrate extend by adding multiple items to a list.

    Use .extend() to add ["hamster", "rabbit"] to the my_pets list.
    Then extend with ["guinea pig", "mouse"].

    Returns:
        list: A list with six items ["cat", "dog", "hamster", "rabbit", "guinea pig", "mouse"]
    """
    my_pets = ["cat", "dog"]

    return my_pets


def append_vs_extend_comparison() -> tuple[list, list[str]]:
    """Show the difference between append and extend.

    For list1:
    - Use .append() to add the list ["cat", "dog"]
      (this adds the list as a single item)

    For list2:
    - Use .extend() to add the list ["cat", "dog"]
      (this adds each item from the list)

    Returns:
        tuple: (list1, list2) to see the difference

    Expected result:
        list1 = [["cat", "dog"]]  # nested list
        list2 = ["cat", "dog"]    # flat list
    """
    list1 = []
    list2 = []

    return (list1, list2)


# =============================================================================
# PART 3: LIST COMPREHENSIONS
# =============================================================================


def pet_name_lengths() -> list[int]:
    """Return a list of the lengths of each pet name.

    Use a list comprehension!

    Example: ["dog", "cat"] -> [3, 3]

    Hint: [len(p) for p in pets]

    Returns:
        list: Length of each pet name
    """
    pass


def long_pet_names() -> list[str]:
    """Return only pets whose names are longer than 10 characters.

    Use a list comprehension with a condition!

    Syntax: [item for item in list if condition]

    Returns:
        list: Pets with names longer than 10 chars
    """
    pass


def pet_names_uppercase() -> list[str]:
    """Return all pet names in uppercase.

    Use a list comprehension with .upper()

    Returns:
        list: All pet names in UPPERCASE
    """
    pass


def pets_starting_with_g() -> list[str]:
    """Return all pets whose names start with 'g'.

    Use a list comprehension with a condition.

    Hint: string.startswith('g')

    Returns:
        list: Pets starting with 'g'
    """
    pass


def pet_name_and_length() -> list[tuple[str, int]]:
    """Return a list of tuples with (name, length) for each pet.
    Where name is the pet name and length is the length of the string.

    Use a list comprehension to create tuples.

    Example: [("dog", 3), ("mouse", 5), ...]

    Hint: [(p, len(p)) for p in pets]

    Returns:
        list: list of (name, length) tuples
    """
    pass


# =============================================================================
# BONUS CHALLENGE
# =============================================================================


def nested_list_comprehension() -> list[list[str]]:
    """Create a 2D list (matrix) using nested list comprehensions.

    Create a 5x5 grid where each cell contains its coordinates as a string.

    You've seen this before, but can you do it with a nested list comprehension
    instead of loops?

    In real life, I strongly recomend that you never do this, but it's a good
    exercise to understand how nested comprehensions work.

    Example output:
    [
        ["(0,0)", "(0,1)", "(0,2)", "(0,3)", "(0,4)"],
        ["(1,0)", "(1,1)", "(1,2)", "(1,3)", "(1,4)"],
        ...
    ]

    Hint: [[f"({i},{j})" for j in range(5)] for i in range(5)]

    Returns:
        list: 5x5 grid of coordinate strings
    """
    pass


if __name__ == "__main__":
    print("First 10 pets:", first_ten_pets())
    print("\nLast 5 pets:", last_five_pets())
    print("\nPet name lengths:", pet_name_lengths()[:10])  # First 10
    print("\nLong pet names:", long_pet_names())
    print("\nPets starting with 'g':", pets_starting_with_g())
