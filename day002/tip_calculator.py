print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
n_people = int(input("How many people to split the bill?"))

total = "{:.2f}".format(round(bill * (1 + (tip/100)) / n_people, 2))
print(f"Each person should pay: ${total}")