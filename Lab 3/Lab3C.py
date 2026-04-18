sizes = ["small", "medium", "large", "extra-large"]

# 0 - small 1 - medium 2 - large 3 - xlarge
time = [30, 60, 75, 135] 
amounts = []

total_time = 0

for i in range(0, 4):
    x = int(input(f"Enter the number of {sizes[i]} sandwiches: "))
    amounts.append(x)
    total_time += time[i] * amounts[i]

for i in range(0, 4):
    print(f"You've entered {amounts[i]} {sizes[i]} sandwiches.")


minutes = int(total_time / 60)
seconds = int(total_time % 60)

print(f"Total cooking time is {minutes} minutes and {seconds} seconds.")