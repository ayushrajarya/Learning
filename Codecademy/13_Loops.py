#7
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

guesses_left = 3
# Start your game!
while guesses_left>0:
    guess=int(input("Your guess: "))
    if guess==random_number:
        print("You win!")
        break
    guesses_left-=1
else:
    print("You lose.")

#12
phrase = "A bird in the hand..."
for char in phrase:
    if char =="A" or char == "a":
        print("X", end="")
    else:
        print(char, end="")
"""
to stay in the same line to print next thing in the same line add end in the print statement.
print("<whatever intended to be printed>", end="")
this end can have any other string also which can be used for concatenation.
"""

#14
"""
While iterating through a dictionary the key is picked.
And the key can be used to get the value
"""

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  # Your code here!
  print("%s %s" % (key, d[key]))
  
#15
choices = ['pizza', 'pasta', 'salad', 'nachos', "pizza"]

print( 'Your choices are:')
for index, item in enumerate(choices):
  print (index+1, item)
"""
Enumerate gives index and item pair that is index of the corresponding element which was picked.
This way evey if there are multiple duplicates it will give the exact index of the item which is picked in that iteration.
"""

#16
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
list_c= [561,651,651,65,1651,65,165,1651,61,8,654]
for ind,( a, b,c) in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(a,b,c))
  print(ind)
print("avssssssssssss")
for ind,t in enumerate(zip(list_a, list_b, list_c)):
  # Add your code here!
  print(max(t))
  print(ind)
  print(type(t))
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

#17
"""
Just like while/else, for/else can also be made
else condition is ony executed when for ends normally and through a break statement.
"""
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print( 'You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')