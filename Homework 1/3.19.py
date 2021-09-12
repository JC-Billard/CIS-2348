#JAKE BILLARD UHID 1582534 program 3.19: Painting a wall
import math

#1
wall_height_1 = int(input("Enter wall height (feet):\n"))   # Wall height 1 input
wall_width_1 = int(input("Enter wall width (feet):\n"))     # Wall width 1 input
wall_area_1 = (wall_height_1*wall_width_1)                  # Calculates area
print("Wall area:", wall_area_1, "square feet")                            # Prints area

#2
squareft = 350                                            # stores 350 in variable
paint_needed = (wall_area_1/squareft)                       # Division
print('Paint needed:', '{:.2f}'.format(paint_needed), "gallons")                                         # prints paint_needed

#3
cans_needed = math.ceil(paint_needed)                       # rounds paint_needed up
print("Cans needed:", cans_needed, "can(s)")

#4
color_pick = input("\nChoose a color to paint the wall:\n")
color_price = 0
if color_pick == "red":
    color_price = 35
elif color_pick == "blue":
    color_price = 25
elif color_pick == "green":
    color_price = 23
else:
    print("we dont have that paint color")
new_color_price = color_price*cans_needed
print("Cost of purchasing", color_pick, "paint:", '${:.0f}'.format(new_color_price))
