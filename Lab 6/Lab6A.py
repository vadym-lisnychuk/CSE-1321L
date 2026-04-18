run = True
while run:
    print("Multiplication and Exponent Calculator")
    print("Choose option 1 for Multiplication")
    print("Choose option 2 for Exponentiation")
    print("Choose option 3 to Exit")
    option = int(input())
    print()

    match option:
        case 1:
            operand_1 = int(input("Enter an operand: "))
            operand_2 = int(input("Enter the other operand: "))
            result = 0
            for i in range(operand_1):
                for j in range(operand_2):
                    result += 1
            print(f"{operand_1} x {operand_2} = {result}")
            print()

        case 2:
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            result = 1

            for i in range(exponent):
                temp = 0
                for j in range(base):
                    temp += result
                result = temp

            print(f"{base}^({exponent}) = {result}")
            
        case 3:
            print("Closing the Calculator...")
            run = False
        case _:
            print("Invalid Choice")
            print()