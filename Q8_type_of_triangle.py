# WAP to determine the type of a triangle whether it is Equilateral, Isosceles or Scalene

# Taking input of sides of a triangle

a=int(input("Enter first side of the triangle: "))
b=int(input("Enter second side of the triangle: "))
c=int(input("Enter third side of the triangle: "))

# Check if the sides form a valid triangle
if (a + b > c) and (b + c > a) and (a + c > b):
    # Determine triangle type
    if a == b == c:
        print("Given sides are of EQUILATERAL TRIANGLE")
    elif a == b or b == c or c == a:
        print("Given sides are of ISOSCELES TRIANGLE")
    else:
        print("Given sides are of SCALENE TRIANGLE")
else:
    print("Invalid Input: The given sides do NOT form a valid triangle.")

"""
------------------------SAMPLE OUTPUT------------------------
Enter first side of the triangle: 4
Enter second side of the triangle: 8
Enter third side of the triangle: 8
Given sides are of ISOSCELES TRIANGLE
-------------------------------------------------------------
"""
