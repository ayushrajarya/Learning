#4
"""
removing items from a list
assume a list "n"
n.pop(index): removes item at an index (this returns the removed item)
n.remove(item): removes first occurance(lowest index if item is present multiple times) of the item
del(n(index)): removes item at an index (this will not return the item)
del n: this will delete the whole list
"""

list = [1, 2, 3, 4, 5]

# Remove and return the last element from the list
#last_element = list.pop()
#print(last_element)
# Remove the first occurrence of the element 3 from the list
#x=list.remove(3)
#print(x) this will not print anything

# Delete the element at index 2 from the list
del (list[2])

# Print the list
print(list)

#11
n = [3, 5, 7]
def list_extender(lst):
    lst.append(9)
    return lst # return lst.ppend(9) did not work
print(list_extender(n))

#14
"""
range(stop): 0,1,2,3,.....,stop-2, stop-1
range(start,stop): start, start+1, start+2,....., stop-2, stop-1
range(start,stop,step): start, start+1*step, start+ 2*step,...., stop-2*step, stop-1*step
start defaults to 0 and step defaults to 1 unless specified.
"""
def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

print (my_function(range(3)))

#15
"""
Iterating through a list
method 1: iterating through items in list: List modification is not possible
method 2: ierating through the indexes: list can be modified while using indexes
"""
n = [3, 5, 7]

def total(numbers):
    result=0
    for i in numbers:
        result+=i
    return result

#17
m = [1, 2, 3]
n = [4, 5, 6]
"""
Joining two lists as simple as adding them.
Second list will be appended at the end of the first list in the same order
"""
def join_lists(x,y):
    return x+y

print(join_lists(m, n))