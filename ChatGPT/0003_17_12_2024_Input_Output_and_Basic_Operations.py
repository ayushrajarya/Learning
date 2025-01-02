"""
Day 3: Input, Output, and Basic Operations
Learn:

Taking input from the user using input().
Displaying output with print().
Performing basic operations: addition, subtraction, multiplication, division, and modulus.
Examples:

python
Copy code
# Taking input from the user
name = input("What is your name? ")
print(f"Hello, {name}!")

# Performing basic math operations
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")
Practice:

Write a program to take the user's birth year as input and calculate their age.
Write a program to take two numbers as input and print their sum, difference, product, and quotient.
"""
from datetime import datetime
num1= int(input("Num 1: "))
num2= int(input("Num 2: "))

print(f"Sum: {num1+num2}")
print(f"Subtraction: {num1-num2}")
print(f"Product: {num1*num2}")
print(f"Division: {num1/num2}")

birth_year= int(input("Birth Year: "))
print(f"Your age approximately: {datetime.now().year - birth_year}")