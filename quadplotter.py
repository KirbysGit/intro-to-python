# Colin Kirby
# quadplotter.py
# written to present the equation for a parabola and its y values at specific
# x values through use of functions, loops, and user inputted coefficients.
# written for COP2500C

# Acts as the function for the equation for a quadratic function (ax^2 + bx + c)
# and returns that value.
def quad_value(a,b,c,x):
    y = a*(x*x) + b*x + c
    return y
# Calls back the previous functions value and prints it with the corresponding
# x value.
def quad_print(a,b,c,x):
    y = quad_value(a,b,c,x)
    print("At x =", x,", y =", quad_value(a,b,c,x))

# Main code starts here:

# Prompts user for three inputted variables (a,b,c)
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Outputs quadratic equation in the form of text based off the previous inputs.
print("Parabola: y =",a,"x^2 +", b,"x +",c)

# Creates a loop for range 0,9 where the function quad print is called which
# then goes through the defintion which in this case is printing the x and y
# value at specific x values.
for x in range (0,10):
    quad_print(a,b,c,x)
# Sets x originally to 1.
x = 1
# Creates a loop in which while x is less than the specific value x is multipled
# by 10 over and over again to display a sort of exponential increase in x value
# , where it then calls the function quad_print to display those specific values
while x < 10000000:
    x = x * 10
    quad_print(a,b,c,x)


