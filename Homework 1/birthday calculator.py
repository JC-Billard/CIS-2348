#JAKE BILLARD UHID 1582534 birthday calculator program

print("Birthday Calculator")

print("Current day")
Month_1 = int(input("Month: "))
Day_1 = int(input("Day: "))
Year_1 = int(input("Year: "))

print("Birthday")
Month_2 = int(input("Month: "))
Day_2 = int(input("Day: "))
Year_2 = int(input("Year: "))

print("You are", Year_1 - Year_2, "years old.")

CurrentDay = (Month_1, Day_1)
BirthDay = (Month_2, Day_2)

if CurrentDay == BirthDay:
    print("Happy Birthday!")
