print("Welcome to the tip calculator!\n")
bill = input("What was the total bill? $")
bill = float(bill)
percentage = input("What percentage tip would you like to give? 10, 20, or 30?")
percentage = int(percentage)
percentage = percentage/100
num_people = input("How many people will be splitting the bill?")
num_people = int(num_people)
cost_per_person = (bill*(1 + percentage))/num_people
cost_per_person = round(cost_per_person, 2)
cost_per_person = str(cost_per_person)
print("Each person should pay: $" + cost_per_person)