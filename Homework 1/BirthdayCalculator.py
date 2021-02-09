print("Birthday Calculator")

print("Current day")
Month1 = int(input("Month: "))
Day1 = int(input("Day: "))
Year1 = int(input("Year: "))

print("Birthday")
Month2 = int(input("Month: "))
Day2 = int(input("Day: "))
Year2 = int(input("Year: "))

print("You are", Year1 - Year2, "years old.")

CurrentDay = (Month1, Day1)
BirthDay = (Month2, Day2)

if CurrentDay == BirthDay:
    print("Happy Birthday!")



