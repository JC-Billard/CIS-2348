#JAKE BILLARD UHID 1582534 Program 2.18 - Cooking measurement converter.

#1
lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(servings), "servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar")
print()
#2
servings2 = float(input("How many servings would you like to make?\n"))
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(servings2), "servings")
lemon_juice2 = float((servings2 / 3))
print('{:.2f}'.format(lemon_juice2), "cup(s) lemon juice")
water2 = float((servings2 / 0.375))
print('{:.2f}'.format(water2), "cup(s) water")
agave_nectar2 = float((servings2 / 2.4))
print('{:.2f}'.format(agave_nectar2), "cup(s) agave nectar\n")
 #3
print("Lemonade ingredients - yields", '{:.2f}'.format(servings2), "servings")
print('{:.2f}'.format(lemon_juice2 / 16), "gallon(s) lemon juice")
print('{:.2f}'.format(water2 / 16), "gallon(s) water")
print('{:.2f}'.format(agave_nectar2 / 16), "gallon(s) agave nectar")
