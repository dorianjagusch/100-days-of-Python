#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

solution = random.randint(1, 100)

def user_pick_difficulty():
    difficulty = ""
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("Choose a difficulty. Type 'hard' or 'easy':\n")
        if difficulty == "hard":
            lives = 5
        elif difficulty == "easy":
            lives = 10
        else:
            continue
    print(f"You have {lives} attempts.")
    return lives

def evaluate_guess(guess):
    """Evaluates the guess in comparison to the solution,
    lowers number of lives and returns boolean whether
    game was won (False= or not (True))"""
    if guess == solution:
        print("You guessed correctly! Congrats!")
        return (False)
    elif guess < solution:
        print("Your guess was too low.")
    else:
        print("Your guess was too high.")
    global lives
    lives -= 1
    return (True)


lives = user_pick_difficulty()
guess= int(input("Guess a number between 1 and 100 (inclusive): "))

game_running = True
while game_running:
    game_running = evaluate_guess(guess)
    if lives == 0:
        print("You ran out of lives. Better luck next time!")
        break
    elif game_running:
        print(f"You have {lives} attempts remaining.")
        guess = int(input("Guess again: "))