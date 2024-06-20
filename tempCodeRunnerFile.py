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
prices = {"banana": 4,  "apple": 2,  "orange": 1.5,  
"pear": 3
}
stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
print(stock)
t=compute_bill(["banana","apple","orange", "pear"])
print(t)
print(stock)
shopping_list = ["banana", "orange", "apple"]