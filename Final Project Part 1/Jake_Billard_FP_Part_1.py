#   Jake Billard   UHID 1582534
#   FINAL PROJECT Part 1
import csv
from operator import itemgetter
import sys


#--- LISTS ---#
Manufacturer_LIST = []
Price_LIST = []
ServiceDates_LIST = []
#--- LISTS ---#


#--- CSV File Input ---#
with open("ManufacturerList.csv") as MFList:
    M_reader = csv.reader(MFList)           # Reads ManufacturerList.csv
    for line in M_reader:
        Manufacturer_LIST.append(line)          # Appends the info from ManufacturerList.csv to it's own list.

with open("PriceList.csv") as PList:
    P_reader = csv.reader(PList)            # Reads PriceList.csv
    for line in P_reader:
        Price_LIST.append(line)            #Appends the info from PriceList.csv to it's own list.

with open("ServiceDatesList.csv") as SDList:
    SD_reader = csv.reader(SDList)          #Reads ServiceDatesList.csv
    for linee in SD_reader:
        ServiceDates_LIST.append(line)           # Appends the info from ServiceDatesList.csv to it's own list.
#--- CSV File Input ---#


#--- Creating New Sorted Lists ---#
sorted_Manufacturer_LIST = (sorted(Manufacturer_LIST, key=itemgetter(0)))
sorted_Price_LIST = (sorted(Price_LIST, key=itemgetter(0)))
sorted_ServicesDates_LIST = (sorted(ServiceDates_LIST, key=itemgetter(0)))
#--- Creating New Sorted Lists ---#


for n in range(0, len(sorted_Manufacturer_LIST)):
    sorted_Manufacturer_LIST[n].append(Price_LIST[n][1])   # Appends Price_LIST into sorted_Manufacturer_LIST.
for n in range(0, len(sorted_Manufacturer_LIST)):
    sorted_Manufacturer_LIST[n].append(ServiceDates_LIST[n][1])   # Appends ServiceDates_LIST into sorteed_Manufacturer_LIST.



combined_LIST = sorted_Manufacturer_LIST   # Combines all the appends into sorted_Manufacturer_LIST into one big list.
inventory = (sorted(combined_LIST, key=itemgetter(1)))      #Sorts combined_LIST by Manufacturer
                                                                        #and declares it as inventory


with open('FullInventory.csv', 'w') as new_FullInventory:
    FI_writer = csv.writer(new_FullInventory)           #Creates a new file: FullInventory.csv
    for n in range(0, len(inventory)):
        FI_writer.writerow(inventory[n])    # Writes everything from the inventory variable/list into the FullInventory.csv file.


#--- Item Type Lists ---#
Phone_LIST = []
Laptop_LIST = []
Tower_LIST = []
Item_LIST = []
Item_LIST = combined_LIST #Declares Item_LIST is combined_LIST
Damaged_LIST = []
#--- Item Type Lists ---#


for n in range(0, len(Item_LIST)):
    if Item_LIST[n][2] == "phone":
        Phone_LIST.append(Item_LIST[n])         #If user enters "phone", the item is appended to Item_LIST
    elif Item_LIST[n][2] == "laptop":
        Laptop_LIST.append(Item_LIST[n])        #If user enters "laptop", the item is appended to Item_LIST
    elif Item_LIST[n][2] == "tower":
        Tower_LIST.append(Item_LIST[n])         #If user enters "tower", the item is appended to Item_LIST


#--- Writing new CSV files ---#

#Phones
with open('PhoneInventory.csv', 'w') as new_PhoneInventory:
    PI_writer = csv.writer(new_PhoneInventory)
    for n in range(0, len(Phone_LIST)):
        PI_writer.writerow(Phone_LIST[n])   #Writes everything from Phone_LIST into PhoneInventory.csv

#Laptops
with open('LaptopInventory.csv', 'w') as new_LaptopInventory:
    LI_writer = csv.writer(new_LaptopInventory)
    for n in range(0, len(Laptop_LIST)):
        LI_writer.writerow(Laptop_LIST[n])      #Writes everything from Laptop_LIST into LaptopInventory.csv

#Towers
with open('TowerInventory.csv', 'w') as new_TowerInventory:
    TI_writer = csv.writer(new_TowerInventory)
    for n in range(0, len(Tower_LIST)):
        TI_writer.writerow(Tower_LIST[n])       #Writes everything from Tower_LIST into TowerInventory.csv

#--- Writing new CSV files ---#


#--- Damaged Inventory ---#
for n in range(0, len(Item_LIST)):
    if Item_LIST[n][3] == "damaged":
        Damaged_LIST.append(Item_LIST[n])       #Appends Items to the Damaged_LIST if it's third index reads "damaged".
Damaged_LIST = (sorted(Damaged_LIST, key=itemgetter(4), reverse=True))      #Sorts Damaged_LIST by it's Price index.

with open('DamagedInventory.csv', 'w') as new_DamagedInventory:
    DI_writer = csv.writer(new_DamagedInventory)
    for n in range(0, len(Damaged_LIST)):
        DI_writer.writerow(Damaged_LIST[n])     #Writes everything from Damaged_LIST into DamagedInventory.csv
#--- Damaged Inventory ---#

