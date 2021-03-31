# Jake Billard UHID 1582534


# Create Class ItemToPurchasew with default constructors
class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


    # PRINT ITEM COST
    def print_item_cost(self):
        pic_output = "{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price,   # Inserts name, quantity, price, and total to the spaces.
                                            (self.item_price * self.item_quantity))
        cost_total = self.item_price * self.item_quantity
        return pic_output, cost_total

    # PRINT ITEM DESCRIPTION
    def print_item_description(self):
        string = '{}: {}'.format(self.item_name, self.item_description)   # prints name and item description in the spaces
        print(string, end='\n')
        return string


# Introduces Shopping Cart class with the default constructor to start it off
class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items


    ###   ADD ITEM  - a  ###
    def add_item(self, string):
        print("\nADD ITEM TO CART")
        item_name = str(input("Enter the item name:"))
        item_description = str(input("\nEnter the item description:"))
        item_price = int(input("\nEnter the item price:"))
        item_quantity = int(input("\nEnter the item quantity:\n"))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))  #Adds each variable to the cart
    ###   ADD ITEM   ###


    ###   REMOVE ITEM - r  ###
    def remove_item(self):
        print("REMOVE ITEM FROM CART")
        string = str(input("Enter name of item to remove:"))
        x = 0

        for item in self.cart_items:
            if (item.item_name == string):
                del self.cart_items[x]   # Deletes Item if the name is in the list
            elif (item.item_name !=string):
                print("\nItem not found in cart. Nothing removed.")
            else:
                pass
    ###   REMOVE ITEM   ###


    ###   CHANGE ITEM QUANTITY - c  ###
    def modify_item(self):
        print("\nCHANGE ITEM QUANTITY")
        name = str(input("\nEnter the item name: "))
        for item in self.cart_items:
            if (item.item_name == name):
                quantity = int(input("\nEnter the new quantity: "))
                item.item_quantity = quantity   # Modifies item Quantity if the item name is in the list
                flag = True # Correct input
                break
            else:
                flag = False # Incorrect input
        if (flag == False):
            print("Item not found in cart. Nothing modified")
    ###    CHANGE ITEM QUANTITY   ###


    #####     COUNT NUMBER OF ITEMS IN CART     #####
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items
            #**
    #####     COUNT NUMBER OF ITEMS IN CART     #####


    ###   TOTAL COST OF CART   ###
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost
    ###   TOTAL COST OF CART   ###


    ###   PRINT TOTAL   ###
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if (total_cost == 0):
            print("SHOPPING CART IS EMPTY")
        else:
            self.output_cart()
    ###   PRINT TOTAL   ###


    ###   PRINT ITEM DESCRIPTION - i   ###
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("\nItem Descriptions")
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description), end='\n')
    ###   PRINT ITEM DESCRIPTION   ###


    ###   OUTPUT SHOPPING CART - o  ###
    def output_cart(self):
        new = ShoppingCart()

        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items:", new.get_num_items_in_cart(), end='\n\n')

        if new.get_num_items_in_cart() == "0":
            print("SHOPPING CART IS EMPTY")
        else:
            pass

        octe = 0
        for item in self.cart_items:
            print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity,
                                             item.item_price, (item.item_quantity * item.item_price)), end='\n') # Puts the name, quantity, price, and total into the spaces
            octe += (item.item_quantity * item.item_price)
        print("\nTotal: ${}".format(octe), end='\n')
    ###   OUTPUT SHOPPING CART   ###


def print_menu(ShoppingCart):
    customer_Cart = newCart
    string = ''

    menu = ("\nMENU"
            "\na - Add item to cart"
            "\nr - Remove item from cart"
            "\nc - Change item quantity"
            "\ni - Output items' descriptions"
            "\no - Output shopping cart"
            "\nq - Quit\n")


    user_option = ''
    while (user_option != 'q'):
        string = ''
        print(menu)
        user_option = input("Choose an option:\n")
        while (user_option != 'a' and user_option != 'o' and user_option != 'i' and user_option != 'r'
               and user_option != 'c' and user_option != 'q'):
            user_option = input("Choose an option:\n")
        if (user_option == 'a'):
            customer_Cart.add_item(string)
        if (user_option == 'o'):
            customer_Cart.output_cart()
        if (user_option == 'i'):
            customer_Cart.print_descriptions()
        if (user_option == 'r'):
            customer_Cart.remove_item()
        if (user_option == 'c'):
            customer_Cart.modify_item()


customer_name = str(input("Enter customer's name:"))
current_date = str(input("\nEnter today's date:"))
print()


print("\nCustomer name:", customer_name, end='\n')
print("Today's date:", current_date, end='\n')


newCart = ShoppingCart(customer_name, current_date)
print_menu(newCart)