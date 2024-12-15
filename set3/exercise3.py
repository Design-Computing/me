"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def bounded_int_input(low, high, message="Enter a number which is between"):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    while True:
        try:
            user_number = int(input(f'{message} {low} and {high}: '))
            if low < user_number < high:
                print(f'{user_number} is between {low} and {high}')
                return user_number
            else: print(f'Number is not between {low} and {high}. Please enter another number.')
        except ValueError:
            print("Invalid input. Please enter an integer.")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)


    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    lowerBound = bounded_int_input(-50000, 50000, message="Enter a lower bound: ")
    upperBound = bounded_int_input(lowerBound+2, 50000, message="Enter an upper bound: ")
    
    if lowerBound >= upperBound:
        print("The lower bound must be less than the upper bound. Please try again.")
    elif upperBound - lowerBound == 1:
        print("The difference between the lower bound and upper bound must be at least 1. Please try again.")  
    else:
        print(f"OK then, your lower bound is {lowerBound} and your upper bound is {upperBound}") 

    actualNumber = random.randint(lowerBound + 1, upperBound - 1)
    while True:
        guessedNumber =  bounded_int_input(lowerBound, upperBound, message="Guess a number: ")
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
            return "You got it!"
            # the tests are looking for the exact string "You got it!". Don't modify that!
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
            lowerBound = guessedNumber
        else:
            print("Too big, try again :'(")
            upperBound = guessedNumber
        


if __name__ == "__main__":
    print(advancedGuessingGame())
