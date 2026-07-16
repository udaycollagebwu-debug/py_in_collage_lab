#1. wriht a program to find the area of a triangle.
side1=int(input("Enter the side 1 of the tringle :"))
side2=int(input("Enter the side 2 of the tringle :"))
side3=int(input("Enter the side 3 of the tringle :"))

s=(side1+side2+side3)/2

area=(s*(s-side1)*(s-side2)*(s-side3))**0.5
print("the arear is :",area)
