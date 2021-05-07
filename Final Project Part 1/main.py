#       Jake Billard        UHID 1582534
#       Final Project       Part 1

import csv
from datetime import datetime

class Complete_Inventory_Output:

    def __init__(self, Item_LIST):
        self.Item_LIST = Item_LIST


#------------------------ FULL INVENTORY ------------------#

    def Full_Inv(self):

        with open('FullInventory.csv', 'w') as FI_newfile:
            Items = self.Item_LIST  #Connects Full_Inv "Items" to __init__
            Item_KEY = sorted(Items.keys(), key=lambda n: Items[n]["Manufacturer_NAME"])     #Sorts Items by Manufacturer.
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
                FI_newfile.write('{},{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ FULL INVENTORY ------------------#



# ------------------------ TYPE ORGANIZATION ---------------#

    def Type_Org(self):

        Items = self.Item_LIST      #Connects Type_Org "Items" to __init__
        itemtypes = []
        Item_KEY = sorted(Items.keys())
        for item in Items:
            Item_TYPE = Items[item]["Item_TYPE"]
            if Item_TYPE not in itemtypes:
                itemtypes.append(Item_TYPE)     #If Item_TYPE is not in the itemtypes list, it will be appended.
        for type in itemtypes:
            file_name = type.capitalize() + 'Inventory.csv'     #Creates the File with it's respective name.
            with open(file_name, 'w') as TO_newfile:
                for item in Item_KEY:
                    ID = item
                    Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                    Item_PRICE = Items[item]["Item_PRICE"]
                    ServiceDate = Items[item]["ServiceDate"]
                    Item_DAMAGED = Items[item]["Item_DAMAGED"]
                    Item_TYPE = Items[item]["Item_TYPE"]
                    if type == Item_TYPE:
                        TO_newfile.write('{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ TYPE ORGANIZATION ---------------#



# ------------------------ PAST SERVICE DATE ---------------#

    def Past_Service_Date(self):

        Items = self.Item_LIST      #Connects Past_Service_Date "Items" to __init__
        Item_KEY = sorted(Items.keys(), key=lambda n: datetime.strptime(Items[n]["ServiceDate"], "%m/%d/%Y").date(), reverse=True)  #Dates sorted from Oldest to Newest.
        with open('PastServiceDateInventory.csv', 'w') as PSD_newfile:      #Creates PastServiceDateInventory.csv
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
                date_TODAY = datetime.now().date()
                date_EXPIRATION = datetime.strptime(ServiceDate, "%m/%d/%Y").date()
                passed_date = date_EXPIRATION < date_TODAY      #The service date is passed due.
                if passed_date:
                    PSD_newfile.write('{},{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate, Item_DAMAGED))

# ------------------------ PAST SERVICE DATE ---------------#



# ------------------------ DAMAGED ITEMS -------------------#

    def Damaged_Items(self):

        Items = self.Item_LIST      #Connects Damaged_Items "Items" to __init__
        Item_KEY = sorted(Items.keys(), key=lambda n: Items[n]["Item_PRICE"], reverse=True)
        with open('DamagedInventory.csv', 'w') as DI_newfile:       #Creates DamagedInventory.csvv
            for item in Item_KEY:
                ID = item
                Manufacturer_NAME = Items[item]["Manufacturer_NAME"]
                Item_TYPE = Items[item]["Item_TYPE"]
                Item_PRICE = Items[item]["Item_PRICE"]
                ServiceDate = Items[item]["ServiceDate"]
                Item_DAMAGED = Items[item]["Item_DAMAGED"]
            if Item_DAMAGED:
                DI_newfile.write('{},{},{},{},{}\n'.format(ID, Manufacturer_NAME, Item_TYPE, Item_PRICE, ServiceDate))

# ------------------------ DAMAGED ITEMS -------------------#



if __name__ == "__main__":
    Items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    Items[item_id] = {}
                    Manufacturer_NAME = line[1]     #Manufacturer Name is index 1
                    Item_TYPE = line[2]             #Item Type is Index 2
                    Item_DAMAGED = line[3]          #Damaged Item is Index 3
                    Items[item_id]["Manufacturer_NAME"] = Manufacturer_NAME.strip()
                    Items[item_id]["Item_TYPE"] = Item_TYPE.strip()
                    Items[item_id]["Item_DAMAGED"] = Item_DAMAGED
                elif file == files[1]:
                    Item_PRICE = line[1]
                    Items[item_id]["Item_PRICE"] = Item_PRICE
                elif file == files[2]:
                    ServiceDate = line[1]
                    Items[item_id]["ServiceDate"] = ServiceDate


#------------------ CSV FILE OUTPUT --------------------#
    inventory = Complete_Inventory_Output(Items)
    inventory.Full_Inv()
    inventory.Type_Org()
    inventory.Past_Service_Date()
    inventory.Damaged_Items()
#------------------ CSV FILE OUTPUT --------------------#
