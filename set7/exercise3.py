# -*- coding: UTF-8 -*-

"""ADVANCED PYTHON: GENERATORS, DICT COMPREHENSIONS, AND COLLECTIONS

This exercise covers more advanced Python features:
- Generators: memory-efficient iteration with yield
- Dictionary comprehensions: creating dicts elegantly
- Collections module: Counter, defaultdict, and more

These features are powerful tools for writing efficient, elegant Python code!
"""

from typing import Dict, List, Tuple, Generator
from collections import Counter, defaultdict
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

numbers = [randint(0, 100) for _ in range(1000)]


# =============================================================================
# PART 1: DICTIONARY COMPREHENSIONS
# =============================================================================

def create_pet_length_dict() -> Dict[str, int]:
    """Create a dictionary mapping pet names to their lengths.
    
    Dict comprehension syntax: {key: value for item in sequence}
    
    Example: {pet: len(pet) for pet in pets}
    
    Returns:
        dict: {pet_name: length}
    """
    pass


def create_number_square_dict() -> Dict[int, int]:
    """Create a dictionary mapping numbers 0-9 to their squares.
    
    Hint: {n: n**2 for n in range(10)}
    
    Returns:
        dict: {0: 0, 1: 1, 2: 4, 3: 9, ...}
    """
    pass


def create_first_letter_dict() -> Dict[str, str]:
    """Create a dictionary mapping first letters to pet names.
    
    Map each unique first letter to the first pet starting with that letter.
    
    Example: {'d': 'dog', 'g': 'goat', 'p': 'pig', ...}
    
    Hint: You can iterate over pets and use p[0] as the key
    
    Returns:
        dict: {first_letter: pet_name}
    """
    pass


def filter_dict_comprehension() -> Dict[str, int]:
    """Create a dictionary of only pets with names longer than 8 characters.
    
    You can add a condition to dict comprehensions!
    
    Syntax: {k: v for k, v in items if condition}
    
    Returns:
        dict: {long_pet_name: length}
    """
    pass


# =============================================================================
# PART 2: GENERATORS
# =============================================================================

def count_up_generator(start: int, end: int) -> Generator[int, None, None]:
    """Create a generator that counts from start to end.
    
    Use 'yield' instead of 'return' to make a generator!
    
    Example:
        def my_generator():
            yield 1
            yield 2
            yield 3
    
    Args:
        start: Starting number
        end: Ending number (inclusive)
        
    Yields:
        int: Next number in sequence
    """
    pass


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """Generate the first n Fibonacci numbers.
    
    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Each number is the sum of the previous two.
    
    This is a great use of generators - you generate numbers on-the-fly
    without storing the whole sequence in memory!
    
    Args:
        n: How many Fibonacci numbers to generate
        
    Yields:
        int: Next Fibonacci number
        
    Hint:
        Start with a = 0, b = 1
        yield a
        Then in a loop: yield b, then a, b = b, a+b
    """
    pass


def even_numbers_generator(max_num: int) -> Generator[int, None, None]:
    """Generate all even numbers from 0 up to max_num.
    
    Args:
        max_num: Maximum number
        
    Yields:
        int: Next even number
    """
    pass


def infinite_counter() -> Generator[int, None, None]:
    """Create an infinite counter generator.
    
    This generator never stops! It counts 0, 1, 2, 3, ...forever.
    
    Warning: Don't try to convert this to a list - it's infinite!
    Use it with next() or in a for loop with a break condition.
    
    Yields:
        int: Next number
        
    Example usage:
        counter = infinite_counter()
        next(counter)  # 0
        next(counter)  # 1
        next(counter)  # 2
    """
    pass


# =============================================================================
# PART 3: COLLECTIONS.COUNTER
# =============================================================================

def count_first_letters() -> Counter:
    """Count how many pets start with each letter.
    
    Use Counter to count first letters of all pet names!
    
    Hint: Counter([p[0] for p in pets])
    
    Returns:
        Counter: {letter: count}
    """
    pass


