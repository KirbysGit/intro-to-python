# Colin Kirby
# movies.py
# written to create the total cost of tickets based off user inputted value
# written for COP2500C

# This line promtps the user for the number of moviegoers in the group.

a = int(input("Enter the number of moviegoers:"))

# Acts as the price of your ticket in a group under 25 as you are
# the only Small Monster Collector
u = 9.50

# These act as the conditions for the two different types of groups as it
# accepts the value then determines if the number of moviegoers is less than 25,
# and thus gets the group discount, however in this paragraph of code below, it
# provides the equation for when a group is below 25, and thus the price per
# person (other than you) is 12, while the price of your ticket is 9.5 which is
# then combined to create the total ticket cost in the output

if(a < 25):
    b = 12
    p = u + (b * (a-1))

# This acts as the else condition such that if the group does have more than 25
# people then the ticket price for everyone is only 7.25. And disregards, the
# Small monster collector discount as 7.25 is less.

else:
    b = 7.25
    p = b * a

# This then prints the correct output of the equations
print ("The total ticket price is $", p,".")
