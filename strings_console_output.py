"""
String methods
len(x)
x.lower()
x.upper()
str(x)
"""
"""
methods that use dot notation only work with strings
on the other hand, len() and str() can work on other data types
"""

string_1 = "Camelot"
string_2 = 2256

print ("Let's not go to %s. 'Tis a silly %02d." % (string_1, string_2))
print ("Let's not go to %s. 'Tis a silly %015d." % (string_1, string_2))
print ("Let's not go to %s. 'Tis a silly d%6d." % (string_1, string_2)) 
# 4 places are skipped rest are printed as space
"""
padding in integer can be done with % formatting like above.
Only 0 can be added for padding, next write how many characters are needed.
d represents that it is an integer.
if number of digits in integer is more than the input in padding then whole variable is printed.
It will not remove any digits.
"""