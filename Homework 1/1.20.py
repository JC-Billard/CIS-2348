#Jake Billard UHID 1582534
import math

int_1 = int(input("Enter integer:\n"))      #asks for integer input
print("You entered:", int_1)               #displays input
int_1squared = int(math.pow(int_1,2))       #squares the input and turns it into an integer
int_1cubed = int(math.pow(int_1,3))         #cubes the input and turns it into an integer
print(int_1, "squared is", int_1squared)       #displays the integer and it's squared number
print("And", int_1, "cubed is", int_1cubed, "!!")        #displays the integer and it's cubed number

int_2 = int(input("Enter another integer:\n"))      #asks for a second integer input
addition_ = int_1 + int_2                           #Adds Int 1 and 2
multiplication_ = int_1 * int_2                     #Multiplies Int 1 and 2
print(int_1, "+", int_2, "is", addition_)            #Displays Addition
print(int_1, "*", int_2, "is", multiplication_)      #Displays Multiplication
