#1
print (5 >> 2 ) # Right Shift
print (5 << 1 ) # Left Shift
print (8 & 5   )# Bitwise AND
print (9 | 4   )# Bitwise OR
print (12 ^ 42) # Bitwise XOR
print (~88)     # Bitwise NOT

#2
print(0b01)    #1
print (0b10)   #2
print (0b11)  #3
print (0b100)  #4
print (0b101)  #5
print (0b110)  #6
print (0b111)   #7
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)

#3
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

#4
print(bin(4))       # 0b100
print(type(bin(4))) # string class
print(bin(4)[2:])   # 100
"""
bin function returns the value as string
"""
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

#5
print(int("1",2))
print(int("0b110",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("0b11001001",2))

