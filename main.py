import math

# Struct of a food item
class MenuItem:
    # 
    def __init__(self, food : str, price : float, discount_perc : float = 0, allergens : list = [] ):
        self.food = food
        self.price = price
        self.discount_perc = discount_perc
        self.allergens = allergens
        pass

    # Function to get the price of the item, with discount applied if applicable
    def getPrice( self ):
        # Get a discounted price if this item has it
        if self.discount_perc != 0:
            return round( self.getBasePrice() * ( 1 - self.discount_perc ), 2 ) 
        
        # Give me a normal price
        return self.getBasePrice()
    
    # Get the base price without modification
    def getBasePrice( self ):
        return round( self.price, 2 )

# Store everything the user wants a cart
user_cart = []

# List of common allergens
item_allergens = ["milk", "eggs", "nuts", "fish", "wheat", "soy", "sesame", "shellfish"]

# Formatting: number, item, price.
menu_items = (
( MenuItem ( "Pizza", 15.99, 0, ["wheat", "milk"] ) ),
( MenuItem( "Burger", 6.00, 0, ["wheat", "sesame"] ) ), 
( MenuItem( "Salad", 15.99, 0, [] ) ), 
( MenuItem( "Pasta", 7.00, 0, ["milk", "wheat"] ) ), 
( MenuItem( "Soda", 2.00, 0, [] ) ), 
( "Checkout" )
)

# User's name
name : str = "" 
# User's balance, formatted by 2 precision points
balance : float = 0.00

# This code intends to make a tip calculator which takes a total dollar amount
# and modifies calculates a percentage total based on the user's input.
def calculateTip(total : float, tip : float) -> float:
    if tip > 0:
        finalPayment : float = (tip+1)*total
        roundedTotal : float = round(finalPayment, 2)  
        print(f"Your chosen tip amount: {int( tip*100 )}%")  
        print(f"Your final payment with your chosen tip: ${roundedTotal:.2f}.")
        return roundedTotal
    else:
        print( f"No tip was applied. Your final payment is ${total:.2f}.")
        return total

# Function to determine the discount percentage applied to items based on discount codes. 
# return integer between 0-99
def getDiscountPerc( discountCode: str ) -> int:
    # TODO: look through a list of discount codes to determine the percentage
    return 0

#Function to track purchases; calls after a purchase is made 
def TrackPurchases(currentCart, purchaseList): # parameters are the current cart and a list of all purchased items, respectively
    for item in currentCart: # Adds all items in the current card into a list of purchases
        purchaseList.append(item)
   
    print("Food bought:") # Prints the tracked purchases
    print("-" * 30)
    for item in purchaseList:
        print(f"{item[1]}")
   
    currentCart.clear() # Clears the current cart 
    
# changes may need to be made to this function based on implementation of allergies
def addItemToOrder( menu_selection : MenuItem, user_allergens : list ) -> bool:
    # checks allergens
    if user_allergens:
        if any(a in menu_selection.allergens for a in user_allergens):
            user_confirmation = input(f"Warning: {menu_selection.food} contains {', '.join(menu_selection.allergens)} which you have listed as an allergy for your account. Do you still want to order it? (Y/N): ")
            if user_confirmation[0].lower() != "y":
                print("Item not added to the cart.")
                # return with no changes to cart if not YES to continue
                return False
    
    # make changes to cart and return
    user_cart.append(menu_selection) # adds integer corresponging to menu item 
    return True

