"""
Day 6: Lists in Python
Learn:
What are lists?
A list is an ordered collection in Python that can hold a mix of data types (e.g., integers, strings, other lists).
Example Input:

python
Copy code
numbers = [10, 20, 30, 40, 50]
print(numbers)  # Output: [10, 20, 30, 40, 50]
Creating and Accessing Elements:
You can create lists using square brackets [] and access elements using indices.
Example Input:

python
Copy code
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Access the first element: "apple"
print(fruits[-1])  # Access the last element: "cherry"
Adding, Removing, and Modifying Elements:
Lists are mutable, so you can add, remove, or change elements.
Example Input:

python
Copy code
# Adding Elements
fruits.append("orange")  # Add "orange" to the end of the list
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]

# Removing Elements
fruits.remove("banana")  # Remove "banana"
print(fruits)  # Output: ["apple", "cherry", "orange"]

# Modifying Elements
fruits[1] = "grape"  # Change "cherry" to "grape"
print(fruits)  # Output: ["apple", "grape", "orange"]
Sorting and Slicing:
Lists can be sorted or sliced for specific portions.
Example Input:

python
Copy code
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Sort the list in ascending order
print(numbers)  # Output: [1, 1, 3, 4, 5]

# Slicing a List
print(numbers[1:4])  # Get elements from index 1 to 3: [1, 3, 4]
Practice Tasks:
Favorite Movies:
Create a list of your favorite movies. Add another movie to the list and print the updated list.
Example:

python
Copy code
movies = ["Inception", "Interstellar", "The Dark Knight"]
new_movie = input("Enter another favorite movie: ")
movies.append(new_movie)
print("Updated movies list:", movies)
Find Largest Number:
Write a program to find the largest number in a list of numbers entered by the user.
Example:

python
Copy code
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest = max(numbers)
print("The largest number is:", largest)
Reverse a List:
Reverse a list without using the reverse() method.
Example:

python
Copy code
numbers = [10, 20, 30, 40, 50]
reversed_list = numbers[::-1]  # Slice with step -1
print("Reversed list:", reversed_list)
"""

movies=["3 idiots", "die hard", "Spider-man"]
movies.append("Harry Potter")
print(movies)
print(movies+["Contratiempo"]) #this also worked

"""
nums=list(input('Input numbers: ')) #this will take individual letter, digit and make it one element as string.
print(nums)
"""
nums = list(map(int, input('Input numbers separated by spaces: ').split()))
print(nums)

"""
Explanation
input(): Takes the input from the user as a string.
.split(): Splits the string into a list of substrings based on spaces (default).
map(int, ...): Converts each substring to an integer.
list(): Converts the map object into a list.
"""
print(max(nums))

# reversing a list
reversed_nums = []
for i in range(1, 1+len(nums)):
    reversed_nums.append(nums[-i])

print(reversed_nums)
print(nums[::-1])

reversed_nums_slicing = nums[::-4]
#this will take last and then every second element can be done with any 'i' number
print(reversed_nums_slicing)

rev=list(reversed(nums))
print(rev)