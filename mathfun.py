# Colin Kirby
# mathfun.py
# program written to find the length of specific sides
# of a triangle based off of user inputted values of
# other values within the triangle.
# written for COP2500C

import math

# adj_length: given the length of hypotenuse
# and the value of the adjacent angle in
# degrees it will return the adjacent length.
# Will cause an error if both values aren't numbers.
def adj_length(hypo_len, theta_adj):
    theta_radians = math.radians(theta_adj)
    y = math.cos(theta_radians) * hypo_len
    return y

# opp_length: given the length of the hypotenuse
# and the value of the adjacent angle in
# degrees it will return the opposite length.
# Will cause an error if both values aren't numbers.
def opp_length(hypo_len, theta_adj):
    theta_radians = math.radians(theta_adj)
    y = math.sin(theta_radians) * hypo_len
    return y

# theta_adj1: given the length of the hypotenuse
# and the opposite side it will return the value of
# the adjacent angle in degrees. Will cause an error
# if both values aren't numbers.
def theta_adj1(hypo_len, opp_len):
    theta_radians = math.asin(opp_len / hypo_len)
    theta_degrees = math.degrees(theta_radians)
    return theta_degrees

# theta_adj2: given the length of the adjacent and
# opposite sides it will return the valeu of the
# adjacent angle in degrees. Will cause an error if
# both values aren't numbers.
def theta_adj2(adj_len, opp_len):
    theta_radians = math.atan(opp_len / adj_len)
    theta_degrees = math.degrees(theta_radians)
    return theta_degrees


# Prompts the user for 4 inputs (as floats) including the
# opposite, adjacent, hypotenuse lengths and the adjacent angles.
opp_len = float(input("Enter the length of the opposite side: "))
adj_len = float(input("Enter the length of the adjacent side: "))
hypo_len = float(input("Enter the length of the hypotenuse: "))
theta_adj = float(input("Enter the adjacent angle of the triangle: "))

# Prints the adjacent length using the function
# adj_length based off the values entered by user
# of length of hypotenuse and angle of adjacent.
print("The length of the adjacent side is roughly ",adj_length(hypo_len,theta_adj))

# Prints the oppostie length using the function
# opp_length based off the vlaues entered by user
# of length of hypotenuse and angle of adjacent.
print("The length of the opposite side is roughly",opp_length(hypo_len,theta_adj))

# Prints the angle of the adjacent using function
# theta_adj1 based off values of hypo_len and opp_len
# entered by the user.
print("The value of the adjacent angle is roughly", theta_adj1(hypo_len,opp_len))

# Prints the angle of the adjacent using function
# theta_adj2 based off values of adj_len and opp_len
# entered by the user.
print("The value of the adjacent angle is roughly", theta_adj2(adj_len,opp_len))


#Notes from Lab:
# Converting the angle from degrees to randians to use trig. functions
#theta_radians = math.radians(theta)
#cos(theta) = base/hypo
#base = math.cos(theta_radians)*hypo
#sin(theta) = perpindicular/hypo
#perpindicular = math.sin(theta_radians)*hypo

#PerfectRightTriangleValues
# hyp = 5
# opp = 3
# adj = 4
# hyp_ang = 90
# adj_ang = 36.87
# opp_ang = 51.13
