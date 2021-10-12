#JAKE BILLARD UHID 1582534


def Palindrome(input):
    return input == input[::-1]     #Defines Palindrome function

input = input()
input_replace = input.replace(' ', '')
process1 = Palindrome(input_replace)        #process1 connects the user input to the palindrome function

if process1:
    print(input, 'is a palindrome')
else:
    print(input, 'is not a palindrome')
