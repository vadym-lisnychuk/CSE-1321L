row1 = input("Enter Bingo row 1 (3 values, comma-separated): ") + ","
row2 = input("Enter Bingo row 2 (3 values, comma-separated): ") + ","
row3 = input("Enter Bingo row 3 (3 values, comma-separated): ") + ","

temp_i = 0
for j in range(3):
    temp_s = ""
    for temp_i in range(temp_i, len(row1)):
        if row1[temp_i] == ",":
            temp_i += 1
            break
        else:
            temp_s += row1[temp_i]

    match j:
        case 0:
            A11 = int(temp_s)
        case 1:
            A12 = int(temp_s)
        case 2:
            A13 = int(temp_s)

temp_i = 0
for j in range(3):
    temp_s = ""
    for temp_i in range(temp_i, len(row2)):
        if row2[temp_i] == ",":
            temp_i += 1
            break
        else:
            temp_s += row2[temp_i]

    match j:
        case 0:
            A21 = int(temp_s)
        case 1:
            A22 = int(temp_s)
        case 2:
            A23 = int(temp_s)


temp_i = 0
for j in range(3):
    temp_s = ""
    for temp_i in range(temp_i, len(row3)):
        if row3[temp_i] == ",":
            temp_i += 1
            break
        else:
            temp_s += row3[temp_i]
    match j:
        case 0:
            A31 = int(temp_s)
        case 1:
            A32 = int(temp_s)
        case 2:
            A33 = int(temp_s)

print("B\tI\tN")
print(f"{A11}\t{A12}\t{A13}")
print(f"{A21}\t{A22}\t{A23}")
print(f"{A31}\t{A32}\t{A33}")

reasons = ""
# 1. The center position (row 2, column 2) must be 0.
valid = True
if A22 != 0:
    valid = False
    reasons += "- FREE space error: center (row 2, col 2) must be 0"
    reasons += "\n"

# 2. Each column must stay within its allowed range:
#       Column 1 (B): 1–15
#       Column 2 (I): 16–30
#       Column 3 (N): 31–45

if not (A11 >= 1 and A11 <= 15) or not (A21 >= 1 and A21 <= 15) or not (A31 >= 1 and A31 <= 15):
    valid = False
    reasons += "- Range error at row 1, column B: 18 (must be 1–15)"
    reasons += "\n"

if not (A12 >= 16 and A12 <= 30) or not (A22 >= 16 and A22 <= 30) or not (A32 >= 16 and A32 <= 30):
    valid = False
    reasons += "- Range error at row 2, column B: 18 (must be 1–15)"
    reasons += "\n"

if not (A13 >= 31 and A13 <= 45) or not (A23 >= 31 and A23 <= 45) or not (A33 >= 31 and A33 <= 45):
    valid = False
    reasons += "- Range error at row 3, column B: 18 (must be 1–15)"
    reasons += "\n"

# 3. In each row, the non-zero values must be different.
if A11 == A12 or A11 == A13 or A12 == A13:
    valid = False
    reasons += "- Duplicate in row 1\n"

if A21 == A22 or A21 == A23 or A22 == A23:
    valid = False
    reasons += "- Duplicate in row 2\n"

if A31 == A32 or A31 == A33 or A32 == A33:
    valid = False
    reasons += "- Duplicate in row 3\n"

if valid:
    print("VALID BINGO CARD")
else:
    print("INVALID BINGO CARD")
    print("Reasons:")
    print(reasons)