# write a python program to calculate the area of a circle
# given its radius using the formula
import math

# ---- area = pie*r^2 ---- take pie as 3.14

# logic building formula

# step 1 ) figure out the inputs and outputs

# inputs -> r -> data type (int/float)
# pi -> 3.14 , or math.pi (import math)
# power -> ask user if want ot use pow or ** -> any

# o/p - > float - area, print area

# step 2)
#rough logic = area = 3.14*pow(r,2)

# step 3) write the logic

radius = float(input("enter the radius of circle : \n"))
print(radius)
print(math.pi)
area = math.pi * math.pow(radius,2)
print(f"area of a circle is  -> {area:.2f}")

# above program in one line

print("\n")
print(3.14*float(input("enter the radius -> "))**2)