# Jake Billard UHID 1582534

numeral_input = map(int, input().split())  #List Input

number_list = [x for x in numeral_input if x >= 0]   #Removes the Negative Values

number_list.sort()  #Sorts List from Smallest to largest

print(*number_list, sep = " ", end='' + ' ')
