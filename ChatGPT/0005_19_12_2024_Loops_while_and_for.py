"""
Day 5: Loops (while and for)
Learn:

Using while loops for repetitive tasks until a condition is false.
Using for loops to iterate over sequences like lists, strings, or ranges.
Examples:

While Loop Example:

python
Copy code
# Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
For Loop Example:

python
Copy code
# Print each character in a string
for char in "Python":
    print(char)

# Print numbers in a range
for num in range(1, 6):
    print(num)
Practice:

Write a program to print all even numbers between 1 and 20 using a for loop.
Write a program that repeatedly asks the user for input using a while loop, stopping only when the user types "exit".
"""

for i in range(1, 21):
    if i%2==0:
        print(i)

while True:
    user_input= input("Your input: ")
    if user_input=="exit":
        break