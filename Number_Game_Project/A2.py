from tkinter import *
import random
import math
""""-------------------------------------------------------------
The Guess the Number Game GUI
File: A2.py
Author: Merle Crutchfield
Purpose: This is a GUI game that asks the user to guess a number
between 1 and 20. It will they reply with three possible
outcomes: the guess is too high, too low, or they got it
right. Once they guess it, it will ask the user if they
wish to play again and if yes it will generate a new
number and new GUI window.
--------------------------------------------------------------"""

def MainGameMethod():
    '''
    This function tells the user after pushing the button if
    their guess was too high, too low, or if they got it
    just right and askes them if they want to play again
    '''
    if int(guess.get()) > target:
        ans.set("Your guess is too high")
        b1 = Button(root, text="Guess", command=MainGameMethod)
        b1.grid(row=2, column=1)
    elif int(guess.get()) < target:
        ans.set("Your guess is too low")
        b1 = Button(root, text="Guess", command=MainGameMethod)
        b1.grid(row=2, column=1)
    else:
        ans.set("Congrats, you guessed it right!\nWould you like to play again (q to quit)?")
        b1 = Button(root, text="Play again", command=PlayAgain)
        b1.grid(row=2, column=1)


def PlayAgain():
    '''
    This function checks to see if the user wants
    to play the game again or if they want to end
    it.
    '''
    b1.master.destroy()
    if guess.get() != 'q':
        GUI()



def GUI():
    '''
    This function is used for creating the graphics
    window and button with text. It also generates
    a new random number each time the game it is
    called.
    '''
    # Globally needed variables
    global guess
    global ans
    global root
    global b1
    global target

    target = random.randint(1, 20)

    root = Tk()
    root.title("GUI Guessing Game")

    lab3 = Label(root, text="Enter guess between 1-20:")
    lab3.grid(row=0, column=0)

    guess = StringVar()
    guess_entry = Entry(root, width=7, textvariable=guess)
    guess_entry.grid(row=0, column=1)

    lab2 = Label(root)
    lab2.grid(row=0, column=2)

    ans = StringVar()
    lab1 = Label(root, textvariable=ans)
    lab1.grid(row=1, column=1)

    ans_label = Label(root)
    ans_label.grid(row=1, column=2)

    b1 = Button(root, text="Guess", command=MainGameMethod)
    b1.grid(row=2, column=1)

    for child in root.winfo_children():
        child.grid_configure(padx=5, pady=5)

    guess_entry.focus()

    # Start main event loop
    root.mainloop()

# Starts the code
GUI()
