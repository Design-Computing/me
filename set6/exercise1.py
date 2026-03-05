# -*- coding: UTF-8 -*-

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsulate one idea, especially if that idea is 
used in several places.

We've talked already about the cycle:
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where:
- RED means make sure the test fails if you haven't done anything
- GREEN means make the test pass, however you can
- REFACTOR means improve the code while keeping tests passing

The function below works fine, but it's long and hard to read. Your task is to
refactor it to use the helper functions you created in set 5.

You should import from set5.exercise1:
    - list_of_words_with_lengths

Then use it to simplify this function!

MODIFY this function, don't write a whole new one.
"""

import requests

# TODO: Import your helper function from set 5
# from set5.exercise1 import list_of_words_with_lengths


def wordy_pyramid():
    """Create a pyramid of words from the word API.
    
    This is the OLD way - lots of repeated code!
    Your task: refactor it to use list_of_words_with_lengths from set 5.
    """
    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/"
        "give_me_a_word?wordlength={length}"
    )
    pyramid_list = []
    
    # Going up the pyramid
    for i in range(3, 21, 2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    
    # Going down the pyramid
    for i in range(20, 3, -2):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)

    return pyramid_list


if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
