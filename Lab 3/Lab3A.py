current_balance = float(input("Amount owed: $"))
apr = float(input("APR: "))


mpr = apr / 12
minimum_payment = current_balance * (mpr / 100)

print(f"Monthly percentage rate: {round(mpr, 3)}")
print(f"Minimum payment: ${round(minimum_payment, 2)}")