#1
zoo_animals = ["pangolin", "cassowary", "sloth","Hen" ];
# One animal is missing!

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])

  #2
numbers = [5, 6, 7, 8]

print ("Adding the numbers at indices 0 and 2...")
print( numbers[0] + numbers[2])
print( "Adding the numbers at indices 1 and 3...")
# Your code here!
print(numbers[1]+numbers[3])

#3
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"
zoo_animals[3]= "Hen"
# What shall fill the void left by our dear departed tiger?
# Your code here!

#4
suitcase = [] 
suitcase.append("sunglasses")
# Your code here!
suitcase.append("Glass")
suitcase.append("water")
suitcase.append("Laptop")
list_length = len(suitcase) # Set this to the length of suitcase

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)

#5
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4]

# The last two items (index four and five)
last =  suitcase [4:6]

#6
animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:]

#7
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =  animals.index("duck")
animals.insert(duck_index,"cobra")
print (animals) # Observe what prints after the insert operation

#8
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print(2*number)

#9
start_list = [5, 3, 1, 2, 4]
square_list = []

for number in start_list:
    square_list.append(number**2)
square_list.sort()
# sort modifies the list 
print (square_list)

#10
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin'])
print(residents["Sloth"])
print(residents["Burmese Python"])

#11
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])
menu["corn"]=15
menu["butter"]=10
menu["peanuts"]=12
print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)

#12
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
del zoo_animals['Unicorn']
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]
zoo_animals["Rockhopper Penguin"]= "Arctic Exhibit_1"
print (zoo_animals)

#13
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove("dagger")

#14
inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
inventory['pouch'].sort() 
inventory["pocket"]= ["seashell", "strange berry", "lint"]
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"]+=50