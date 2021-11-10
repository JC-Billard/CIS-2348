#JAKE BILLARD | UHID 1582534
input = input().split() # Puts input into a list
for word in input:
    word_frequency = input.count(word)   #counts each word given in input
    print(word, word_frequency)
