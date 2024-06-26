#2
def is_even(n):
    return True if (n%2==0) else False
"""
if else in return example above 
return something if condition1 else something_else
"""

#3
def is_int(x):
    return True if x%1==0 else False
"""
Finding out if a number is integer
"""
#3 Part 2
def is_int(x):
    print(x%1)
    return True if x%1==0 else ("Negative" if x<0 else ("Positive" if x>0 and x<1 else "Greater than 1"))
print(is_int(2.3))
"""
In return statement elif won't work and for a better code readability thou shall not write too much in one line
But iit an still be done as shown above.
First check one if condition
then in else within parenthesis write another if condition
In this way if can be nested infinite times in the else of the preceeding condition  
"""

#4
def digit_sum(x):
    s=0
    for c in str(x):
        s+=int(c)
    return s
#4 way 2
def digit_sum(x):
    s=0
    while (x//10>0):
        s+=x%10
        x=x//10
    s+=x%10
    return s

#5
def factorial(x):
    f=1
    for i in range(x):
        f*=(i+1)
    return f

#6
def is_prime(x):
    if x<2:
        return False
    for i in range(2,x-1):
        if x%i==0:
            return False
    else:
        return True

print(is_prime(1))

#7
def reverse(text):
    s=""
    for c in text:
        s=c+s
    return s

print(reverse("sdhvbwd"))

#8
def anti_vowel(text):
    s=""
    for c in text:
        if c.upper() not in ["A","E","I","O","U"]:
            s+=c
    return s
print(anti_vowel("gvCYTCWTUVA usvqcu Tcxuq x "))

#9
def scrabble_score(word):
    curr_score=0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    for c in word:
        curr_score+=score[c.lower()]
    return curr_score 

print(scrabble_score("helix"))

#10
def censor(text, word):
    ast_len= len(word)
    text_list= text.split()
    for i, curr_word in enumerate(text_list):
        if curr_word== word:
            text_list[i]= "*" * ast_len
    return " ".join(text_list)

print(censor("something we all do but never say that we do.", "do"))

#11
def count(sequence, item):
    curr_count=0
    for i in sequence:
        if i==item:
            curr_count+=1
    return curr_count

print(count([1, 2, 1, 1], 1))

#12
def purify(numbers):
    final_list=[]
    for num in numbers:
        if num%2 == 0:
            final_list.append(num)
    return final_list
print(purify([1651,651,6165,1651,65,165,1,65,2,19,16,3,46,54,613,8]))

#13
def product(numbers):
    prod=1
    for i in numbers:
        prod*=i
    return prod
print(product([1,2,3,4,5,6]))

#14
def remove_duplicates(numbers):
    new_list=[]
    for i in numbers:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(remove_duplicates([1,2,1,2,1,5,1,4,5,89,6,5,1,25,8,6,7,8,6,54,7,5,5,3,2,5,6,8]))

#15
def median(numbers):
    numbers.sort() # this works
    # numbers = numbers.sort() does not work
    """
    numbers=sorted(numbers)   This also works
    """
    length=len(numbers)
    return numbers[length//2] if length%2 !=0 else (numbers[length//2]+numbers[length//2-1])/2.0

print(median([1,2]))