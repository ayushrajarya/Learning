#1
def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

#4
"""
def some_funtion(x,y,z):
    here x,y,z are parameters and values that are fed in the funtion for them are called arguments.
"""
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print ("%d to the power of %d is %d." % (base, exponent, result))

power(37, 4)  # Add your arguments here!

#6
def cube(number):
    return number**3

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
    
#9
from math import sqrt
# from module import function
print(sqrt(25))
"""
if you import a function directly then there is no need to write module.function again and again.
Otherwise we would have to write math.sqrt(25) just now to achieve the same thing.
"""

#10
# to import everything and not wanting to write the funtion name again and again then do universal import
# from module import *
from math import *
"""
This may look good but when there are many modules in a program then tracking each function and variable name is a hassle
The conflict may arrise if two functions or variables have same name and one of them is being imported from a module
This may result in unexpecte result from the script.
So, it is beter to import the module and then call with module.
Over that it fills your program with a ton of variable and functions.
"""

#11
import math
everything = dir(math)
print(everything)
"""
This will give everything available in the module.
import module
print(dir(module))
"""

#13
"""
maximum = max(02024,12,6,6,45,6,65,6,5,66,6,5)
print (maximum)
This throws an error saying leading zeros not allowed look into this more
"""

#16
k=1.2
print(type(k))

#17
def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

#19
def distance_from_zero(x):
    if type(x)==int or type(x)==float:
        return abs(x)
    else:
        return "Nope"
print(distance_from_zero('20.4'))










