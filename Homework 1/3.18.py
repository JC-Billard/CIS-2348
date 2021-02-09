import math

# Color Dictionary
paint_colors = {
    "red":35,
    "blue":25,
    "green":23
}

# Question 1
wall_height = int(input(("Enter wall height (feet):\n"))) #wall height input
wall_width = int(input(("Enter wall width (feet):\n"))) #wall width input
wall_area = (wall_height * wall_width) #area calculation
print("Wall area:", wall_area, "square feet") #area output

# Question 2
paint_needed = (wall_area / 350) #Needed Paint Calculation
print("Paint needed:", round(paint_needed, 2), "gallons") #Needed Paint Output

# Question 3
cans = (math.ceil(paint_needed))
print("Cans needed:", cans, "can(s)\n") #Cans Needed Output


# Question 4
choice = str(input("Choose a color to paint the wall:\n"))
print("Cost of purchasing ", choice, " paint: $", paint_colors[choice] * cans, sep='')
