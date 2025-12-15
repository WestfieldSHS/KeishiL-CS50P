dollars = float(input("How much was the meal? "))
percent = int(input("What percentage would you like to tip? "))
tip = dollars * percent / 100
print(f"Leave ${tip:.2f}")
