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
game_images = {
    0: rock,
    1: paper,
    2: scissors
}
print("Welcome to Rock, Paper, Scissors!")
print("You will be playing against the computer. Here are the rules:")
print("Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.\n")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print("\nYou chose:")
print(game_images[user_choice])
time.sleep(1)
computer_choice = random.randint(0, 2)
print("Computer choice:")
time.sleep(1)
print(game_images[computer_choice])
result = (user_choice - computer_choice) % 3
print("\nResult:")
if result == 0:
    print("It's a draw!")
elif result == 1:
    print("You win!")
else:
    print("Computer wins!")