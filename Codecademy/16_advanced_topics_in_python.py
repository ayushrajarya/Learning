#1
my_dict= {"one":1, "two": 2, "three":3}
print(my_dict.items()) # this returns an array of tuples with each tuple consisting a key/value pair
print(type(my_dict.items()))
x=my_dict.items()
print(x)

#2
my_dict= {"one":1, "two": 2, "three":3}
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#3
my_dict= {"one":1, "two": 2, "three":3}
for k in my_dict:
    print(k,my_dict[k])
"""
Order is not specified in this and output might very well differ from machine to machine
"""

#4
# else in list comprehenssion
l=[i**2 if i%2==0 else i**3 if i%3==0  else "odd" for i in range(10)]
print(l)
"""
Typical example to use if else if else in a list comprehension
"""

#5
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
# Complete the following line. Use the line above for help.
even_squares = [i**2 for i in range(1,11) if i%2==0]
print (even_squares)

#6
cubes_by_four= [x**3 for x in range(1,11) if x**3%4==0]
print(cubes_by_four)

#7
"""
List slicing
[start: end: stride]
where startis inclusive and end is extrusive that is end will not be part of list like range function.
"""

#8
my_list = list(range(1, 11)) # List of numbers 1 - 10
# Add your code below!
print(my_list[::2])
print(my_list[::-1])
print(my_list[::-2])
"""
first semi colon represents that while list is to be taken as start and end not specified.
Second semi colon implies the stride.
if the integer is positive then it takes elements from left to right.
if the stride is negative then it starts from right and goes to left.
"""

#9
my_list = range(1, 11) 
# this won't make it a list this will just show as a range
# above would still work with a for loop but it ould be stored as a range function only
# that is the class is a range
print(type(my_list))
backwards= my_list[::-1]
print(backwards)
for x in my_list:
    print(x)