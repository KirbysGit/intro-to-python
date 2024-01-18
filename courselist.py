# Colin Kirby
# courselist.py
# program written to create a courselist for the user based off inputted strings.
# written for COP2500C


# indent_list: prints a properly formatted this given a list, and title, with indents
# and numbered points. Will cause an error if parameters are not strings.
def indent_list(thelist,title):
    print(title)
    n = 0
    for item in thelist:
        n = n+1
        print("    ",n,f"- {item}")

# course_ifelse: creates an if-else statement in which if "EXIT" is entered in the input
# then it will just print the courselist. Else while it is not "EXIT" it will add that
# course to the end of the list and prompt user for another course. Will cause an error if
# course is not a string.
def course_ifelse(course):
    if course == "EXIT":
        print(courselist)
    else:
        while course != "EXIT":
            courselist.append(course)
            course = input("Enter a course or enter 'EXIT' to stop entering courses. ")
# pop_course: deletes the requested numbered course based off index which is x - 1. Will
# cause an error if x is not an int.
def pop_course(x): 
    x = x - 1
    courselist.pop(x)

# course1_ifelse: creates an if-else statment in which if "EXIT" is entered it will just
# print the courselist, Else, if a course is entered it will add that course to the end
# of the courselist then sort the list, and the finally print the this by calling back
# function indent_list.
def course1_ifelse(course1):
    if course1 == "EXIT":
        indent_list(courselist, "Your Course List: ")
    else:
        courselist.append(course1)
        courselist.sort()
        indent_list(courselist, "Your Course List: ")

# Main Program:

# Creates an empty list.
courselist = []

# Prompts user for a course or tells them to enter "EXIT" to end the input.
course = input("Enter a course or enter 'EXIT' to stop entering courses. ")

# Calls function course_ifelse.
course_ifelse(course)

# Sorts the list, then calls function indent_list.
courselist.sort()
indent_list(courselist, "Your Course List: ")


# Prompts user for the number of the course they wish to drop and sets it
# equal to x.
x = int(input("Enter the number of the course you wish to drop, ex. If you wish to drop course 1 enter '1': "))

# Deletes the inputted course from list based off its number then prints the list by
# calling function indent_list.
pop_course(x)
indent_list(courselist,"Your Course List: ")

# Prompts user for another course they want to enter, if not they enter "EXIT" to stop
# entering a course.
course1 = input("If you wish, Enter another course to add to list, if not enter 'EXIT' to stop entering courses. ")

# Calls function course1_ifelse.
course1_ifelse(course1)



                 