# order summary
def OrderSummary():
    global balance
    
    # Check if the cart is empty
    if not user_cart:
        print(f'Your cart is empty. Add items before checking out.')
        return

    discount_percentage = 0
    has_discountCode = input(f'Do you have a discount code (Y/N)? ')
    if has_discountCode[0].lower() == 'y':
        while True:
            user_discount = input ("Enter your discount code (Write \"N\" if you don't have one): ")
            discount_percentage = getDiscountPerc(user_discount)
            if discount_percentage > 0:
                # Convert into an integer
                print(f' Discount is applied {user_discount} - {discount_percentage * 100}% off')
                break
            elif user_discount[0].lower() == "n":
                print( "User didn't have a discount code. Continuing.")
                break
            else:
                print(f'Invalid Code')
    else:
        print(f'No discount being used.')

    print('\n' + '-' * 30)
    print("ORDER SUMMARY".center(35))
    for item in user_cart:
        print( f"{item.food} - {item.price:.2f}".center(35) )
    print('\n' + '-'*30)

    # Expect a menu item
    total_spent : float = 0.0
    item : MenuItem
    for item in user_cart:
        # Apply the discount to each item
        item.discount_perc = discount_percentage
        # Get the price from the item, it could be different due to a discount.
        total_spent += item.getPrice()
        print(f"{item.food:<10} ${item.getPrice():.2f}")

    print("-" * 30)
    print(f"Subtotal after discount: ${total_spent:.2f}")

    # Ask for tip amount
    tip_percent = int( input("Enter tip percentage (0-20%): ") )
    
    # Clamp the number between 0 and 20
    if tip_percent < 0:
        tip_percent = 0
    if tip_percent > 20:
        tip_percent = 20
    
    # Convert to float
    tip_percent /= 100

    # Calculate the tip
    final_price = calculateTip(total_spent, tip_percent)

    # **Deduct the final price from balance**
    balance -= final_price
    print(f'Remaining Balance {balance}')
    print("Payment is successful!")

# Function to display the menu with a prompt for a suggestion
# question: What question will be displayed from this
# options: What are the options you want the user to select from; tuple of MenuItems + one string option
# returns the string answer of the selected question
def displayMenuWithSelection( question : str, options: tuple ) -> str:
    # Is this list empty?
    if not options:
        return

    # Check if the user puts in a valid option.
    # If not, keep prompting the user with it
    success = False
    answer = 0
    # Keep prompting the user until a valid selection has been made
    while not success:
        # Print the list
        print("-" * 30)
        for idx, option in enumerate(options):
            # Check if what we're printing is a menu item
            if type(option) == MenuItem:
                print(f"{idx+1}. {option.food:<6} -  Price: ${option.price:.2f}")
            # Only print this if you have things in your cart
            elif option == "Checkout":
                if user_cart:
                    print( f"{idx+1}. {option}" )
        print("-" * 30)

        # prompt for a number
        answer = input( question )
        
        # Is this a number?
        if not answer.isdigit():
            continue
        
        # cast to a number
        answer = int( answer )

        # Is this choice within the range of the list?
        if answer <= 0 or answer > len( options ):
            continue
        
        # Okay, this is a valid selection, get out of here
        success = True

    # off by one, correct it
    # Check if this is a menu item or generic selection
    return options[answer-1]

# Entry function
if __name__ == "__main__":
    # Prompt for name and give a message
    name = input("Please enter your name: ")
    print(f"Welcome to the Online Ordering System, {name}!")

    # How much money do you have?
    balance : float = float( input( "Please enter your account balance: ") )
    print( f"Your balance is: ${balance:.2f}") 
    
    # Compile a list of allergies based on what the user said
    user_allergy_list = []

    # Print all possible options
    print ( f"Potential options: {item_allergens}" )

    # prompt the user for allergies, separated by spaces
    allergies = input( "Enter allergies, separated by spaces (e.g. milk nuts eggs). Press Enter if you have no allergies.\n")

    # if the user entered something, add a terminator char for later
    if allergies:
        # Search thru the list, and add it to an allergen list so that we can use it for item adding
        allergies += "_"
        temp_string = ""
        for char in allergies:
            if char.isspace() or char == "_":
                user_allergy_list.append( temp_string )
                temp_string = ""
            else:
                temp_string += char
    
    while True:
        # Make a selection. Return a food item.
        selection = displayMenuWithSelection( "Select your options ", menu_items )

        # If the user wants to checkout, you  
        if selection == "Checkout":
            OrderSummary()
        else:
            if addItemToOrder( selection, user_allergy_list ):
                print( f"You have selected: {selection.food} Adding to cart." )
    