# Jake Billard 1582534
import csv

csv_input = input() #input file name

#open csv file and read it
file=open(csv_input,'r')
hwfile = csv.reader(file, delimiter = ',')
for row in hwfile:
    word_list = row

#no duplicates and correct order
nodups = list(dict.fromkeys(word_list))
length = len(nodups)
for n in range(length):
    print(nodups[n], word_list.count(nodups[n]))



