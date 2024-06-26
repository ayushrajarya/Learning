my_name = "Ayush Arya"
print("Hello and welcome "+ my_name + " !")
#this is a comment
"""
this is also a comment
this way you can write multi line comments
print("see nothing got printed")
"""
print("this \nis printed in next \"line\" with quotes and a \\ backlash")

january_to_june_rainfall = 1.93 + 0.71 + 3.53 + 3.41 + 3.69 + 4.50
annual_rainfall = january_to_june_rainfall

july_rainfall = 1.05
annual_rainfall += july_rainfall

august_rainfall = 4.91
annual_rainfall += august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall+= september_rainfall + october_rainfall + november_rainfall + december_rainfall
# this works fine

# multi-line string in a variable
haiku= """The old pond,
A frog jumps in:
Plop!"""

age=13
age = str(age)
print(type(age))

marks= '79'
marks= int(marks)
print(type(marks))
# similarlly, int, str, float
fl='-3.5'
fl=float(fl)
# this will throw error "ValueError: invalid literal for int()" as string is not an integer
# fl='-2.6'
# fl= int(fl)
print(fl)
print(type(fl))

fl=int(fl)
#this works as this converts float to int removing decimal part
print(fl)
print(type(fl))