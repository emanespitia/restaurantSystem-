import math

# Store everything the user wants a cart
user_cart = []

# Struct of a food item
class MenuItem:
    # 
    def __init__(self, food : str, price : float, discount_perc : float = 0 ):
        self.food = food
        self.price = price
        self.discount_perc = discount_perc
        pass

# Formatting: number, item, price.
menu_items = (MenuItem ( "Pizza", 15.99, ) ),( MenuItem( "Burger", 6.00 ) ), ( MenuItem( "Salad", 15.99 ) ), ( MenuItem( "Pasta", 7.00 ) ), ( MenuItem( "Soda", 2.00 ) )

# This code intends to make a tip calculator which takes a total dollar amount
# and modifies calculates a percentage total based on the user's input.
def calculateTip(total:float, tip:float) -> float:
    #testTotal:float = 11.95 
    userInput = input(f"Would you like to add a tip? Type 1 for yes, any other integer for no: ")
    value = int(userInput)
    
    if(value != 1):
        print("You have chosen to not tip.")
        theTip = 0
    else:
        userInput2 = input("How much would you like to tip?(%): ")
        theTip = int(userInput2)
        tip = theTip/100
        finalPayment:float = (tip+1)*total
        roundedTotal:float = round(finalPayment, 2)  
        print(f"Your chosen tip amount: {theTip}%")  
        print(f"Your final payment with your chosen tip: ${roundedTotal}")    
        return roundedTotal

# Function to determine the discount percentage applied to items based on discount codes. 
# return float between 0-1
def getDiscountPerc( discountCode: str ) -> float:
    # TODO: look through a list of discount codes to determine the percentage
    return 0.0

#Function to track purchases; calls after a purchase is made 
def TrackPurchases(currentCart, purchaseList): # parameters are the current cart and a list of all purchased items, respectively
    for item in currentCart: # Adds all items in the current card into a list of purchases
        purchaseList.append(item)
   
    print("Food bought:") # Prints the tracked purchases
    print("-" * 30)
    for item in purchaseList:
        print(f"{item[1]}")
   
    currentCart.clear() # Clears the current cart 
        
#order summary
def OrderSummary():
    global balance 

    if not user_cart:
        print(f'Your cart is empty. Add Items before checkout')
        return

    print('\n' + '-'*30)
    print("ORDER SUMMARY".center(35))
    print('\n' + '-'*30)

    discount_percentage = 0
    has_discountCode = input(f'Do you have a discount code (yes/no)? ')

    if has_discountCode == 'YES' or 'yes ':
        while True:
            user_discount = input ("Entyer your discount code: ")

            discount_percentage = getDiscountPerc(user_discount)

            if discount_percentage > 0:
                print (f' Disocunt is applied {user_discount} - {discount_percentage}% off')
            else:
                print(f'Invalid Code')
    else:
        print(f'No discount being used')

    total_price = 0
    for item in user_cart:
        # Apply the discount to each item
        item.discount_perc = discount_percentage
        discounted_price = item.price * (1 - item.discount_perc / 100)
        total_spent += discounted_price
        print(f"{item.food:<10} ${discounted_price:.2f}")

    print("-" * 30)
    print(f"Subtotal after discount: ${total_spent:.2f}")

    # Ask for tip amount
    tip_percent = int(input("Enter tip percentage (0-20%): "))
    final_price = calculateTip(total_spent, tip_percent)

    # **Deduct the final price from balance**
    balance -= final_price
    print(f'Remaining Balance {balance}')

    print("Payment is successful!")



   

# Entry function
if __name__ == "__main__":
    # Prompt for name and give a message
    name = input("Please enter your name: ")
    print(f"Welcome to the Online Ordering System, {name}!")
    # How much money do you have?
    balance = input("Please enter your account balance: ")
    print(f"Your balance is: {balance}")
    # TODO: Allow the user to input a discount code
    #discount_code = input( "If you have a discount code, enter it here, otherwise, leave blank:")
    #discount_perc = getDiscountPerc( discount_code )

    # Try again until the user wants to leave
    success = False
    while not success:
        # Generate a list from the food items defined above
        print("Please choose an item from the menu: ")
        print("-" * 30)
        num : int = 0
        menu_options = []
        for num, item in enumerate( menu_items ):
            # add the discount percentage to the item 
            #item.discount_perc = discount_perc
            menu_options.append( item )
            print(f"{num+1}. {item.food:<6} -  Price: ${item.price:.2f}")
        # Display a checkout option on the menu if there's something in the cart
        if ( len(user_cart) > 0 ):
            menu_options.append( "Checkout" )
            print ( f"{len(menu_items)+1}. Checkout")

        print( "-" * 30 )
        answer = input( "What do you want to eat: " )
        # Is this a menu option?
        if not answer.isdigit():
            continue
        # cast to a number
        answer = int( answer )
        # Is this a valid answer within the list?
        if not answer > 0 or not answer < len( menu_options ):
            continue

        # TODO: 
        print( menu_options[-1] )

        success = True




    
