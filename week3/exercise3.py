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

    lowerBound = input("Enter an lower bound: ")
    try:
      lowerBound = int(lowerBound)
    except ValueError:
      IntegerTest0 = False
      while IntegerTest0 == False:
        try:
          lowerBound = int(lowerBound)
          IntegerTest0 = True
        except ValueError:
          lowerBound = input("Enter an lower bound: ")

    upperBound = input("Enter an upper bound: ")
    try:
      upperBound = int(upperBound)
    except ValueError:
      IntegerTest = False
      while IntegerTest == False:
        try:
          upperBound = int(upperBound)
          IntegerTest = True
        except ValueError:
          upperBound = input("Enter an upper bound: ")
    
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)
    print("OK then, a number between {a} and {b} ?".format(a = lowerBound, b = upperBound))

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = input("Guess a number: ")
        try:
          guessedNumber = int(guessedNumber)
        except ValueError:
          IntegerTest1 = False
          while IntegerTest1 == False:
            try:
              guessedNumber = int(guessedNumber)
              IntegerTest1 = True
            except ValueError:
              guessedNumber = input("Guess a number: ")

        if guessedNumber < lowerBound or guessedNumber > upperBound:
          print("Guess a number in the range, fool.")
        else:
          print("You guessed {},".format(guessedNumber),)
          if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
          elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
          else:
            print("Too big, try again :'(")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
