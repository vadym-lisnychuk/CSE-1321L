largest_number = 1
print("Please enter 10 numbers and this program will display the largest.")
for i in range (1, 11):
    current_number = int(input(f"Please enter number {i}: "))
    if (current_number > largest_number):
        largest_number = current_number


print(f"The largest number was {largest_number}")