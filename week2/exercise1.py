"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']

#if there is the word in the array in some_words, print out the 'word'
for word in some_words:
    print(word)
#prints out the set of words in the function

#if the letter x is in some_words, print out 'x'
for x in some_words:
    print(x)
#prints out the set of words in the function
print(some_words)

#if there are more than 3 elements in the array print out the string
if len(some_words) > 3:
    print('some_words contains more than 3 words')
#prints out the string

#prints out the computers system, processor, etc hardware
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
