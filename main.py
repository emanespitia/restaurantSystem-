import math


# This code indends to make a tip calculator which takes a total dollar amount
# and modifies calculates a percentage total based on the user's input.
 
testTotal:float = 11.95
testTip:int = 20
 
def calculateTip(total:float, percentTip:int) -> float:
    tip = percentTip/100
    finalPayment = (tip+1)*total
    print(f"Your chosen tip amount: {percentTip}%")
    roundedTotal:float = round(finalPayment, 2)
    print(f"Your final payment: ${roundedTotal}")
 
calculateTip(testTotal, testTip)




name = input("Please enter your name: ")
print(f"Welcome to the Online Ordering System {name}!")

balance = input("please enter your account balane: ")

menu_items = (1, "Pizza", 15.99), (2, "Burger", 6.0), (3, "Salad", 5.0),(4, "Pasta", 7.0), (5, "Soda", 2.0)

print(f"Your balance is: {balance}")
print("Please choose an item from the menu: ")
print("-" * 30)
for number, item, price in menu_items:
    print(f"{number}. {item:<6} Price: ${price}")
print("-" * 30)

    
