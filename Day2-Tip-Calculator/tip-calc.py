print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 20, or 30?"))/100
num_people = int(input("How many people will be splitting the bill?"))
cost_per_person = round( ((bill*(1 + percentage))/num_people), 2)
print(f"Each person should pay: ${cost_per_person}")