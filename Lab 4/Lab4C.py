a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

if (a <= 0 or b <= 0 or c <= 0):
    print("Invalid input. All sides must be greater than 0.")
elif(a == b == c):
    print("The triangle is an equilateral triangle.")
elif(a == b or b == c or a == c):
    print("The triangle is an isosceles triangle.")
elif(a + b <= c or a + c <= b or b + c <= a):
    print("The sides do not form a valid triangle.")
else:
    print("The triangle is a scalene triangle.")