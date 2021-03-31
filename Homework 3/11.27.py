#Jake Billard UHID 1582534

d = {}
d_list = []

for n in range(1, 6):
    print("Enter player", str(n) + "'s jersey number:")
    jersey_input = int(input())

    while ((jersey_input < 0) or (jersey_input > 99)):
        print("Incorrect input")
        print("Enter player", str(n) + "'s jersey number:")

    print("Enter player", str(n) + "'s rating:\n")
    rating_input = int(input())

    while ((rating_input < 1) or (rating_input > 9)):
        print("Incorrect input")
        print("Enter player", str(n) + "'s rating:\n")
        rating_input = int(input())

    d[jersey_input] = rating_input


print("ROSTER")
for (z, h) in sorted(d.items()):
    print("Jersey number: %d, Rating: %d" % (z, h))


######      MENU OPERATIONS      ######

###   ADD PLAYER   ###
def add_player():
    print("Enter a new player's jersey number:")
    jersey_input = int(input())

    while ((jersey_input < 0) or (jersey_input > 99)):
        print("Incorrect input")
        print("Enter a new player's jersey number:")
        jersey_input = int(input())

    print("Enter the player's rating:")
    rating_input = int(input())

    while ((rating_input < 1) or (rating_input) > 9):
        print("Incorrect input")
        print("Enter the player's rating:")
        rating_input = int(input())

    d.update({jersey_input:rating_input})
###   ADD PLAYER   ###


###   REMOVE PLAYER   ###
def remove_player():
    print("Enter a jersey number:")
    jersey_input = int(input())

    while ((jersey_input < 0) or (jersey_input > 99)):
        print("Incorrect input")
        print("Enter a jersey number:")
        jersey_input = int(input())

    if jersey_input in d.keys():
        del d[jersey_input]
###   REMOVE PLAYER   ###


###   UPDATE PLAYER   ###
def update_player():
    print("Enter a new rating for player:")
    rating_input = int(input())

    while ((rating_input < 1) or (rating_input > 9)):
        print("Incorrect input")
        print("Enter a new rating for player:")
        rating_input = int(input())

    d[jersey_input] = rating_input
###   UPDATE PLAYER   ###


###   OUTPUT ROSTER   ###
def output_roster():
    print("ROSTER - check")
    for (z, h) in sorted(d.items()):
        print("Jersey number: %d, Rating: %d" % (z, h))
###   OUTPUT ROSTER   ###


###   OUTPUT PLAYERS ABOVE A RATING   ###
def above_a_rating():
    print("Enter a rating:")
    rating_input = int(input())

    while ((rating_input < 1) or (rating_input > 9)):
        print("Incorrect input")
        print("Enter a rating:")
        rating_input = int(input())
    print("ABOVE 5")
###   OUTPUT PLAYERS ABOVE A RATING   ###

######      MENU OPERATIONS      ######



print("""\nMENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit

Choose an option:""")

menu_choice: str = input()

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

        
elif(menu_choice == "q"):
        exit()