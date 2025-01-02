"""
Day 7: Tuples and Sets in Python
Learn:
Tuples:

Tuples are immutable ordered collections, similar to lists but cannot be modified after creation.
Useful for data that should not change.
python
Copy code
# Creating a tuple
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Accessing elements
print(len(my_tuple))  # Length of the tuple
Sets:

Sets are unordered collections of unique elements.
Useful for removing duplicates and performing set operations like union, intersection, etc.
python
Copy code
# Creating a set
my_set = {1, 2, 3, 3}  # Duplicates are ignored
print(my_set)  # Output: {1, 2, 3}

# Adding and removing elements
my_set.add(4)
my_set.remove(2)
print(my_set)
Practice Tasks:
Create a tuple of five numbers and print the sum of its elements.
Write a program to find the union and intersection of two sets entered by the user.
Given a list with duplicate elements, create a set to remove duplicates and print the unique elements.
"""

tup= (1,5,8,9,6)
s=0
for i in tup:
    s+=i
print(s)
"""    this also works
tup= tuple(map(int, input("Input tuple: ").split()))
s=0
for i in tup:
    s+=i
print(s)
"""

l= [1,2,5,6,97,8,4,6,45,8,7,6,1,3,6,4,78,5,21,3,6,45,8,2]
m=set(l)
print(l)
l=[1,1,1,1,2,3,3]
print(m)

set1= set(map(int, input("Set 1: ").split()))
set2= set(map(int, input("Set 2: ").split()))

union_set_operator= set1 | set2
print(union_set_operator)
union_set_method= set1.union(set2)
print(union_set_method)

intersetion_set_operator= set1&set2
print(intersetion_set_operator)
intersetion_set_method= set1.intersection(set2)
print(intersetion_set_method)