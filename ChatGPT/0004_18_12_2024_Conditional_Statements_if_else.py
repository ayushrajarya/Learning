"""
Day 4: Conditional Statements (if-else)
Learn:

Using if, elif, and else for decision-making in Python.
Writing conditional expressions to control program flow.
Examples:

python
Copy code
# Checking if a number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Checking if a user is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
Practice:

Write a program to check if a given year is a leap year.
Write a program to determine if a number entered by the user is even or odd.
"""
year=int(input("Input Year: "))
if year%2==0:
    print(f"Year {year} is Even.")
else:
    print(f"Year {year} is Odd.")
