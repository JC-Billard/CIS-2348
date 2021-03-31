# Jake Billard UHID 1582534

words_input = input().split() # Puts input into a list

for word in words_input:
    frequency = words_input.count(word)   #counts each word
    print(word, frequency)   #prints each word with their respective frequency

