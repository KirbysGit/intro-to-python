# Colin Kirby
# vehicle.py
# program written to display a truck through numerous coded pen movements
# and rotations
# written for COP2500C

import turtle

my_screen = turtle.getscreen()
my_turtle = turtle. Turtle()

#sets the background color, pencolor and pensize for turtle

my_screen.bgcolor("white")
my_turtle.pencolor("black")
my_turtle.pensize(5)

#starts with basic movements backwards and forwards to create the back of
#the truck

my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.backward(130)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(25)
my_turtle.right(90)

#creates a circle for the back wheel

my_turtle.circle(20)
my_turtle.penup()
my_turtle.goto(-63, -50)
my_turtle.left(90)
my_turtle.pendown()
my_turtle.forward(90)
my_turtle.right(90)

#creates a second circle for front wheel

my_turtle.circle(20)
my_turtle.penup()
my_turtle.goto(67,-50)
my_turtle.left(90)
my_turtle.pendown()

#creates the front of truck 
my_turtle.forward(25)
my_turtle.left(90)
my_turtle.forward(55)
my_turtle.left(85)
my_turtle.forward(35)
my_turtle.right(80)
my_turtle.forward(35)
my_turtle.left(85)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(43)
my_turtle.right(180)
my_turtle.forward(43)
my_turtle.penup()
my_turtle.right(90)
my_turtle.forward(25)
my_turtle.end_fill()
my_turtle.pendown()

#creates the window of the truck

my_turtle.fillcolor("cyan")
my_turtle.begin_fill()
my_turtle.right(90)
my_turtle.forward(35)
my_turtle.left(90)
my_turtle.forward(32)
my_turtle.left(95)
my_turtle.forward(32)
my_turtle.end_fill()
my_turtle.penup()
my_turtle.goto(-65,-50)
my_turtle.pendown()

#moves the turtle back to the back wheel where it then fills it with
#the color black

my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()
my_turtle.penup()
my_turtle.goto(66,-50)
my_turtle.pendown()

#moves the turtle to the front wheel to fill it with color black
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(20)
my_turtle.end_fill()
my_turtle.penup()
my_turtle.goto(3,0)

#my attempt at filling in the triangle of white that was leftover

my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.right(38)
my_turtle.forward(49)
my_turtle.left(129)
my_turtle.forward(24)
my_turtle.end_fill()
