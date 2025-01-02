"""
Day 2: Variables and Data Types
Learn:

Variables in Python: How to declare and assign them.
Common data types: Strings (str), Integers (int), Floats (float), and Booleans (bool).
Rules for naming variables.
Examples:

python

    name = "Alice"  
    age = 25  
    is_student = True  
    height = 5.7  

print(f"Name: {name}, Age: {age}, Student: {is_student}, Height: {height}")  
Practice:

Declare variables for your favorite movie, its release year, and whether you recommend it. Print them all in a sentence.
Write a program to calculate the area of a rectangle with the given length = 8 and width = 3. Print the result.

"""
"""
Data types in Python
Most common

1. Numeric Types
int: Represents integers (whole numbers).
Example: x = 5, y = -10
float: Represents decimal (floating-point) numbers.
Example: pi = 3.14, temperature = -27.5
complex: Represents complex numbers with a real and imaginary part.
Example: z = 3 + 4j
2. Text Type
str: Represents strings (sequences of characters).
Example:
python
Copy code
name = "Alice"
message = "Hello, World!"
3. Boolean Type
bool: Represents True or False values (logical type).
Example:
python
Copy code
is_valid = True
is_empty = False
4. Sequence Types
list: A mutable collection of ordered items, which can be of different types.
Example:

python
Copy code
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "text", True]
tuple: An immutable collection of ordered items.
Example:

python
Copy code
coordinates = (4, 5)
colors = ("red", "blue", "green")
range: Represents a sequence of numbers. Commonly used in loops.
Example:

python
Copy code
numbers = range(1, 10)
5. Mapping Type
dict: A collection of key-value pairs.
Example:
python
Copy code
person = {"name": "Alice", "age": 25, "is_student": True}
6. Set Types
set: An unordered collection of unique items.
Example:

python
Copy code
unique_numbers = {1, 2, 3, 3}
# Output: {1, 2, 3}
frozenset: An immutable version of a set.
Example:

python
Copy code
frozen = frozenset([1, 2, 3])
7. Binary Types
bytes: Immutable sequence of bytes.
Example:

python
Copy code
byte_data = b"Hello"
bytearray: Mutable sequence of bytes.
Example:

python
Copy code
byte_array = bytearray(b"Hello")
byte_array[0] = 87  # Changes to "Wello"
memoryview: A memory view object of a bytes-like object.
Example:

python
Copy code
mv = memoryview(byte_data)
8. None Type
NoneType: Represents a null or "no value" type.
Example:
python
Copy code
value = None


"""