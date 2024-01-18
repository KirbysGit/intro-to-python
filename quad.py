# Colin Kirby
# quad.py
# written to solve the quadratics roots of a equaton based off the user
# inputted coefficient(a,b,c) by using definitions and specific conditions.
# written for COP2500C

# Imports the math library
import math

# Serves as the function for the determinant in which determinant equals the
# b^2 - 4(a)(c) which helps us to find how many roots equation has
def determinant(a,b,c):
    x = (b * b) - 4*(a)*(c)
    return x

# Serves as the function for the positive side of the quadratic equation in
# which the determinant is added onto the rest of the numerator.
def root_one (a,b,x):
    pos_root = (-(b) + math.sqrt(x))/(2 * (a))
    return pos_root

# Serves as the function for the negative side of the quadratic equation in
# which the determinant is subtracted from the rest of the numerator.
def root_two (a,b,x):
    neg_root = (-(b) - math.sqrt(x))/(2 * (a))
    return neg_root

# Main code begins here:

# Prompts the user for three coefficients (a,b,c)
a = (float(input("Enter coefficient a: ")))
b = (float(input("Enter coefficient b: ")))
c = (float(input("Enter coefficient c: ")))

# Serves to set the discriminant equal to a variable to simplify the parameters.
x = determinant(a,b,c)

# Serves as the conditions for outputted text.

# Serves to stop the possibility of error later by seeing if discriminant is
# less than 0 it prints the message that it instead has complex roots.
if(determinant(a,b,c) < 0):
    print("Sorry, that quadratic has complex roots.")
# Serves for the multiple roots, b/c if root_one doesnt equal root_two it means
# they are different numbers and the quadratic equation has two roots.
elif(root_one(a,b,x) != root_two(a,b,x)):
    print("That quadratic has two roots:", root_one(a,b,x),"and", root_two(a,b,x))
# Serves for the single roots as if root_one = root_two then there is only one
# root when it then prints that the quadratic equation has only one root.
elif(root_one(a,b,x) == root_two(a,b,x)):
    print("That quadratic has one root:", root_one(a,b,x))
