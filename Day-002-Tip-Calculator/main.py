print("Welcome to the Tip Calculator")
bill=float(input("What was the total bill? $"))
tip_percentage=float(input("How much tip would you like to give? 10, 12, or 15? "))
split=float(input("How many people to split the bill? "))
tip=(bill*(tip_percentage/100)+bill)/split
tip=round(tip,2)
print(f"Each person should pay: ${tip}")