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
menu_items = (MenuItem( "Pizza", 15.99 ) ), ( MenuItem( "Burger", 6.00 ) ), ( MenuItem( "Salad", 15.99 ) ), ( MenuItem( "Pasta", 7.00 ) ), ( MenuItem( "Soda", 2.00 ) )

# This code indends to make a tip calculator which takes a total dollar amount
# and modifies calculates a percentage total based on the user's input.
def calculateTip( total: float, percentTip: int ) -> float:
    # get a tip value based on the percentage provided
    tip = percentTip / 100
    # Calculate the final payment based on the tip
    finalPayment = ( tip+1 ) * total

    print(f"Your chosen tip amount: {percentTip}%")
    roundedTotal:float = round(finalPayment, 2)
    print(f"Your final payment: ${roundedTotal}")

# Function to determine the discount percentage applied to items based on discount codes. 
# return float between 0-1
def getDiscountPerc( discountCode: str ) -> float:
    # TODO: look through a list of discount codes to determine the percentage
    return 0.0

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


    
