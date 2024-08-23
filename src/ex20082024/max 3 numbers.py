# find max between 3 numbers

# logic building

# user i/p - num1, num2,num3-> int
# op -> int or string with max number.

# logic ? if else -1 condition
# more than 1 condition -> if elif else

num1 = int(input("enter the 1st number\n"))  # 5 , #10
num2 = int(input("enter the 2nd number\n"))  # 3 , # 12
num3 = int(input("enter the 3rd number\n"))  # 2, # 11

# 5 > 3 and 5 > 2 -> true -- 5 is max
# num1 > num2 and num1 > num2 -> num1 is greater

# num2 > num1 and num2> num3 -> num2 is greater
# 12 >10 and 12 > 11 -> true -- 12 is max

# else num3

if num1 >= num2 and num1 >= num3:
    print("max is ", num1)
elif num2 >= num1 and num2 >= num3:
    print("max is ", num2)
else:
    print("max is ", num3)
