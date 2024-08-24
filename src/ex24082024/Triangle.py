# Triangle classifier
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

a = float(input("enter side a: "))
b = float(input("enter side b: "))
c = float(input("enter side c: "))

if a == b and b == c and c == a:
    print("it is equilateral triangle")
elif a != b and b != c and c != a:
    print("it is scalen triangle")
else:
    print("it is isoscelen triangle ")
