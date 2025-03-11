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

    
