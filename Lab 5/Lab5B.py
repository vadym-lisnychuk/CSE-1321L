run = True
print("[Factorial Calculator]")
while run:
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Error: Number must be 0 or positive, try again.")
        print()
    else:
        print(f"Calculating {num}! ...")
        
        fact = 1
        for i in range (1, num + 1):
            fact = fact * i

        print(f"{num}! is {fact}")
        print()
        print("Program Terminated")
        run = False