#JAKE BILLARD UHID 1582534

#inputs for first equation
x1 = int(input())
y1 = int(input())
z1 = int(input())

#inputs for second equation
x2 = int(input())
y2 = int(input())
z2 = int(input())

#define equations
def equation1(x,y):
    return ((x1*x)+(y1*y))-z1
def equation2(x,y):
    return ((x2*x)+(y2*y))-z2
solution = False

for x in range(-10,10):
    for y in range(-10,10):
        if equation1(x, y) == equation2(x, y) and equation1(x, y) == 0:
          print(x, y)
          solution = True
if (solution == False):
    print("No solution")
