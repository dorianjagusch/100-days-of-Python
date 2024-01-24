from art import logo, vs
from game_data import data
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')


def retrieve_options():
    optione = random.sample(data, 2)
    return optione

def find_winner(options):
    if options[0]["follower_count"] > options[1]["follower_count"]:
        winner = "a"
    elif options[0]["follower_count"] == options[1]["follower_count"]:
        winner = ["a", "b"]
    else:
        winner = "b"
    return winner

def higher_lower(score):
    if score > 0:
        os.system('clear')
        print(f"Correct! Your current score: {score}")
    options = retrieve_options()
    print(logo)
    print(f"Option A: {options[0]['name']}: a {options[0]['description']}, from {options[0]['country']}")
    print(vs)
    print(f"Option B: {options[1]['name']}: a {options[1]['description']}, from {options[1]['country']}")
    winner = find_winner(options)
    choice = ""
    while choice != "a" and choice != "b":
        choice = input("Who has more followers? 'A' or 'B'?: ").lower()
    if choice in winner:
        higher_lower(score + 1)
    else:
        os.system('clear')
        print(f"You made the wrong choice. Next time, you {score}-point loser.")
    return

higher_lower(0)