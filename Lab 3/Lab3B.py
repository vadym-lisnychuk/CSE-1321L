quality_points = 0
total_hours = 0

for i in range(1, 5):
    hours = int(input(f"Course {i} hours: "))
    grade = int(input(f"Grade for course {i}: "))
    quality_points += hours * grade 
    total_hours += hours

print(f"Total hours: {total_hours}")
print(f"Total quality points: {quality_points}")
print(f"Your GPA for this semester is {round(quality_points / total_hours, 2)}")

