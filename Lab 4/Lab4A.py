grade = float(input("Enter your grade: "))
#97

if grade > 97:
    letter = "A+"
elif grade > 94:
    letter = "A"
elif grade > 91:
    letter = "A-"
elif grade > 88:
    letter = "B+"
elif grade > 85:
    letter = "B"
elif grade > 82:
    letter = "B-"
elif grade > 79:
    letter = "C+"
elif grade > 76:
    letter = "C"
elif grade > 73:
    letter = "C-"
elif grade > 70:
    letter = "D+"
elif grade > 67:
    letter = "D"
elif grade > 64:
    letter = "D-"
else:
    letter = "F"

print(f"Letter grade is: {letter}")