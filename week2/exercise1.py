"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this have the collections of the word ('what', 'does', 'this', 'line', 'do', '?')
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #This shows the collections have the words ('what', 'does', 'this', 'line', 'do', '?')

# I think it is looking for 'word' in this collection.
for word in some_words: # it creates a loop called word with the list of 'some_words'
    # I think this print the 'word' loop which is the list/collection in the collection.
    print(word) # This line prints the 'word' loop which is the list/collection in the collection.

# I think it creates a loop called x with the list called 'some_words'
for x in some_words: # it creates a loop called word.
    # I think this print the 'x' loop which is the list/collection in the collection.
    print(x) # This line prints the 'x' loop which is the list/collection in the collection.

# I think this print the collection called 'some_words'.
print(some_words) # It prints the collection itself.

# I think it checkes whether the collection 'some_words' contains more than 3 conponents.
if len(some_words) > 3: # It checkes whether the collection 'some_words' contains more than 3 conponents.
    # I think it prints 'some_words contains more than 3 words'.
    print('some_words contains more than 3 words') # It prints 'some_words contains more than 3 words'.

# I think it defines the function of 'usefulFunction()'
def usefulFunction(): # It defines the function of 'usefulFunction()'
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think it prints out the content of 'platform.uname()' which is: system, node, release, version, machine, and processor.
    print(platform.uname()) # It prints out the content of 'platform.uname()' which is: system, node, release, version, machine, and processor to the function 'usefulFunction() defined above.

# This line prints the function called 'usefulFunction()'
usefulFunction() # It prints the function called 'usefulFunction()'.

