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

# Sample data for exercises
pets = [
    "dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
    "guinea pig", "donkey", "duck", "water buffalo",
    "western honey bee", "dromedary camel", "horse", "silkmoth",
    "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
    "guineafowl", "ferret", "muscovy duck", "barbary dove",
    "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
    "canary", "society finch", "fancy mouse", "siamese fighting fish",
    "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"
]

numbers = [randint(1, 100) for _ in range(20)]


# =============================================================================
# PART 1: LAMBDA FUNCTIONS
# =============================================================================

def double_with_lambda():
    """Use a lambda function to double a number.
    
    Lambda syntax: lambda parameter: expression
    Example: lambda x: x * 2
    
    Create a lambda that takes a number and returns it doubled.
    
    Returns:
        function: A lambda function that doubles its input
    """
    pass


def add_ten_with_lambda():
    """Use a lambda function to add 10 to a number.
    
    Returns:
        function: A lambda function
    """
    pass


def is_even_lambda():
    """Use a lambda function to check if a number is even.
    
    Hint: Use the modulo operator %
    lambda x: x % 2 == 0
    
    Returns:
        function: A lambda that returns True if even, False if odd
    """
    pass


def get_string_length():
    """Use a lambda to get the length of a string.
    
    Returns:
        function: A lambda using len()
    """
    pass


# =============================================================================
# PART 2: MAP FUNCTION
# =============================================================================

def map_double_numbers():
    """Use map with a lambda to double all numbers in the numbers list.
    
    map() applies a function to each item in a sequence.
    
    Syntax: list(map(function, sequence))
    
    Note: map() returns a map object, convert it to a list!
    
    Returns:
        list: All numbers doubled
    """
    pass


def map_pet_lengths():
    """Use map to get the length of each pet name.
    
    You can use map with the built-in len function!
    
    Syntax: list(map(len, pets))
    
    Returns:
        list: Length of each pet name
    """
    pass


def map_first_letter():
    """Use map with a lambda to get the first letter of each pet name.
    
    Hint: lambda p: p[0]
    
    Returns:
        list: First letter of each pet name
    """
    pass


def map_uppercase():
    """Use map to convert all pet names to uppercase.
    
    Hint: You can use lambda p: p.upper() or just use str.upper directly!
    
    Returns:
        list: All pet names in uppercase
    """
    pass


# =============================================================================
# PART 3: FILTER FUNCTION
# =============================================================================

def filter_long_names():
    """Use filter to get only pets with names longer than 10 characters.
    
    filter() keeps only items where the function returns True.
    
    Syntax: list(filter(function, sequence))
    
    Returns:
        list: Pets with long names
    """
    pass


def filter_even_numbers():
    """Use filter to get only even numbers from the numbers list.
    
    Hint: Use your is_even_lambda from earlier!
    
    Returns:
        list: Only even numbers
    """
    pass


def filter_pets_with_space():
    """Use filter to get pets whose names contain a space.
    
    Hint: lambda p: ' ' in p
    
    Returns:
        list: Pets with spaces in their names
    """
    pass


# =============================================================================
# PART 4: BUILT-IN FUNCTIONS
# =============================================================================

def find_longest_pet_name():
    """Find the longest pet name using max().
    
    max() can take a key parameter!
    
    Syntax: max(sequence, key=function)
    Example: max(pets, key=len)
    
    Returns:
        str: The longest pet name
    """
    pass


def find_shortest_pet_name():
    """Find the shortest pet name using min().
    
    Returns:
        str: The shortest pet name
    """
    pass


def find_max_number():
    """Find the maximum number in the numbers list.
    
    Simple: max(numbers)
    
    Returns:
        int: The largest number
    """
    pass


def find_min_number():
    """Find the minimum number in the numbers list.
    
    Returns:
        int: The smallest number
    """
    pass


def sum_all_numbers():
    """Calculate the sum of all numbers.
    
    Use the built-in sum() function!
    
    Returns:
        int: Sum of all numbers
    """
    pass


def average_number():
    """Calculate the average of all numbers.
    
    Average = sum / count
    
    Returns:
        float: Average of numbers
    """
    pass


# =============================================================================
# PART 5: ZIP FUNCTION
# =============================================================================

def zip_pets_with_numbers():
    """Use zip to pair each pet with a number.
    
    zip() combines multiple sequences into tuples.
    
    Syntax: list(zip(sequence1, sequence2))
    
    Returns:
        list: List of (pet, number) tuples
    """
    pass


def create_pet_dictionary():
    """Create a dictionary mapping pets to numbers using zip.
    
    You can convert zipped tuples directly to a dict!
    
    Syntax: dict(zip(keys, values))
    
    Returns:
        dict: Dictionary of pet -> number
    """
    pass


# =============================================================================
# PART 6: ENUMERATE FUNCTION
# =============================================================================

def enumerate_pets():
    """Use enumerate to get (index, pet) pairs.
    
    enumerate() gives you index and value together!
    
    Syntax: list(enumerate(sequence))
    
    Returns:
        list: List of (index, pet) tuples
    """
    pass


def enumerate_from_one():
    """Use enumerate starting from 1 instead of 0.
    
    enumerate() takes an optional start parameter!
    
    Syntax: list(enumerate(sequence, start=1))
    
    Returns:
        list: List of (index, pet) tuples starting from 1
    """
    pass


def find_pet_positions():
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

def combine_map_filter():
    """First filter for long names, then map to uppercase.
    
    You can chain operations!
    
    Returns:
        list: Long pet names in uppercase
    """
    pass


def sort_by_last_letter():
    """Sort pets by their last letter.
    
    Use sorted() with a key parameter.
    
    Hint: sorted(pets, key=lambda p: p[-1])
    
    Returns:
        list: Pets sorted by last letter
    """
    pass


if __name__ == "__main__":
    # Test your functions here!
    print("Double lambda:", double_with_lambda()(5))
    print("\nLongest pet:", find_longest_pet_name())
    print("Shortest pet:", find_shortest_pet_name())
    print("\nMax number:", find_max_number())
    print("Min number:", find_min_number())
    print("Sum:", sum_all_numbers())
    print("Average:", average_number())
    print("\nFirst 5 pet-number pairs:", list(zip_pets_with_numbers())[:5])
