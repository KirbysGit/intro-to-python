# Colin Kirby
# autopolygonator.py
# written to create a polygon in turtle based off user inputted values
# written for COP2500C

import turtle

# request input from users of integers for number of sides
# polygon and total length of polygon
i = int(input("Number of sides of polygon: "))
j = int(input("Total length of polygon: "))
n=i
# using a variable for length per side of polygon
# as the total length / number of sides gives the length per side
k = j / i

# displays turtle
my_screen = turtle.getscreen()
my_turtle = turtle. Turtle()

# creates a loop in which I reassigned the number of sides from i to n as well
# because if not it would create the shape infinitely, specifically depending
# on "n" move the turtle forward "k" and left 360 / i for equal angles,
# and n = n - 1 to act as a sort of break for the loop.
while n >= 0:
    my_turtle.forward(k)
    my_turtle.left(360/i)
    n = n - 1
    



