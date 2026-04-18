def allMath(x, y):
    if y == 0:
        div = None
        floor = None
        modulus = None
    else:
        div = x / y
        floor = x // y
        modulus = x % y

    temp = (x + y,
            x - y,
            x * y,
            div,
            floor,
            modulus,
            pow(x, y))

    return temp


x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
print(f"Your resulting tuple is {allMath(x,y)}")