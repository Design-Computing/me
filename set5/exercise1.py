# -*- coding: UTF-8 -*-

import requests

"""RECURSION

Recall that recursion is the practice of calling a function from inside itself.
It can be used to break down problems into smaller and smaller pieces.

A recursive function always has two parts:
1. A BASE CASE - when to stop recursing
2. A RECURSIVE CASE - when to call yourself again

Example:
    def countdown(n):
        if n <= 0:           # BASE CASE
            print("Blastoff!")
        else:                # RECURSIVE CASE
            print(n)
            countdown(n-1)   # Call yourself with a smaller problem
"""


def get_a_word_of_length_n(length):
    """Get a word of specific length from the word API.
    
    Args:
        length: The desired word length (must be >= 4)
        
    Returns:
        A word of the specified length, or None if invalid input
    """
    pass


def list_of_words_with_lengths(list_of_lengths):
    """Get a list of words with specified lengths using recursion.
    
    This is the recursive version! Use recursion to build the list.
    
    Args:
        list_of_lengths: A list of desired word lengths [4, 5, 6, ...]
        
    Returns:
        A list of words matching those lengths
        
    Hint: Think about:
    - BASE CASE: What if the list is empty?
    - RECURSIVE CASE: Get the first word, then recursively get the rest!
    """
    pass


if __name__ == "__main__":
    print("Testing get_a_word_of_length_n:")
    word = get_a_word_of_length_n(10)
    print(f"A 10-letter word: {word}")
    
    print("\nTesting list_of_words_with_lengths:")
    words = list_of_words_with_lengths([4, 5, 6, 7])
    print(f"Words: {words}")
