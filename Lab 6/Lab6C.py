while True:
    row = int(input("Enter Number for Rows or 0 to quit: "))
    if row == 0:
        break

    line = ""
    for i in range(1, row + 1):
        line += " " * (row - i)

        for k in range(i, 1, -1):
            line += str(k)

        for j in range(1, i + 1):
            line += str(j)

        print(line)
        line = ""