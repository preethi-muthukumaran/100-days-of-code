import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

pass_chars = []
for num in range(0, num_letters):
    index = random.randint(0, len(letters) - 1)
    pass_chars.append(letters[index])

for num in range(0, num_symbols):
    index = random.randint(0, len(symbols) - 1)
    pass_chars.append(symbols[index])

for num in range(0, num_numbers):
    index = random.randint(0, len(numbers) - 1)
    pass_chars.append(numbers[index])

#Shuffle all the eligible chars for our password
random.shuffle(pass_chars)

password = ""
password = password.join(pass_chars)

print("\nSuggested Password: \n")
print(password)