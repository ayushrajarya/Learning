#2
print("Pig Latin")

#3
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")

#4
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")
if len(original)>0:
    print(original)
else:
    print("empty")

#5
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")
if len(original)>0 and original.isalpha():
    print(original)
else:
    print("empty")

#6
print ('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word: ")
if len(original)>0 and original.isalpha():
    print(original)
elif len(original)>0 and not original.isalpha():
    print("not Alpha")
else:
    print("empty")

#final
pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
  print (original)
  word=original.lower()
  first=word[0]
  new_word=word+first+pyg
  new_word=new_word[1:]
  print(new_word)  
else:
  print ('empty')














