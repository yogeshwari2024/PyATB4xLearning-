# loop : repeat block of code multiple times

#  loop Types in python :  1) For loop , 2) while loop

# For Loop : can execute a block of code multiple times
# syntax :
#  for varaible name in the range(start, stop, step):

# // code that has be executed

for i in range(1,10):  # to start 1 to stop 10-1, step =1, ==> 9
    print(i)

#############

for value in range(1,10,2):  # 1 3 5 7 9
    print(value,end=" ")


#############

print("\n")

for i in range(0,10):
    print("Hello world!", i)

#############
print("\n")

for number in range(10,0,-2): # 10,8,6,4,2
    print(number)

### list

my_list = list(range(1,10))
print(my_list)

