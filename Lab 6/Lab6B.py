import random
print("Guess the number I am thinking!")

mystery = True
random_number = random.randint(1, 100)
while mystery:
    x = int(input("Enter any number between 1 and 100: "))
    if(x > random_number):
        print("Too high!")
    elif(x < random_number):
        print("Too low!")
    else:
        print(f"Correct! I was thinking of {random_number}")
        mystery = False