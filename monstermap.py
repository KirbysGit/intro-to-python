# Colin Kirby
# monstermap.py
# written to display a 10 x 8 grid of circle with varying sizes
# depending on the user inputted multiplies and the current cell.
# written for COP2500C

#imports turtle library
import turtle

# prompts the user for three inputs including the horizontal and
# vertical multiplier and constant value.
x = float(input("Enter the Horizontal Multiplier value: "))
y = float(input("Enter the Vertical Multiplier value: "))
z = float(input("Enter the Constant value: "))

# displays the turtle on screen
my_screen = turtle.getscreen()
my_turtle = turtle. Turtle()

# creates a nested for loop in which per cell a circle is created
# with a radius determined by both cell values and user inputted
# values which then continues until it reaches the vert cell 9
# and horiz cell 11 to create a 10 by 8 grid (b/c it starts at 1).
for horiz_cell in range (1,11):
    for vert_cell in range(1,9):
        my_turtle.penup()
        my_turtle.goto(25 * horiz_cell, -25 * vert_cell)
        my_turtle.pendown()
        my_turtle.fillcolor("green")
        my_turtle.begin_fill()
        radius = ((x * horiz_cell + y * vert_cell) + z)
        my_turtle.circle(radius)
        my_turtle.end_fill()
        






