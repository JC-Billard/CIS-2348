# JAKE BILLARD UHID 1582534 program 5.22: Automobile service invoice

#Service and price dictionary
services_and_prices = {'Oil change': 35,
                        'Tire rotation': 19,
                        'Car wash': 7,
                        'Car wax': 12,
                        '-': 0}

#1
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

#2
first_service_choice = input("\nSelect first service:\n")     #First service input
second_service_choice = input("Select second service:\n")   #Second service input

#3
print("\nDavy's auto shop invoice")

#Calling upon the dictionary based on the user input.
first_service_price = services_and_prices[first_service_choice]
second_service_price = services_and_prices[second_service_choice]
service_price_total = first_service_price+second_service_price

#If-Else statement in case '-' is used
if first_service_choice == '-':
    print("\nService 1:", 'No service')
    print("Service 2: {}, ${}".format(second_service_choice, second_service_price))
    print('\nTotal:', '${:.0f}'.format(second_service_price))
elif second_service_choice == '-':
    print("\nService 1: {}, ${}".format(first_service_choice, first_service_price))
    print("Service 2:", 'No service')
    print('\nTotal:', '${:.0f}'.format(first_service_price))
else:
    print("\nService 1: {}, ${}".format(first_service_choice, first_service_price))
    print("Service 2: {}, ${}".format(second_service_choice, second_service_price))
    print("\nTotal:", '${:.0f}'.format(service_price_total))
