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

#10
to_one_hundred = range(101)
backwards_by_ten= list(to_one_hundred[::-10])
print(backwards_by_ten)

#11
to_21=list(range(1,22))
odds=to_21[::2]
print(odds)
middle_third= to_21[7:14]
print(middle_third)

#12
"""
lambda is a small anonymous function.
It can take any number of arguments, but can only have one expression.
"""
my_list = list(range(16))
test=lambda x: x%3==0
print(test(5))
test=lambda x: x%3
print(test(5))
# print(lambda x: x%3==0, [0,1,2,3,4,5,6,7,8,9,10])
test= list(filter(lambda x: x%3 == 0, my_list))
# test= filter(lambda x: x%3 == 0, my_list) this will somehow not store it as list
# we have to specify to convert to list as shown above
print(test)

#13
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print( list(filter(lambda x : x== "Python", languages)))
"""
It is imperative that we give a lambda function in filter to filter out.
A defined functin can also be used to filter out the result.
"""

#14
squares= list([x**2 for x in range(1,11)])
print(list(filter(lambda x : x>=30 and x<=70, squares)))

#15
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
print(movies.items())

#16
threes_and_fives = [x for x in range(1,16) if x%3==0 or x%5==0]
# x needs to be same in picking the item and inside comprehension definition
print(threes_and_fives)

#17
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message= garbled[::-2]
print(message)

#18
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = "".join(list(filter(lambda x : x!='X', garbled)))
print(message)