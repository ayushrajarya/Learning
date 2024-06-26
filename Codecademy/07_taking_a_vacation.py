#1
def answer():
    return 42

#2
def hotel_cost(nights):
    return 140*nights

#3
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city== "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

#4
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city== "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost=40*days
    if days>= 7:
        cost-=50
    elif days>=3:
        cost-=20
    return cost

#5
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city== "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost=40*days
    if days>= 7:
        cost-=50
    elif days>=3:
        cost-=20
    return cost

def trip_cost(city, days):
    return rental_car_cost(days)+hotel_cost(days-1)+plane_ride_cost(city)

print(trip_cost("Los Angeles", 6))

#6
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city== "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost=40*days
    if days>= 7:
        cost-=50
    elif days>=3:
        cost-=20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days-1)+plane_ride_cost(city)+spending_money

#7
def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city== "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    
def rental_car_cost(days):
    cost=40*days
    if days>= 7:
        cost-=50
    elif days>=3:
        cost-=20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days-1)+plane_ride_cost(city)+spending_money

print(trip_cost("Los Angeles", 5, 600))


