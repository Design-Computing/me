# -*- coding: UTF-8 -*-

"""LIST OPERATIONS AND COMPREHENSIONS

This exercise covers essential list operations in Python:
- Slicing: accessing parts of lists
- Append vs Extend: adding items to lists
- List comprehensions: elegant way to create lists

These are fundamental Python skills you'll use constantly!
"""


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


# =============================================================================
# PART 1: SLICING
# =============================================================================

def first_ten_pets():
    """Return the first 10 pets from the pets list.
    
    Hint: Use slicing with [:10]
    
    Returns:
        list: First 10 pets
    """
    pass


def last_five_pets():
    """Return the last 5 pets from the pets list.
    
    Hint: You can use negative indices! [-5:]
    
    Returns:
        list: Last 5 pets
    """
    pass


def pets_from_4_to_10():
    """Return pets from index 4 to 10 (exclusive).
    
    Remember: [start:end] doesn't include the end index
    
    Returns:
        list: Pets from index 4 to 9
    """
    pass


def middle_pets():
    """Return the middle 20 pets.
    
    Hint: The list has 40 items. Middle 20 means skip first 10, take next 20.
    You can use [10:30]
    
    Returns:
        list: Middle 20 pets
    """
    pass


def reverse_pets():
    """Return the pets list in reverse order.
    
    Hint: Use [::-1] to reverse a list!
    The -1 means "step backwards"
    
    Returns:
        list: All pets in reverse order
    """
    pass


def every_third_pet():
    """Return every third pet from the list.
    
    Hint: [::3] means "start at beginning, step by 3"
    
    Returns:
        list: Every 3rd pet
    """
    pass


# =============================================================================
# PART 2: APPEND VS EXTEND
# =============================================================================

def append_example():
    """Demonstrate append by adding a single item to a list.
    
    Create a new list, then use .append() to add the string "hamster" to it.
    Then append another string "rabbit".
    
    Returns:
        list: A list with two items
    """
    pass


def extend_example():
    """Demonstrate extend by adding multiple items to a list.
    
    Create a new list, then use .extend() to add ["hamster", "rabbit"] to it.
    Then extend with ["guinea pig", "mouse"].
    
    Returns:
        list: A list with four items
    """
    pass


def append_vs_extend_comparison():
    """Show the difference between append and extend.
    
    Create two lists: list1 and list2, both starting as empty.
    
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
    pass


# =============================================================================
# PART 3: LIST COMPREHENSIONS
# =============================================================================

def pet_name_lengths():
    """Return a list of the lengths of each pet name.
    
    Use a list comprehension!
    
    Example: ["dog", "cat"] -> [3, 3]
    
    Hint: [len(p) for p in pets]
    
    Returns:
        list: Length of each pet name
    """
    pass


def long_pet_names():
    """Return only pets whose names are longer than 10 characters.
    
    Use a list comprehension with a condition!
    
    Syntax: [item for item in list if condition]
    
    Returns:
        list: Pets with names longer than 10 chars
    """
    pass


def pet_names_uppercase():
    """Return all pet names in uppercase.
    
    Use a list comprehension with .upper()
    
    Returns:
        list: All pet names in UPPERCASE
    """
    pass


def pets_starting_with_g():
    """Return all pets whose names start with 'g'.
    
    Use a list comprehension with a condition.
    
    Hint: string.startswith('g')
    
    Returns:
        list: Pets starting with 'g'
    """
    pass


def pet_name_and_length():
    """Return a list of tuples with (name, length) for each pet.
    
    Use a list comprehension to create tuples.
    
    Example: [("dog", 3), ("cat", 3), ...]
    
    Hint: [(p, len(p)) for p in pets]
    
    Returns:
        list: List of (name, length) tuples
    """
    pass


# =============================================================================
# BONUS CHALLENGE
# =============================================================================

def nested_list_comprehension():
    """Create a 2D list (matrix) using nested list comprehensions.
    
    Create a 5x5 grid where each cell contains its coordinates as a string.
    
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
    # Test your functions here!
    print("First 10 pets:", first_ten_pets())
    print("\nLast 5 pets:", last_five_pets())
    print("\nPet name lengths:", pet_name_lengths()[:10])  # First 10
    print("\nLong pet names:", long_pet_names())
    print("\nPets starting with 'g':", pets_starting_with_g())