def count_number_frequency() -> Counter:
    """Count how many times each number appears in the numbers list.
    
    Counter is perfect for frequency analysis!
    
    Returns:
        Counter: {number: frequency}
    """
    pass


def most_common_number() -> Tuple[int, int]:
    """Find the most common number in the numbers list.
    
    Counter has a .most_common() method!
    
    Hint: Counter(numbers).most_common(1)[0]
    This returns a list of (value, count) tuples.
    
    Returns:
        tuple: (most_common_number, count)
    """
    pass


def top_three_letters() -> List[Tuple[str, int]]:
    """Find the three most common first letters in pet names.
    
    Use Counter and .most_common(3)
    
    Returns:
        list: [(letter, count), (letter, count), (letter, count)]
    """
    pass


# =============================================================================
# PART 4: COLLECTIONS.DEFAULTDICT
# =============================================================================

def group_pets_by_first_letter() -> Dict[str, List[str]]:
    """Group all pets by their first letter using defaultdict.
    
    defaultdict automatically creates entries for new keys!
    
    Example:
        from collections import defaultdict
        groups = defaultdict(list)
        for pet in pets:
            groups[pet[0]].append(pet)
    
    Returns:
        dict: {letter: [pets starting with that letter]}
    """
    pass


def group_pets_by_length() -> Dict[int, List[str]]:
    """Group pets by their name length using defaultdict.
    
    Returns:
        dict: {length: [pets with that length]}
    """
    pass


def count_with_defaultdict() -> Dict[str, int]:
    """Count first letters using defaultdict(int).
    
    defaultdict(int) starts at 0, so you can just += 1
    
    Example:
        counts = defaultdict(int)
        for pet in pets:
            counts[pet[0]] += 1
    
    Returns:
        dict: {letter: count}
    """
    pass


# =============================================================================
# BONUS CHALLENGES
# =============================================================================

def lazy_evaluation_demo() -> Generator[int, None, None]:
    """Demonstrate why generators are memory efficient.
    
    Create a generator that yields squares of numbers from 0 to 1,000,000.
    
    Don't convert to a list! Just return the generator.
    This uses almost no memory, whereas a list would use a lot!
    
    Returns:
        generator: Generator of squared numbers
    """
    pass


def chain_generators() -> List[int]:
    """Use multiple generators together.
    
    Create a generator that:
    1. Generates numbers from 1 to 100
    2. Only yields even numbers
    3. Yields the square of each even number
    
    Returns:
        list: Squares of even numbers from 1-100
        (It's okay to convert to list here for the return)
    """
    pass


def word_length_histogram() -> Counter:
    """Create a histogram of pet name lengths.
    
    Use Counter to count how many pets have each name length.
    
    Returns:
        Counter: {length: count}
        
    Example result: {3: 5, 4: 8, 5: 10, ...}
    meaning 5 pets have 3-letter names, 8 have 4-letter names, etc.
    """
    pass


def pets_by_length_nested() -> Dict[int, Dict[str, List[str]]]:
    """Create nested defaultdict to group pets by length and first letter.
    
    Structure: {length: {first_letter: [pets]}}
    
    Example: {3: {'d': ['dog'], 'c': ['cat']}, ...}
    
    Hint: defaultdict(lambda: defaultdict(list))
    
    Returns:
        dict: Nested dictionary of pets
    """
    pass


if __name__ == "__main__":
    # Test your functions here!
    print("Pet length dict (first 5):")
    pet_dict = create_pet_length_dict()
    for i, (pet, length) in enumerate(pet_dict.items()):
        if i >= 5:
            break
        print(f"  {pet}: {length}")
    
    print("\nFirst 10 Fibonacci numbers:")
    fib = fibonacci_generator(10)
    print(list(fib))
    
    print("\nFirst letter counts:")
    print(count_first_letters())
    
    print("\nMost common number:")
    print(most_common_number())
    
    print("\nPets grouped by first letter (showing 'g'):")
    groups = group_pets_by_first_letter()
    print(f"  g: {groups.get('g', [])}")
