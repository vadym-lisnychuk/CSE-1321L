REACTION_CONST = 1.47
BRAKE_CONST = 30
FRICTION_MULTIPLIER = 0.85

print("[Highway Stopping Distance Calculator]")

speed = float(input("Enter the speed (in mph): "))
t = float(input("Enter the reaction time (in seconds): "))
mu = float(input("Enter the road friction coefficient (mu): "))

friction_factor = FRICTION_MULTIPLIER * mu

D = (REACTION_CONST * speed * t) + ((speed * speed) / (BRAKE_CONST * friction_factor))
D = round(D, 2)

print(f"The estimated stopping distance is {D} feet.")