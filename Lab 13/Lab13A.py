# s = input("Enter temperatures for each day separated by space:\n")
from multiprocessing.reduction import steal_handle

s = "32 33 34 29 12 10 14 25 26 30 31 32 33"
data = [int(x) for x in s.split()]
heatwaves = 0   # > 30
cold_streak = 0 # < 15 consecutive
avg = round(sum(data) / len(data), 2)

heat_streak = 0
for x in data:
    if x > 30:
        heat_streak += 1
    else:
        heat_streak = 0

    if heat_streak == 3:
        heatwaves += 1
        heat_streak = 0

streak = 0
streaks = []
for x in data:
    if x < 15:
        streak += 1
    else:
        streaks.append(streak)
        streak = 0

cold_streak = max(streaks)


print(f"Number of heat waves: {heatwaves}")
print(f"Longest cold streak: {cold_streak} days")
print(f"Average temperature: {avg}°C")