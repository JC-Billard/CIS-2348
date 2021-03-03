#Jake Billard 1582534
input_word = input()

if input_word.replace(' ','') == input_word.replace(' ','')[::-1]:
    print(input_word, "is a palindrome")
else:
    print(input_word, "is not a palindrome")
