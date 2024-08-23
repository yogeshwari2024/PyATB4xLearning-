# Conditions and Loops

# write a program to take a user age and let him know if he can go the club.

# logic building
# 1.user i/p - data type -> int
# o/p -> string-> user if he can go or not

# 2. Rough logic
# age > 21 -> print can go
# age < 21 -> print can't go


user_age = int(input("Enter the age of user : "))

if user_age >= 21:
    print("he/she can go to club")
else:
    print("can't go")
