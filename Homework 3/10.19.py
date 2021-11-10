#JAKE BILLARD | UHID 1582534

class ItemToPurchase:
    def __init__(self, it_name = "none", it_price = 0, it_quantity = 0, it_description = "none"): #starts variables at 0 default values
        self.it_name = it_name
        self.it_price = it_price
        self.it_quantity = it_quantity
        self.it_description = it_description

    def print_item_cost(self):
        total_output = "{} {} @ ${} = ${}".format(self.it_name, self.it_quantity, self.it_price,
                                            (self.it_price * self.it_quantity))
        total_price = self.it_price * self.it_quantity
        return total_output, total_price

    def print_item_descriptions(self):
        format_str = '{}: {}'.format(self.it_name, self.it_description)   #prints item name and description into "it_desc"
        print(format_str, end='\n')
        return format_str

 # ShoppingCart
class ShoppingCart:
    def __init__(self, cust_name = "none", todays_date = "January 1, 2016", items_in_cart=[]):
        self.cust_name = cust_name              #customer name
        self.todays_date = todays_date          #todays date
        self.items_in_cart = items_in_cart      #items currently in the cart (list)

    #Add Items (a)
    def add_item(self, format_str):
        print("\nADD ITEM TO CART")
        it_name = str(input("Enter the item name:"))
        it_description = str(input("\nEnter the item description:"))
        it_price = int(input("\nEnter the item price:"))
        it_quantity = int(input("\nEnter the item quantity:\n"))
        self.items_in_cart.append(ItemToPurchase(it_name, it_price, it_quantity, it_description))  #Adds each variable to the cart

    #Remove Items (r)
    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        format_str = str(input("Enter name of item to remove:"))

        for format_str in self.items_in_cart:
            if (format_str.it_name == format_str):
                del self.items_in_cart[format_str]   # Deletes Item if the name is in the list
            elif (format_str.it_name != format_str):
                print("\nItem not found in cart. Nothing removed.")
            else:
                pass

    #Modify Item Quantity (c)
    def modify_item(self):
        print("\nCHANGE ITEM QUANTITY")
        #***
        for item in self.items_in_cart:
            item_name_m = str(input("\nEnter the item name: "))
            if (item.it_name == item_name_m):
                quantity = int(input("\nEnter the new quantity: "))      #***       #If item is in the cart, it allows user to modify quantity
                item.it_quantity = quantity
                it_finder = True        #Correct inpu
                break
            else:
                it_finder = False       #Incorrect input
        if (it_finder == False):        #If Item is not in cart. Doesn't do anything.
            print("Item not found in cart. Nothing modified")

    #Count number of itmes in the cart
    def get_num_items_in_cart(self):
        cart_item_quantity = 0      #defaults cart number to 0
        for item in self.items_in_cart:
            cart_item_quantity = cart_item_quantity + item.it_quantity
        return cart_item_quantity

    #Total Cost of Cart Items Selected
    def get_cost_of_cart(self):
        total_price = 0     #defaults total price to 0
        cost = 0            #defaults cost to 0
        for item in self.items_in_cart:
            cost = (item.it_quantity * item.it_price)
            total_price += cost
        return total_price

    #Prints Cart Total Price
    def print_total(self):
        total_price = self.get_cost_of_cart()
        if (total_price == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            self.output_cart()

    #Prints item Description (i)
    def print_it_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.cust_name, self.todays_date))
        print("\nItem Descriptions")
        for item in self.items_in_cart:
            print("{}: {}".format(item.it_name, item.it_description), end='\n')

    #Outputs the Cart (o)
    def output_cart(self):
        new = ShoppingCart()
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.cust_name, self.todays_date))
        print("Number of Items:", new.get_num_items_in_cart(), end='\n\n')
        if new.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            pass
        default_oc = 0
        for item in self.items_in_cart:
            print("{} {} @ ${} = ${}".format(item.it_name, item.it_quantity,
                                             item.it_price, (item.it_quantity * item.it_price)), end='\n') # Puts the name, quantity, price, and total into the spaces
            default_oc += (item.it_quantity * item.it_price)
        print("\nTotal: ${}".format(default_oc), end='\n')

def print_menu(ShoppingCart):
    customer_Cart = newCart
    format_str = ''
    user_menu = ("\nMENU"
            "\na - Add item to cart"
            "\nr - Remove item from cart"
            "\nc - Change item quantity"
            "\ni - Output items' descriptions"
            "\no - Output shopping cart"
            "\nq - Quit\n")

    user_choice = ''
    while (user_choice != 'q'):
        format_str = ''
        print(user_menu)
        user_choice = input("Choose an option:\n")
        while (user_choice != 'a' and user_choice != 'o' and user_choice != 'i' and user_choice != 'r'
               and user_choice != 'c' and user_choice != 'q'):
            user_choice = input("Choose an option:\n")
        if (user_choice == 'a'):
            customer_Cart.add_item(format_str)
        if (user_choice == 'o'):
            customer_Cart.output_cart()
        if (user_choice == 'i'):
            customer_Cart.print_it_descriptions()
        if (user_choice == 'r'):
            customer_Cart.remove_item()
        if (user_choice == 'c'):
            customer_Cart.modify_item()

cust_name = str(input("Enter customer's name:"))
todays_date = str(input("\nEnter today's date:"))
print()

print("\nCustomer name:", cust_name, end='\n')
print("Today's date:", todays_date, end='\n')

newCart = ShoppingCart(cust_name, todays_date)
print_menu(newCart)
