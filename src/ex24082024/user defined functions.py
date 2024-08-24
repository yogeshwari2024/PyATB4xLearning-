# definition  and calling
# user defined functions
# 1. they can't return -> no return
# 2.they can return something
# they have parameters
# they don't have parameter/arguments


# 1. they can't return -> no return type and no parameter
print("1. output of no return type and no parameter\n ")
def greet():
    print("hello world")

result = greet()
print(result,"\n")


# 2 . no return type with argument
print("2. no return type with argument \n")
def greet_by_name(name):
    print("hello", name,"\n")

greet_by_name("pramod")


# 3. no return type with default argument

print("3. no return type with default argument \n")
def say_hello_default_arg(name="pramod"):
    print("hello", name.upper())


say_hello_default_arg("amit")
say_hello_default_arg()
say_hello_default_arg(name="tushar")  # positional agrument


################
print("\n")
def multiple_agrs(name1="arpita", name2="pramod", name3="amit"):
    print("multiple arguments", name1, name2, name3)

multiple_agrs(name1="ram", name2="sham", name3="amit")


#### 4. Argument + return type
print("4. Argument + return type \n")
def sum_of_two_number(num1, num2):
    return num1 + num2


result = sum_of_two_number(10, 24)
print(result,"\n")

#####

print("\n")

def greet_to_all_of_you():
    print("Hello , Everyone")


def greet():
    print("yes")
    greet_to_all_of_you()


greet()
# greet_to_all_of_you()


