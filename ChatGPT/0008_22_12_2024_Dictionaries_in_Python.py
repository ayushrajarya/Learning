"""
Day 8: Dictionaries in Python
Learn:
What are Dictionaries?

Dictionaries are unordered collections of key-value pairs.
Keys are unique, and each key is mapped to a value.
python
Copy code
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Access value by key
Adding and Removing Items:

You can add new key-value pairs, update existing values, or remove items.
python
Copy code
my_dict["city"] = "New York"  # Add a new key-value pair
my_dict["age"] = 26  # Update value of existing key
del my_dict["name"]  # Remove a key-value pair
Methods for Dictionaries:

keys(), values(), items(), get(), pop()
python
Copy code
print(my_dict.keys())  # Returns the keys
print(my_dict.values())  # Returns the values
print(my_dict.items())  # Returns key-value pairs as tuples
Practice Tasks:
Create a dictionary with your name, age, and city. Add a new key for your profession and update your age.
Write a program to remove a key-value pair from a dictionary based on user input.
Given a dictionary, print all the keys and their corresponding values.
"""

my_dict= {"name": "Ayush", "age": 25, "city": "Hyd"}
print(my_dict)
my_dict["profession"]="Software Engineer"
my_dict["age"]=26
print(my_dict)

del my_dict["age"]

