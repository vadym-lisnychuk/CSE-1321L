size = int(input("Enter an odd number for the size of the hourglass: "))
if size % 2 == 0:
    size += 1

val = 0
for i in range(size // 2):
    print(" " * i, end="")
    for j in range(size - 2 * i):
        print(val % 10, end="")
        val += 1
    print()

for i in range(size // 2, -1, -1):
    print(" " * i, end="")
    for j in range(size - 2 * i):
        print(val % 10, end="")
        val += 1
    print()