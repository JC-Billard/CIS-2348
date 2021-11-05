# JAKE BILLARD | UHID 1582534
# FINAL PROJECT - PART 1
import csv
from datetime import datetime


class inventory__output:

    def __init__(self, full_item_list):
        self.full_item_list = full_item_list


#full inventory - works

    def Full_Inventory(self):

        with open('FullInventory.csv', 'w') as FullInv_nf:
            Item_dict = self.full_item_list
            Itemdict_key = sorted(Item_dict.keys(), key=lambda n: Item_dict[n]["manufacturer"])   #Itemdict_key is sorted by manufacturer using lambda

            for item in Itemdict_key:                                                              #FullInventory.csv is created by linking each aspect to an item inside the csv file
                theitem = item
                manufacturer = Item_dict[item]["manufacturer"]
                it_type = Item_dict[item]["it_type"]
                it_price = Item_dict[item]["it_price"]
                service_date = Item_dict[item]["service_date"]
                it_damaged = Item_dict[item]["it_damaged"]
                FullInv_nf.write('{},{},{},{},{},{}\n'.format(theitem, manufacturer, it_type, it_price, service_date, it_damaged))      #writes each aspect of Full_Inventory.csv in order



#type inventory - works

    def Type_Inv(self):

        Item_dict = self.full_item_list
        item_type_list = []                         #Created a list of each item type
        Itemdict_key = sorted(Item_dict.keys())

        for item in Item_dict:
            it_type = Item_dict[item]["it_type"]
            if it_type not in item_type_list:
                item_type_list.append(it_type)     #If item type (it_type) is not in the item_type_list list, it will be appended.

        for type in item_type_list:
            file_name = type.capitalize() + 'Inventory.csv'     #Creates a separate file for each product type (phone, tower, laptop)

            with open(file_name, 'w') as type_inv_nf:           #Writes separate product type csv files
                for item in Itemdict_key:
                    theitem = item
                    manufacturer = Item_dict[item]["manufacturer"]
                    it_price = Item_dict[item]["it_price"]
                    service_date = Item_dict[item]["service_date"]
                    it_damaged = Item_dict[item]["it_damaged"]
                    it_type = Item_dict[item]["it_type"]
                    if type == it_type:
                        type_inv_nf.write('{},{},{},{},{}\n'.format(theitem, manufacturer, it_price, service_date, it_damaged))     #writes each aspect of Type_Inv in order



#past service date - works

    def Past_Service_Date(self):

        Item_dict = self.full_item_list      #Connects Past_Service_Date "Item_dict" to __init__
        Itemdict_key = sorted(Item_dict.keys(), key=lambda n: datetime.strptime(Item_dict[n]["service_date"], "%m/%d/%Y").date(), reverse=True)  #Itemdict_key is sorted by oldest date to newest date using lambda and dateime.striptime

        with open('PastServiceDateInventory.csv', 'w') as psd_nf:      #Writes PastServiceDateInventory.csv
            for item in Itemdict_key:
                theitem = item
                manufacturer = Item_dict[item]["manufacturer"]
                it_type = Item_dict[item]["it_type"]
                it_price = Item_dict[item]["it_price"]
                service_date = Item_dict[item]["service_date"]
                it_damaged = Item_dict[item]["it_damaged"]
                current_date = datetime.now().date()
                expired_date = datetime.strptime(service_date, "%m/%d/%Y").date()
                passed_date = expired_date < current_date
                if passed_date:
                    psd_nf.write('{},{},{},{},{},{}\n'.format(theitem, manufacturer, it_type, it_price, service_date, it_damaged))      #writes each aspect of PastServiceDateInventory.csv in order



#damaged Item dictionary - works

    def Damaged_Item_dict(self):

        Item_dict = self.full_item_list      #Connects Damaged_Item_dict "Item_dict" to __init__
        Itemdict_key = sorted(Item_dict.keys(), key=lambda n: Item_dict[n]["it_price"], reverse=True)                                   #Itemdict_key is sorted by most expensive to least expensive

        with open('DamagedInventory.csv', 'w') as di_nf:       #Creates DamagedInventory.csvv
            for item in Itemdict_key:
                theitem = item
                manufacturer = Item_dict[item]["manufacturer"]
                it_type = Item_dict[item]["it_type"]
                it_price = Item_dict[item]["it_price"]
                service_date = Item_dict[item]["service_date"]
                it_damaged = Item_dict[item]["it_damaged"]
                if it_damaged:
                    di_nf.write('{},{},{},{},{}\n'.format(theitem, manufacturer, it_type, it_price, service_date))                  #writes each aspect of DamagedInventory.csv in order



#main
if __name__ == "__main__":
    Item_dict = {}              #Dictionary is created
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                Item_ID = line[0]                                               #Item ID number is assigned to index 0
                if file == files[0]:
                    Item_dict[Item_ID] = {}
                    manufacturer = line[1]                                      #manufacturer (name) is assigned to index 1
                    it_type = line[2]                                           #item type is assigned to index 2
                    it_damaged = line[3]                                        #damaged item is assigned to index 3
                    Item_dict[Item_ID]["manufacturer"] = manufacturer.strip()
                    Item_dict[Item_ID]["it_type"] = it_type.strip()
                    Item_dict[Item_ID]["it_damaged"] = it_damaged
                elif file == files[1]:
                    it_price = line[1]
                    Item_dict[Item_ID]["it_price"] = it_price
                elif file == files[2]:
                    service_date = line[1]
                    Item_dict[Item_ID]["service_date"] = service_date
#csv file output
    program = inventory__output(Item_dict)
    program.Full_Inventory()
    program.Type_Inv()
    program.Past_Service_Date()
    program.Damaged_Item_dict()
