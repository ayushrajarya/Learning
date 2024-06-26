#1
def clinic():
    print("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()
clinic()

#2
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

#3
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three =  False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

#4
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 6>7

# Make me true!
bool_three = 10**2==100

# Make me false!
bool_four = 'a'!='a'

# Make me true!
bool_five = 3-2
print(bool_five)
"""
Writing an expression and giving it a value might not work (not sure about this though)
"""

#9
"""
Boolean operators are not just evaluated from left to right. There is an order of operations for boolean operators.
1. "NOT" is evaluated.
2. "AND" is evaluated next.
3. "OR" is evaluated last.
"()" can be used to specify order.
"""

#10
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = 1==1 and 'a'!='b' or not 6==7

# Make me false!
bool_three = not 't'=='t' and (4==4 or 6!=8)

# Make me true!
bool_four = 6!=7 or 9+1==10 and not 10**2==100

# Make me true!
bool_five = not 6==7 and not 5+1==5 or 'o'!='p' or not 6==9

#11
response = 'Y'

answer = "Left"
if answer == "Left":
    print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

#12
def using_control_once():
    if 6==6:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print (using_control_once())
print (using_control_again())

#13
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return  6==7      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return    6!=6    # Make sure this returns False

print(black_knight())
print(french_soldier())

#14
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0
        
print (greater_less_equal_5(4))
print (greater_less_equal_5(5))
print (greater_less_equal_5(6))

#15
# Complete the if and elif statements!
def grade_converter(grade):
    if grade >=90:
        return "A"
    elif grade>=80 and grade <=89:
        return "B"
    elif grade >=70 and grade <=79:
        return "C"
    elif grade >=65 and grade <=69:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print (grade_converter(92))

# This should print a "C"
print (grade_converter(70))

# This should print an "F"
print (grade_converter(61))


















