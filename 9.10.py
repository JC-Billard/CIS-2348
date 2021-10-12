# JAKE BILLARD UHID 1582534
import csv

#gets user input
input1 = input()


csv_input = (open('input1.csv','r'))    #Opens input1.csv and reads it
csv_file = csv.reader(csv_input, delimiter=',')
for row in csv_file:
    _list = row                          #Sets up the row in the CSV file with "list"

no_duplicates = list(dict.fromkeys(_list))
length = len(no_duplicates)

for i in range(length):
    print(no_duplicates[i], _list.count(no_duplicates[i]))
