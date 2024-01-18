# Colin Kirby
# lineplotter.py
# written to display an equation line and the values of the line
# at specific x values
# written for COP2500C

# prompts user for two "float" inputs of the slope of the line and the
# intercept of the line
m = float(input("Enter the slope: "))
b = float(input("Enter the intercept: "))

# prints the whole equation of the line based off of user inputted values
print("y =", m,"x +",b,":")

#uses variables to set a base for the loops
x = 0
i = 1

# use a "for" loop for first 10 x-values and end loop
for x in range(0,11,1):
    y = (m*x) + b
    print("At x =", x, ", y =", y)

# use a "while" loop for the sort of exponential step to display 100, 1000, etc.
# and print the values of that
while (x <= 10000):
    i = i + 1
    x = 10**i
    y = (m*x) + b
    print("At x =", x, ", y =", y)
    
    

            
    
    
