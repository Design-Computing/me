# -*- coding: UTF-8 -*-

"""FUNCTIONS, LAMBDAS, AND BUILT-INS

This exercise covers functional programming concepts and Python built-ins:
- Lambda functions: anonymous one-line functions
- Map and filter: applying functions to sequences
- Built-in functions: max, min, sum, zip, enumerate
- Practical use cases for all of these

These make your code more concise and "Pythonic"!
"""

from random import randint

from set7.pets import pets

numbers = [randint(1, 100) for _ in range(20)]


# =============================================================================
# PART 1: LAMBDA FUNCTIONS WITH SORTED
# =============================================================================
# Lambdas are anonymous functions - small, one-line functions used inline.
# They're perfect for simple operations you don't want to write a full def for!
# One common use: custom sorting with sorted()


def sort_pets_by_length() -> list[str]:
    """Sort pets by name length using a lambda.

    Lambda syntax: lambda parameter: expression
    Example: lambda x: len(x)

    sorted() can take a key parameter with a lambda!

    Hint: sorted(pets, key=lambda p: len(p))

    Returns:
        list: Pets sorted by name length (shortest first)
    """
    pass


def sort_pets_by_last_letter() -> list[str]:
    """Sort pets by their last letter using a lambda.

    Hint: lambda p: p[-1]

    Returns:
        list: Pets sorted by last letter
    """
    pass


def sort_pets_reverse_alphabetical() -> list[str]:
    """Sort pets in reverse alphabetical order.

    You can combine sorted() with reverse=True!

    Hint: sorted(pets, reverse=True)

    Returns:
        list: Pets sorted Z to A
    """
    pass


# =============================================================================
# PART 2: MAP FUNCTION
# =============================================================================


def map_double_numbers() -> list[int]:
    """Use map with a lambda to double all numbers in the numbers list.

    map() applies a function to each item in a sequence.

    Syntax: list(map(function, sequence))

    Note: map() returns a map object, convert it to a list!

    Returns:
        list: All numbers doubled
    """
    pass


def map_pet_lengths() -> list[int]:
    """Use map to get the length of each pet name.

    You can use map with the built-in len function!

    Syntax: list(map(len, pets))

    Returns:
        list: Length of each pet name
    """
    pass


def map_first_letter() -> list[str]:
    """Use map with a lambda to get the first letter of each pet name.

    Hint: lambda p: p[0]

    Returns:
        list: First letter of each pet name
    """
    pass


def map_uppercase() -> list[str]:
    """Use map to convert all pet names to uppercase.

    Hint: You can use lambda p: p.upper() or just use str.upper directly!

    Returns:
        list: All pet names in uppercase
    """
    pass


# =============================================================================
# PART 3: FILTER FUNCTION
# =============================================================================


def filter_long_names() -> list[str]:
    """Use filter to get only pets with names longer than 10 characters.

    filter() keeps only items where the function returns True.

    Syntax: list(filter(function, sequence))

    Returns:
        list: Pets with long names
    """
    pass


def filter_even_numbers() -> list[int]:
    """Use filter to get only even numbers from the numbers list.

    Hint: lambda x: x % 2 == 0

    Returns:
        list: Only even numbers
    """
    pass


def filter_pets_with_space() -> list[str]:
    """Use filter to get pets whose names contain a space.

    Hint: lambda p: ' ' in p

    Returns:
        list: Pets with spaces in their names
    """
    pass


# =============================================================================
# PART 4: BUILT-IN FUNCTIONS
# =============================================================================


def find_longest_pet_name() -> str:
    """Find the longest pet name using max().

    max() can take a key parameter!

    Syntax: max(sequence, key=function)
    Example: max(pets, key=len)

    Returns:
        str: The longest pet name
    """
    pass


def find_shortest_pet_name() -> str:
    """Find the shortest pet name using min().

    Returns:
        str: The shortest pet name
    """
    pass


def find_max_number() -> int:
    """Find the maximum number in the numbers list.

    Simple: max(numbers)

    Returns:
        int: The largest number
    """
    pass


def find_min_number() -> int:
    """Find the minimum number in the numbers list.

    Returns:
        int: The smallest number
    """
    pass


def sum_all_numbers() -> int:
    """Calculate the sum of all numbers.

    Use the built-in sum() function!

    Returns:
        int: Sum of all numbers
    """
    pass


def average_number() -> float:
    """Calculate the average of all numbers.

    Average = sum / count

    Returns:
        float: Average of numbers
    """
    pass


# =============================================================================
# PART 5: ZIP FUNCTION
# =============================================================================


def zip_pets_with_numbers() -> list[tuple[str, int]]:
    """Use zip to pair each pet with a number.

    zip() combines multiple sequences into tuples.

    Syntax: list(zip(sequence1, sequence2))

    Returns:
        list: list of (pet, number) tuples
    """
    pass


def create_pet_dictionary() -> dict[str, int]:
    """Create a dictionary mapping pets to numbers using zip.

    You can convert zipped tuples directly to a dict!

    Syntax: dict(zip(keys, values))

    Returns:
        dict: dictionary of pet -> number
    """
    pass


# =============================================================================
# PART 6: ENUMERATE FUNCTION
# =============================================================================


def enumerate_pets() -> list[tuple[int, str]]:
    """Use enumerate to get (index, pet) pairs.

    enumerate() gives you index and value together!

    Syntax: list(enumerate(sequence))

    Returns:
        list: list of (index, pet) tuples
    """
    pass


def enumerate_from_one() -> list[tuple[int, str]]:
    """Use enumerate starting from 1 instead of 0.

    enumerate() takes an optional start parameter!

    Syntax: list(enumerate(sequence, start=1))

    Returns:
        list: list of (index, pet) tuples starting from 1
    """
    pass


def find_pet_positions() -> list[int]:
    """Find the positions (indices) of all pets starting with 'g'.

    Use enumerate in a list comprehension!

    Hint: [i for i, p in enumerate(pets) if p.startswith('g')]

    Returns:
        list: Indices of pets starting with 'g'
    """
    pass


# =============================================================================
# BONUS CHALLENGES
# =============================================================================


def combine_map_filter() -> list[str]:
    """First filter for long names, then map to uppercase.

    You can chain operations!
    Hint: You can nest functions or use intermediate variables.

    Returns:
        list: Long pet names (>10 chars) in uppercase
    """
    pass


def complex_sort() -> list[str]:
    """Sort pets by: 1) length, 2) alphabetically if same length.

    You can use tuples in the key function!
    When sorted by tuple, it sorts by first element, then second, etc.

    Hint: sorted(pets, key=lambda p: (len(p), p))

    Returns:
        list: Pets sorted by length, then alphabetically
    """
    pass


if __name__ == "__main__":
    # Test your functions here!
    print("Pets by length:", sort_pets_by_length()[:5])
    print("\nDoubled numbers:", map_double_numbers()[:5])
    print("Even numbers:", filter_even_numbers()[:5])
    print("\nLongest pet:", find_longest_pet_name())
    print("Shortest pet:", find_shortest_pet_name())
    print("\nMax number:", find_max_number())
    print("Min number:", find_min_number())
    print("Sum:", sum_all_numbers())
    print("Average:", average_number())
    print("\nFirst 5 pet-number pairs:", list(zip_pets_with_numbers())[:5])
