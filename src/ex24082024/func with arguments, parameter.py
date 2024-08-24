# functions with arguments and parameters


def greet():
    print("hello, there!!")


def greet_by_name(x):
    print("hello,", x)


greet_by_name("pramod")
greet_by_name(4535)
greet_by_name(434.8)


def greet(name):
    print("hello,", name)

name = input("enter ur name\n")
greet(name)