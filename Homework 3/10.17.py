#   Jake Billard   UHID 1582534

class ItemToPurchase:
    def __init__(self):   # Default Constructor with starter values.
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):   # Print Name, Quantity, Price, and Total of Item.
        print(str(self.item_name), str(self.item_quantity), "@ $" + str(self.item_price), "= $" + str(self.item_price*self.item_quantity))

if __name__ == "__main__":

    # Calling the class.
    item_1 = ItemToPurchase()
    item_2 = ItemToPurchase()

    ###   ITEM 1 INPUTS   ###
    print("Item 1")
    item_1.item_name = input("Enter the item name:")
    item_1.item_price = int(input("\nEnter the item price:"))
    item_1.item_quantity = int(input("\nEnter the item quantity:"))
    ###   ITEM 1 INPUTS   ###

    print()
    print()

    ###   ITEM 2 INPUTS   ###
    print("Item 2")
    item_2.item_name = input("Enter the item name:")
    item_2.item_price = int(input("\nEnter the item price:"))
    item_2.item_quantity = int(input("\nEnter the item quantity:"))
    ###   ITEM 2 INPUTS   ###

    print()

    # Connecting Item_1 and Item_2 to print_item_cost
    print("\nTOTAL COST")
    item_1.print_item_cost()
    item_2.print_item_cost()

    # Grand Total
    item_total = ((item_1.item_price * item_1.item_quantity)+(item_2.item_price * item_2.item_quantity))

    print( "\nTotal: $",(item_total), sep='')
