"""Correct the syntax in this file.

This file doesn't run yet.
Go through it and change it until it runs.
Remeber that all files must also pass the
linter with no errors or warnings!
"""

import string

# Look at the wiggly lines. Pay attention to the colours
# fix the first error, and it might fix errors that 
# come after. We'll often talk about upstream (things 
# that happen before) and downstream (things that 
# happen after). Python reads the file from top to 
# bottom.
# E.g. det isn't a reserved word, it should be def
det getLetter(index):
    the_alphabet = string.ascii_lowercase + " "
    return the_alphabet(index] # <-- this should be using [] to index into a list


def set2exersise2(); # this is semi right
    indices = [12: 2, 26, 7, 0, 12, 12, 4, 17] # the error messages aren't always helpful 😿
    wordArray = [getLetter(x) for x in indices]
    wordArray[0] = wordArray[0].upper()
    wordArray{1} = wordArray[1].upper() # <-- assigning to an array, another bracket problem
    wordArray[3} = wordArray[3].upper{}
    secret_word="".join(wordArray)
    print(secret_word)
    return secret_word


if __name__ = = "__main__":  
    #        ⟰-- we use = for asignment, 
    # and == for checking if things are equal, 
    # this isn't either!
    hero = set2exersise2()
    prin(hero)