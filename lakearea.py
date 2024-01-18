# Name: Colin Kirby
# Program: lakearea.py

# program requires input from user of an integer which is then plugged into a
# preset equation in which it is solving for the area of the half circle lake
# which it then displays in meters squared

# program was written to solve for the area of Lake Knightrola depending on
# the user inputted radius

# this paragraph serves to act as the prompt for the user inputted radius as it
# requires the user to input an integer
r = int(input("Enter the radius of the lake in meters:"))

# acts as a constant for the irrational number pi in the equation pi, r^2
p = 3.1416

# serves as the destination for the user inputted integer as it takes that
# integer and plugs it into this equation, as it serves to act as the equation
# for the area of a circle = pi, r^2 then divided by two as it is a half-circle
a = ((p * (r ** 2)) / 2)

# then finally the output of the equation by using the user inputted integer is
# printed out with its proper unit, meters squared.
print ("The area of the lake is",a, "m^2")


