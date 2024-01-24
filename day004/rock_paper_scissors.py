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

#Write your code below this line 👇
import random

options = [rock, paper, scissors]

user_choice = int(input("Choose your weapon! 0: rock, 1: paper, 2: scissors\n"))
print(options[user_choice])

comp_choice = random.randint(0,2)
print("Computer choice:\n" + options[comp_choice])

if user_choice == comp_choice:
    print("You draw!")
elif (user_choice + 1) % 3 == comp_choice:
    print("You lose!")
else:
     print("You win!")

