# Colin Kirby
# betterlist.py
# program written to create and display a list based off of user criteria.
# written for COP2500C


# pretty_list: prints a properly numbered, capitalized, and indented list
# based off of the items accumulated in the courselist and the
# title based off entered parameter. Will cause an error if parameters
# are not a list, and the title is not a proper string.
def pretty_list(courselist,title):
    print(title)
    n = 0
    for item in courselist:
        n = n + 1
        print(" ",n,f": {item.capitalize()}")
    print(" ")

# take_course: request input from user based on courses they wish to add,
# then appends the items that were split from user inputted string into courselist,
# and calls back pretty_list to properly format the list.

def take_course(courselist):
    course = input("What courses would you like to take? ")
    course = (course.lower())
    course1 = course.split(",")
    for item in course1:
        courselist.append(item.strip())
    pretty_list(courselist, "You are currently taking these courses: ")

# remove_course: request input from user based on courses they wish to remove,
# then appends those item to a new list where it it then reference and appended
# to courselist with proper format through "strip" and finally printed with
# a proper format with function pretty_list.

def remove_course(courselist):
    course = input("What course would you like to drop? ")
    course = (course.lower())
    course1 = course.split(",")
    course2 = []
    for item in course1:
        course2.append(item.strip())
    for item in course2:
        if item in courselist:
            courselist.remove(item.strip())
    pretty_list(courselist, "You are currently taking these courses: ")
    
# Main Code begins here:

# creates empty list.

courselist = []

# prints You aren't currently taking any courses with an open line.

print("You aren't currently taking any courses.")
print(" ")

# sets x equal to 0 so the loop can function.
x = 0

# creates a while loop so while x DOES NOT equal 5 it will continue
# but when it hits 5 it will end the loop.
while x != 5:
    # creates an if-else statement in which x is less than 5 it
    # will call back function take_course, then take the len of
    # the list so it can properly continue loop.
    if x < 5:
        take_course(courselist)
        x = len(courselist)
    # creates the elif part of statement so while x is greater
    # than 5 it will call back function remove_course, then take
    # the len of
    elif x > 5:
        remove_course(courselist)
        x = len(courselist)

# prints Done once loop is finished.
print("Done!")




