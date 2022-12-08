import random
import math

""""-------------------------------------------------------------
The Guess the Number Game
File: A1.py
Author: Merle Crutchfield
Purpose: This is a CLI game that asks the user to guess a number
between 1 and 20. It will they reply with three possible
outcomes: the guess is too high, too low, or they got it
right. Once they guess it, it will ask the user if they
wish to play again and if yes it will generate a new
number.
--------------------------------------------------------------"""

# ---------------------------------------------------------------
# GetInput
# ---------------------------------------------------------------
def GetInput(s):
    '''
    This function prints out the string passed and takes in the
    users int input, which it returns.
    '''
    num = input(s)
    return num

#---------------------------------------------------------------
# PlaySomethingGame
#---------------------------------------------------------------
def PlaySomethingGame():
    '''
    This function generates a random number 1-20 inclusively.
    It then get the guess first guess of the user. If it is
    wrong, it travels through a while loop that will tell the
    user if the guess is too high or low, then gets the next
    input and runs again. Once the user gets it right, it prints
    out a congrats statement.
    '''
    target = random.randint(1, 20)
    guess = int(GetInput("Guess a number between 1-20: "))

    while guess != target:
        if guess > target:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        guess = int(GetInput("Guess another number between 1-20: "))
    print("Congrats, you guessed it right!")

#================================================================
# Initial input line
c = input("Welcome! Press q to quit or any key to continue: ")
# Runs the game until the user requests to end
while c != 'q':
    PlaySomethingGame()
    c = input("Press q to quit or any key to continue: ")
