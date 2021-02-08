#Service Dictionary
service_menu = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

#Menu print
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()

#Service input
service1 = str(input("Select first service:\n"))
service2 = str(input("Select second service:\n"))
print()

#Invoice
print("Davy's auto shop invoice\n")
if service1 == "Oil change":
    print("Service 1: Oil change, $", service_menu[service1])
elif service1 == "Tire rotation":
    print("Service 1: Tire rotation, $", service_menu[service1])
elif service1 == "Car wash":
    print("Service 1: Car wash, $", service_menu[service1])
elif service1 == "Car wax":
    print("Service 1: Car wax, $", service_menu[service1])
elif service1 == "-":
    print("Service 1: No service")

if service2 == "Oil change":
    print("Service 2: Oil change, $", service_menu[service2])
elif service2 == "Tire rotation":
    print("Service 2: Tire rotation, $", service_menu[service2])
elif service2 == "Car wash":
    print("Service 2: Car wash, $", service_menu[service2])
elif service2 == "Car wax":
    print("Service 2: Car wax, $", service_menu[service2])
elif service2 == "-":
    print("Service 2: No service")
print()

print("Total: $", service_menu[service1]+service_menu[service2])
