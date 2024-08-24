# create a program to sum of three number from the user input

num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
num3 = int(input("enter the num3: "))


def sum_of_three_number(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_three_number(num1, num2, num3)
print(result)


# result = sum_of_three_number(n1=num1, n2=num2, n3=num3)
# print(result)
# =====================================

# def print_arguments(*args):


## * args = multiple argument with no limit -> list
# print(args[0])

# print_arguments("pramod")
