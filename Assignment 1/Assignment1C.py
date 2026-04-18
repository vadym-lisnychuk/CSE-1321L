print("[Time Conversion – Minutes to Days, Hours, and Minutes]")
minutes = float(input("Enter the total minutes: "))

days = int(minutes // 1440)
minutes -= 1440 * days

hours = int(minutes // 60)
minutes -= hours * 60


print(f"{minutes} minutes is approximately {days} day(s), {hours} hours, and {round(minutes, 2)} minutes.")