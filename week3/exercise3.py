"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


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
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    
    bs = False
    while bs == False:
        preanswer1 = False
        while preanswer1 != True:
            lowerBound = input("Enter an lower bound: ")
            try:
                int(lowerBound)
                preanswer1 = True
            except ValueError:
                print("Only whole number is accepted!")
                preanswer1 = False
        preanswer2 = False
        while preanswer2 != True:
            upperBound = input("Enter an upper bound: ")
            if upperBound > lowerBound:
                try:
                    int(upperBound)
                    bs = True
                    preanswer2 = True
                except ValueError:
                    print("Only whole number is accepted!")
                    upperBound = input("Enter an upper bound: ")
                    preanswer2 = False
            else:
                print("The upperbound can not be smaller or equal to the lowerbound!")
                preanswer2 = False
        print("OK then, a number between " + str(lowerBound) + " and " + str(upperBound) + ".")

    upperBound = int(upperBound)
    lowerBound = int(lowerBound)
    actualNumber = random.randint(lowerBound+1, upperBound)

    guessed = False
    while not guessed:
        answer = False
        while answer != True:
          guessedNumber = input("Guess a number: ")
          try:
              int(guessedNumber)
              answer = True
          except ValueError:
              answer = False
              print("Only whole number is accepted!")
        print("You guessed {},".format(guessedNumber),)
        if int(guessedNumber) == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif int(guessedNumber) < actualNumber and int(guessedNumber) > lowerBound:
            print("Too small, try again :'(")
        elif int(guessedNumber) > actualNumber and int(guessedNumber) < upperBound:
            print("Too big, try again :'(")
        elif int(guessedNumber) > upperBound:
            print("Your guess is not even within your range!\nIt is way to big, it should be lower than " + str(upperBound) + ". Try again :' ")
        elif int(guessedNumber) <= lowerBound:
            print("Your guess is not even within your range!\nIt is way to small, it should be bigger than " + str(lowerBound) + ". Try again :' ")
    return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!
if __name__ == "__main__":
    print(advancedGuessingGame())
