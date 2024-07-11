#01_python_syntax.py
#this is a comment
"""
this is also a comment
this way you can write multi line comments
print("see nothing got printed")
"""
print("this \nis printed in next \"line\" with quotes and a \\ backlash")

# multi-line string in a variable
haiku= """The old pond,
A frog jumps in:
Plop!"""

marks= '79'
marks= int(marks)
print(type(marks))
# similarlly, int, str, float
fl='-3.5'
fl=float(fl)
# this will throw error "ValueError: invalid literal for int()" as string is not an integer
# fl='-2.6'
# fl= int(fl)
print(fl)
print(type(fl))

fl=int(fl)
#this works as this converts float to int removing decimal part
print(fl)
print(type(fl))

#02_strings_console_output.py

"""
String methods
len(x)
x.lower()
x.upper()
str(x)
"""
"""
methods that use dot notation only work with strings
on the other hand, len() and str() can work on other data types
"""
string_1 = "Camelot"
string_2 = 2256

print ("Let's not go to %s. 'Tis a silly %02d." % (string_1, string_2))
print ("Let's not go to %s. 'Tis a silly %015d." % (string_1, string_2))
print ("Let's not go to %s. 'Tis a silly d%6d." % (string_1, string_2)) 
# 4 places are skipped rest are printed as space
"""
padding in integer can be done with % formatting like above.
Only 0 can be added for padding, next write how many characters are needed.
d represents that it is an integer.
if number of digits in integer is more than the input in padding then whole variable is printed.
It will not remove any digits.
"""

#03_datetime_lib.py

