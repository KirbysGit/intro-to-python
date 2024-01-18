# a -> opp.
# b -> adj.
# c -> hypo.
# float means decimal values
# "math" is a library of python

import math

adj = float(input("Enter the value of the Adjacent side: "))
opp = float(input("Enter the value of the Opposing side:"))

hypo = math.sqrt(adj*adj + opp*opp)

print("The length of hypotenuse is: ", hypo)

Tl = adj + opp + hypo

print ("The total length of the triangle is: ", Tl)

Ta = (adj * opp)/2

print ("The area of the triangle is: ", Ta)

Vt = math.asin(opp/hypo)

print ("The value of angle theta is:", Vt)
