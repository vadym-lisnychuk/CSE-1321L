def isValid(width, height):
    return width + height > 30.0

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

while True:
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if isValid(width, height):
        print("This is a valid rectangle.")
        print(f"The area is: {area(height, width)}")
        print(f"The perimeter is: {perimeter(width, height)}")
        print()
    else:
        print("This is an invalid rectangle.")
        print()

    match input("Do you want to enter another width and height (Y/N)?: "):
        case 'Y':
            print()
        case 'N':
            print()
            print("Program Ends")
            break
        case _:
            print()