print("Welcome!")
n = float(input("Please input a number: "))
print()
print("What would you like to do with this number:\n0) Get the additive inverse of the number\n1) Get the reciprocal of the number\n2) Square the number\n3) Cube the number\n4) Exit the program")
option = int(input())

match option:
    case 0:
        print(f"The additive inverse of {n} is {n * -1}")
    case 1:
        if(n == 0):
            print("Cannot divide by 0!")
        print(f"The reciprocal of {n} is {round(1/n,3)}")
    case 2:
        print(f"The square of {n} is {n * n}")
    case 3:
        print(f"The cube of {n} is {pow(n, 3)}")
    case 4:
        print("Thank you, goodbye!")
    case _:
        print("Invalid option!") 