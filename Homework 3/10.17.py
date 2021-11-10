# JAKE BILLARD | UHID 1582534

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none" #starts item_name with "none"
        self.item_price = 0     #starts item_price at 0
        self.item_quantity = 0  #starts item_quantity at 0

    def print_item_cost(self):
        print(str(self.item_name), str(self.item_quantity), "@ $" + str(self.item_price), "= $" + str(self.item_price*self.item_quantity))  # Print Name, Quantity, Price, and Total of Item.

if __name__ == "__main__":          #main

    item_1 = ItemToPurchase()       #Calls Item_1 to class

    print("Item 1")
    item_1.item_name = input("Enter the item name:")
    item_1.item_price = int(input("\nEnter the item price:"))
    item_1.item_quantity = int(input("\nEnter the item quantity:"))
    print()
    print()

    item_2 = ItemToPurchase()       #Calls Item_2 to class

    print("Item 2")
    item_2.item_name = input("Enter the item name:")
    item_2.item_price = int(input("\nEnter the item price:"))
    item_2.item_quantity = int(input("\nEnter the item quantity:"))
    print()
    print("\nTOTAL COST")
    item_1.print_item_cost()     # Connecting item_1 to print_item_cost
    item_2.print_item_cost()     # Connecting item_2 to print_item_cost

    #Total
    total_price = ((item_1.item_price * item_1.item_quantity)+(item_2.item_price * item_2.item_quantity))
    print( "\nTotal: $",(total_price), sep='')
