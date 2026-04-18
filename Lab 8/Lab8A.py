import random

seed = int(input("Enter a seed value: "))

random.seed(seed)

a = int(input("How many times would you like to roll the die? "))
sum = 0

for i in range(a):
    b = random.randint(1, 6)
    sum += b
    print(f"Roll {i + 1}: {b}")

print(f"Total: {sum}")