from datetime import datetime
now=datetime.now()
print(now)
print( now.date)
print("%02d/%02d/%04d" % (now.day, now.month, now.year))
print("%02d:%02d:%02d" % (now.hour,now.minute, now.second))
print("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))

#04_conditionals_and_control_flow.py

bool_five = 3-2
print(bool_five)
"""
Writing an expression and giving it a value might not work (not sure about this though)
"""
"""
Boolean operators are not just evaluated from left to right. There is an order of operations for boolean operators.
1. "NOT" is evaluated.
2. "AND" is evaluated next.
3. "OR" is evaluated last.
"()" can be used to specify order.
"""

#06_functions.py

"""
def some_funtion(x,y,z):
    here x,y,z are parameters and values that are fed in the funtion for them are called arguments.
"""
# from module import function
"""
if you import a function directly then there is no need to write module.function again and again.
Otherwise we would have to write math.sqrt(25) just now to achieve the same thing.
"""
# to import everything and not wanting to write the funtion name again and again then do universal import
# from module import *
"""
This may look good but when there are many modules in a program then tracking each function and variable name is a hassle
The conflict may arrise if two functions or variables have same name and one of them is being imported from a module
This may result in unexpecte result from the script.
So, it is beter to import the module and then call with module.
Over that it fills your program with a ton of variable and functions.
"""
"""
This will give everything available in the module.
import module
print(dir(module))
"""
"""
maximum = max(02024,12,6,6,45,6,65,6,5,66,6,5)
print (maximum)
This throws an error saying leading zeros not allowed look into this more
"""

#09_a_day_at_supermarket.py
# a dictionary has to initialized before assigning any value
""" Below will work though as kay and value pair is given while initialising
prices={"banana":4, "apple":2, "orange": 1}
print(prices)

Below will not work without initialising en empty ditionary
prices["banana"]=4
prices["apple"]=2
print(prices)
"""

"""
A variable initalised in the main code and called in the function will work just fine.
If any change is done in a funtion to that variable then the main variable will be chnaged.
"""
def compute_bill(food):
    total=0
    for f in food:
        if stock[f]>0:
            total+= prices[f]
            stock[f]-=1
    return total
prices = {"banana": 4,  "apple": 2,  "orange": 1.5,"pear": 3}
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
t=compute_bill(["banana","apple","orange", "pear"])
print(t)
print(stock)
shopping_list = ["banana", "orange", "apple"]
"""
This affected the variable "stock" even when it was not an argument for the function "compute_bill"
"""

#10_student_becomes_the_teacher.py
"""
Assume there are dictionaries with names "lloyd", "alice" and "tyler"
And inside them there are keys namely "name", "homework", "quizzes", "tests"
students=[lloyd,alice,tyler]
#replacing dictionary name with variable
for s in students:
    print(s["name"])
    print(s["homework"])
    print(s["quizzes"])
    print(s["tests"])
this will fetch the value from the dictionary
"""

#11_lists_and_functions.py
"""
removing items from a list
assume a list "n"
n.pop(index): removes item at an index (this returns the removed item)
n.remove(item): removes first occurance(lowest index if item is present multiple times) of the item
del(n(index)): removes item at an index (this will not return the item)
del n: this will delete the whole list
"""

#Remove and return the last element from the list
#last_element = list.pop()
#print(last_element)
#Remove the first occurrence of the element 3 from the list
#x=list.remove(3)
#print(x) this will not print anything

"""
range(stop): 0,1,2,3,.....,stop-2, stop-1
range(start,stop): start, start+1, start+2,....., stop-2, stop-1
range(start,stop,step): start, start+1*step, start+ 2*step,...., stop-2*step, stop-1*step
start defaults to 0 and step defaults to 1 unless specified.
"""

"""
Iterating through a list
method 1: iterating through items in list: List modification is not possible
method 2: ierating through the indexes: list can be modified while using indexes
"""

"""
Joining two lists as simple as adding them.
Second list will be appended at the end of the first list in the same order
"""

#13_loops.py
"""
While/else
while/else is similar to if/else.
Else part is executed once the conition in while is evaluated as 'False'.
While loop is entered and False condition is evaluated then Else part will be executed.
While entering the while loop the condition if eveluated to be false in the first iteration then also Else part will be executed.
Else part won't be executed only when the loop is broken because of a "break statement"
"""

from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

"""
to stay in the same line to print next thing in the same line add end in the print statement.
print("<whatever intended to be printed>", end="")
this end can have any other string also which can be used for concatenation.
"""

"""
While iterating through a dictionary the key is picked.
And the key can be used to get the value
"""

"""
Enumerate gives index and item pair that is index of the corresponding element which was picked.
This way evey if there are multiple duplicates it will give the exact index of the item which is picked in that iteration.
"""

"""
zip creates group of elements and stops at the shortest list.
Zip can take two or more lists.
for a, b,c in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(a,b,c))
enumerate also works with zip as shown above.
for ind,t in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(t))
  print(ind)
"""

"""
Just like while/else, for/else can also be made
else condition is ony executed when for ends normally and through a break statement.
"""

#14_practie_make_perfect.py
"""
if else in return example above 
return something if condition1 else something_else
"""

def is_int(x):
    print(x%1)
    return True if x%1==0 else ("Negative" if x<0 else ("Positive" if x>0 and x<1 else "Greater than 1"))
print(is_int(2.3))
"""
In return statement elif won't work and for a better code readability thou shall not write too much in one line
But it can still be done as shown above.
First check one if condition
then in else within parenthesis write another if condition
In this way if can be nested infinite times in the else of the preceeding condition  
"""

def median(numbers):
    numbers.sort() # this works
    # numbers = numbers.sort() does not work
    """
    numbers=sorted(numbers)   This also works
    """
    length=len(numbers)
    return numbers[length//2] if length%2 !=0 else (numbers[length//2]+numbers[length//2-1])/2.0

#16_advanced_topics_in_python.py
my_dict= {"one":1, "two": 2, "three":3}
print(my_dict.items()) # this returns an array of tuples with each tuple consisting a key/value pair

my_dict= {"one":1, "two": 2, "three":3}
for k in my_dict:
    print(k,my_dict[k])
"""
Order is not specified in this and output might very well differ fro machine to machine
"""

# else in list comprehenssion
l=[i**2 if i%2==0 else i**3 if i%3==0  else "odd" for i in range(10)]
print(l)
"""
Typical example to use if else if else in a list comprehension
"""

"""
List slicing
[start: end: stride]
where startis inclusive and end is extrusive that is end will not be part of list like range function.
"""

my_list = list(range(1, 11))
print(my_list[::2])
print(my_list[::-1])
print(my_list[::-2])
"""
first semi colon represents that while list is to be taken as start and end not specified.
Second semi colon implies the stride.
if the integer is positive then it takes elements from left to right.
if the stride is negative then it starts from right and goes to left.
"""

my_list = range(1, 11) 
# this won't make it a list this will just show as a range
# above would still work with a for loop but it ould be stored as a range function only
# that is the class is a range
print(type(my_list))
backwards= my_list[::-1]
print(backwards)
for x in my_list:
    print(x)

"""
lambda is a small anonymous function.
It can take any number of arguments, but can only have one expression.
"""
my_list = list(range(16))
test=lambda x: x%3==0
print(test(5)) # this will compare and written a boolean
test=lambda x: x%3
print(test(5)) # this shows remainder
# print(lambda x: x%3==0, [0,1,2,3,4,5,6,7,8,9,10])
test= list(filter(lambda x: x%3 == 0, my_list))
# test= filter(lambda x: x%3 == 0, my_list) this will somehow not store it as list
# we have to specify to convert to list as shown above
print(test) # this filters and shows elements which have 0 remainder

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print( list(filter(lambda x : x== "Python", languages)))
"""
It is imperative that we give a lambda function in filter to filter out.
A defined functin can also be used to filter out the result.
"""

#17_introdution_to_bitwise_operators.py
print (5 >> 4 ) # Right Shift
print (5 << 1 ) # Left Shift
print (8 & 5   )# Bitwise AND
print (9 | 4   )# Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT
