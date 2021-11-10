#JAKE BILLARD | UHID 1582534

num_input = map(int, input().split())  #List Input
num_list = [x for x in num_input if x >= 0]   #Removes the Negative Values
num_list.sort()  #Smallest to largest
print(*num_list, sep = " ", end='' + ' ')
