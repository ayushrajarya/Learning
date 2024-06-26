#1
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
    print(name)

#2
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}
for k in webster:
    print(webster[k])

#3
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in a:
    if i%2==0:
        print(i)

#4
def fizz_count(x):
    count=0
    for item in x:
        if item== "fizz":
            count+=1
    return count

#9
prices={}
# a dictionary has to initialized before assigning any value
""" Below will work though as kay and value pair is given while initialising
prices={"banana":4, "apple":2, "orange": 1}
print(prices)

Below will not work without initialising en empty ditionary
prices["banana"]=4
prices["apple"]=2
print(prices)
"""
prices["banana"]=4
prices["apple"]=2
prices["orange"]=1.5
prices["pear"]=3

stock={}
stock["banana"]=6
stock["apple"]=0
stock["orange"]=32
stock["pear"]=15
total =0
for k in prices:
    print(k)
    print("price: %s" % str(prices[k]))
    print("stock: %s" % str(stock[k]))

for k in prices:
    print(prices[k]*stock[k])
    total+= prices[k]*stock[k]
print(total)

#11
"""
A variable initalised in the main code and called in the function will work just fine.
If any change is done in a funtion to that variable then the main variable will be chnaged.
"""
def compute_bill(food):
    total=0
    for f in food:
        if stock[f]>0:
            total+= prices[f]
            stock[f]-=1
    return total
prices = {"banana": 4,  "apple": 2,  "orange": 1.5,"pear": 3}
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
print(stock)
t=compute_bill(["banana","apple","orange", "pear"])
print(t)
print(stock)
shopping_list = ["banana", "orange", "apple"]
