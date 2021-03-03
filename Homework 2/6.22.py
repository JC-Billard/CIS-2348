#Jake Billard 1582534

#first x input
first_x = int(input())
#first y input
first_y = int(input())
#first z input
first_z = int(input())

#second x input
second_x = int(input())
#second y input
second_y = int(input())
#second z input
second_z = int(input())

def equation1(x, y):
    return ((first_x * x) + (first_y * y)) - first_z
def equation2(x, y):
    return ((second_x * x) + (second_y * y)) - second_z
    
solution = False

for x in range (-10, 10):
    for y in range (-10, 10):
        if equation1(x, y) == equation2(x, y) and equation1(x, y) == 0:
          print(x, y)
          solution = True

if (solution == False):
    print("No solution")
          