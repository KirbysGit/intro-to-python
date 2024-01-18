# Colin Kirby
# betterlist.py
# program written
# written for COP2500C


# PROBLEM STATEMENT:
# Small Monster collectors often have problems keeping track of their
# small monsters, so with this code I have created an efficient way of tracking
# and sorting through these inputted small monsters by type or name.

# Has a couple of programming limtis such as if a small monster with same
# name is entered twice, you can only call back the earliest version of that
# small monster. Also, when shutting down program requires double confirmation.

# Functions:

# pretty_list: uses a function with the parameters of a list and a string
# for the title and prints a properly indented and numbered list.
def pretty_list(thelist,title):
    print(title)
    n = 0
    for item in thelist:
        n = n + 1
        print("     ",n,f"- {item.capitalize()}")

# value_1: serves as the SM Tracker adder function as it request
# input from user of both a small monster and its type. Will cause
# error if there is not a small monster and its type separated by a
# comma.
def value_1():
    sm2 = input("Enter the small monster and it's type separated by commas: ")
    sm2 = sm2.lower()
    tr1 = sm2.split(",")
    if len(tr1) == 2:
        for i in range(len(tr1)):
                tr1[i] = tr1[i].strip()
        smcollection.append(tr1[0])
        typelist.append(tr1[1])
        print("Small Monster was added to Tracker!")
    else:
        print("Please enter the small monster AND its type.")

# value_2: serves at the SM Tracker call back as it request a
# input from the user of the SM they wish to call back. Will print
# a statement if the inputted sm is not already in smcollection list.
def value_2():
    cb2 = input("Enter the small monster you wish to call back: ")
    cb2 = cb2.lower()
    if cb2 in smcollection:
        n1 = smcollection.index(cb2)
        n1 = n1 + 1
        cb2 = cb2.capitalize()
        for i in range(len(typelist)):
            typelist[i] = typelist[i].capitalize()
        print(" ")
        print(cb2,":")
        print(" Type:",(typelist[n1 - 1]))
        print(" Number:",n1)
        for i in range(len(typelist)):
            typelist[i] = typelist[i].lower()
    else:
        print(" ")
        print("Sorry, that small monster is not in the tracker.")

# value_5: serves to allow the user to sort through their SM's by
# type, so following a user input it will print all of the SM's
# of that type in a properly formatted list. Will print an empty list
# if the inputted type has no small monsters to go with it.
def value_5():
    print("You can now sort through your small monsters by type.")
    print(" ")
    type1 = input("Enter a type of small monster you wish to sort through by: ")
    type1 = type1.lower()
    stypelist = []
    for i in range(len(typelist)):
        if typelist[i] == type1:
            stypelist.append(smcollection[i])
    pretty_list(stypelist, f"Your {type1}-type small monster(s):")

# tracker_code: calls back all the other functions to create a completely
# user inputted program allowing the user to choose what they want to do
# through use of if-elif-else statements by allowing them to input a value
# based off their next choice of step.
def tracker_code():
    print(" ")
    a1 = input("Please enter value here: ")
    print(" ")
    # once user input is 3 it ends loop
    while a1 != "3":
        # if user input is 1 then refers to add SM function
        if a1 == "1":
            value_1()
            print(" ")
            a1 = input("Enter a value here: ")
            print(" ")
        # if user input is 2 then refers to callback SM function
        elif a1 == "2":
            value_2()
            print(" ")
            a1 = input("Enter a value here: ")
            print(" ")
        # if user input is 4 prints the help statment
        elif a1 == "4":
            print(x)
            print(" ")
            a1 = input("Enter a value here: ")
            print(" ")
        # if user input is 5 refers to the sort function
        elif a1 == "5":
            value_5()
            print(" ")
            a1 = input("Enter a value here: ")
            print(" ")
        # if user input is not 1-5 then prints this statment
        else:
            print("""Please enter one of the values mentioned,
If you wish to see the help statement please enter "4".""")
            print(" ")
            a1 = input("Enter a value here: ")
            print(" ")
    shutdown()
    start_leave()
    print(" ")
    print("To confirm please enter 'Start' or 'Leave' in the area below.")
    start_leave()


# shutdown: simplfies large block of text that allows me to call back
# this message without the need to type it all out again.
def shutdown():
    print("You have now turned off the S.M. Tracker.")
    print(" ")
    print("""If you wish to add or sort through your Small Monsters
anymore please enter "Start" in the area below.""")
    print(" ")
    print("""If you wish to completely shut down the S.M. enter
"Leave" in the area below.""")
    print(" ")

# start_leave: creates a function that allows user two options of
# Start the tracker back up or completely shutting down the tracker
# through an if then statement.
def start_leave():
    b1 = input("Enter here: ")
    if b1 == "Start":
        print(" ")
        print("Welcome back to the S.M. Tracker!")
        tracker_code()
    elif b1 == "Leave":
        print(" ")
        print("S.M. Tracker is now OFF.")

# Main code:

# Introduction message to tracker and First inputs for small monsters.
print("Hello!, Welcome to your own personal S.M. Tracker!")
print(" ")
print("""By entering in what you catch to this program
you can sort through and better organize your
assortment of small monsters!""")
print(" ")
sm1 = input("So, to get started please enter a small monster: ")
sm1 = sm1.lower()
print(" ")
t1 = input("Now, What type was that small monster? ")
t1 = t1.lower()
print(" ")

# Creates two list and appends early inputted items.
smcollection = []
typelist = []
smcollection.append(sm1)
typelist.append(t1)

# Explaining call back function in this program.
print("""You have now saved your first small monster and its
type to the S.M. Tracker! You can now efficiently track 
your small monsters by type!""")
print(" ")
print("""If you wish to call back your small monster you
may just enter it and it will print it with
a clean format!""")
print(" ")

# First callback function. Provides a "error" statment
# if the small monster is not found in smcollection.
cb1 = input("Please enter a small monster you wish to call back: ")
cb1 = cb1.lower()
print(" ")
if cb1 in smcollection:
    n = smcollection.index(cb1)
    n = n + 1
    cb1 = cb1.capitalize()
    print(cb1,":")
    print("  Type:",t1.capitalize())
    print("  Number:", n)
else:
    print("Sorry, that small monster was not found in the tracker.")
    print(" ")
    cb2 = input("""Please re-enter the small monster you wish to call back here
(Hint: Just re-enter the pokemon you entered in first): """)
    cb2 = cb2.lower()
    print(" ")
    n = smcollection.index(cb2)
    n = n + 1
    cb2 = cb2.capitalize()
    print(cb2,":")
    print("  Type:",t1.capitalize())
    print("  Number:", n)

# Sets x equal to the help statement so it is easier to call back.
print(" ")
x = ("""If you wish to add a small monster please enter "1".
If you wish to call back a small monster please enter "2".
If you wish to exit the tracker please enter "3".
If you wish to call back this help statment again enter "4".
If you wish to print more sorting options enter "5". """)

# Begins the user control.
print("Now the S.M. Tracker is under your control!")
print(x)

# Calls back function tracker_code.
tracker_code()


# Checklist:
# Accept Input - done
# Produce Output - done
# Use both string and numeric variables meaningfully - done
# Use list to manage data - done
# Use conditional statements to make decisions - done
# Use loops to deal with data iteratively - done
