import random
import time
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = ["ROCK", "PAPER", "SCISSORS"]
options_drawing = [rock, paper, scissors]
print("Welcome to Rock, Paper, Scissors!\n")
print("""Remember, these are your options:\n
0 for Rock
1 for Paper 
2 for Scissors\n""")
time.sleep(2)
print("On shoot, type your number!\n")
time.sleep(2)
print("Rock")
time.sleep(1)
print("Paper")
time.sleep(1)
print("Scissors")
time.sleep(3)
print("SHOOT!\n")
user_choice = int(input("Quick, which option do you choose 0 - Rock, 1 - Paper, 2 - Scissors:\n"))

time.sleep(2)
computer_choice = random.randint(0, 2)

result = "Error. Try Again"
#Win or lose check:
if user_choice == computer_choice:
    result = "Draw"
elif user_choice > computer_choice:
    result = "Win"
elif user_choice < computer_choice:
    result = "Lose"
else:
    result = "Error. Try Again"
    exit(0)

print(f"You chose, {options[user_choice]}!")
print(f"{options_drawing[user_choice]}\n")
print(f"The computer chose, {options[computer_choice]}!")
print(f"{options_drawing[computer_choice]}\n")

print(f"The result of the game is: You {result}!")
print("\nThank you for playing. Hope to see you soon.")
exit(0)