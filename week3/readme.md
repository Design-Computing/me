TODO: Reflect on what you learned this week and what is still unclear.
isdigit doesnt work for lists
    print("\nWelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = input("Enter an upper bound: ")
    lowerBound = input("Enter a lower bound")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        try:
          guessedNumber = int(input("Guess a number: "))
          print("You guessed {},".format(guessedNumber),)
          if guessedNumber == actualNumber:
              print("You got it!! It was {}".format(actualNumber))
              guessed = True
          elif guessedNumber < actualNumber:
              print("Too small, try again :'(")
          else:
              print("Too big, try again :'(")
        except:
          print("That aint an integer chief")