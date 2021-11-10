#Jake Billard UHID 1582534

#Menu operations below

#add player
def add_player():
    print("Enter a new player's jersey number:")
    inputjersey = int(input())

    while ((inputjersey < 0) or (inputjersey > 99)):
        print("Incorrect input")
        print("Enter a new player's jersey number:")
        inputjersey = int(input())

    print("Enter the player's rating:")
    inputrating = int(input())

    while ((inputrating < 1) or (inputrating) > 9):
        print("Incorrect input")
        print("Enter the player's rating:")
        inputrating = int(input())

    d.update({inputjersey:inputrating})

#remove player
def remove_player():
    print("Enter a jersey number:")
    inputjersey = int(input())
    while ((inputjersey < 0) or (inputjersey > 99)):
        print("Incorrect input")
        print("Enter a jersey number:")
        inputjersey = int(input())
    if inputjersey in d.keys():
        del d[inputjersey]

#update player
def update_player():
    print("Enter a jersey number:")
    inputjersey = int(input())
    while ((inputjersey < 0) or (inputjersey > 99)):
        print("Incorrect input")
        print("Enter a jersey number:")
    if inputjersey in d.keys():
        print("Enter a new rating for player:")
        inputrating = int(input())
        while ((inputrating < 1) or (inputrating > 9)):
            print("Incorrect input")
            print("Enter a new rating for player:")
            inputrating = int(input())

        d[inputjersey] = inputrating

#output roster
def output_roster():
    print("ROSTER")
    for (z, h) in sorted(d.items()):
        print("Jersey number: %d, Rating: %d" % (z, h))

#output players above an "a" rating
def above_a_rating():
    print("Enter a rating:")
    inputrating = int(input())

    while ((inputrating < 1) or (inputrating > 9)):
        print("Incorrect input")
        print("Enter a rating:")
        inputrating = int(input())
    print("ABOVE 5")

def menu():
    print('\nMENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')

menu()
menu_choice = 'mmm'
while(menu_choice != "q"):
#input with if, elif statements
    menu_choice = str(input("\nChoose an option:\n"))

    if(menu_choice == "a"):
            add_player()

    elif(menu_choice == "d"):
            remove_player()

    elif(menu_choice == "u"):
            update_player()

    elif(menu_choice == "r"):
            above_a_rating()

    elif(menu_choice == "o"):
            output_roster()

    else:
        pass

d = {}
d_list = []
for n in range(1, 6):
    print("Enter player", str(n) + "'s jersey number:")
    inputjersey = int(input())

    while ((inputjersey < 0) or (inputjersey > 99)):
        print("Incorrect input")
        print("Enter player", str(n) + "'s jersey number:")
    print("Enter player", str(n) + "'s rating:\n")
    inputrating = int(input())

    while ((inputrating < 1) or (inputrating > 9)):
        print("Incorrect input")
        print("Enter player", str(n) + "'s rating:\n")
        inputrating = int(input())
    d[inputjersey] = inputrating

print("ROSTER")
for (z, h) in sorted(d.items()):
    print("Jersey number: %d, Rating: %d" % (z, h))
