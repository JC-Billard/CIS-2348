#Jake Billard 1582534

#Enter Password
password = input()

#Replacement Values
password = password.replace("i", "!")
password = password.replace("a", "@")
password = password.replace("m", "M")
password = password.replace("B", "8")
password = password.replace("o", ".")

#Print New Password & Add "q*s"
print(password + "q*s")
