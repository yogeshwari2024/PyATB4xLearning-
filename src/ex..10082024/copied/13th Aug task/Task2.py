'''

Task #2

Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}

'''

num_1 = int(input("Enter the number 1 value : "))
num_2 = int(input("Enter the number 2 value : "))


print(f"Maximum of two given numbers :{max(num_1,num_2)}")
print(f"Power of number 1 to number 2 is : {pow(num_1,num_2)}")
print(f"Substraction between two number s : { num_1 - num_2}")
print(f"multiplication of two numbers is : {num_1*num_2}")
print(f"Addition of two numbers is : {num_1 + num_2}")
print(f"Division of two numbers is {num_1/num_2:.2f}")
