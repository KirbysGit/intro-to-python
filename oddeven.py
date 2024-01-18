# Colin Kirby
# oddeven.py
# program takes user input and returns an output depending on inputted variable
# written for COP2500C

# imports random library allowing for functions such as random.randint which
# generates a random integer between set values

import random

# sets the random integer generated for the game to p

p = random.randint(1,256)

# prompts user for input of "odd" or "even"

choice = (input("I'm thinking of a number. Is it odd or even? "))

# provides conditions for input such as:
# if something other than odd or even is inputted it provides an error message
# if both p and choice are even or odd then it provides a nice message
# if p and choice are different then it provides a sorry message

if (choice != "odd" and choice != "even"):
    print ("You did not enter odd or even. Try again. The number was ",p," if you were wondering.")
elif( choice == "even" and p % 2 == 0):
    print("My number was", p, ". Nice job!")
elif( choice == "even" and p % 2 != 0):
    print("My number was", p, ". Sorry!")
elif( choice == "odd" and p % 2 != 0):
    print("My number was", p, ". Nice job!")
elif( choice == "odd" and p % 2 == 0):
    print("My number was", p, ". Sorry!")






