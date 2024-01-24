from art import logo
import os
os.system('cls' if os.name == 'nt' else 'clear')

players = {}
player_to_add = True

print(logo)


def find_max():
  highest_bidder = ""
  for player in players:
    current = players[player]
    if highest_bidder == "" or current > players[highest_bidder]:
      highest_bidder = player
  return highest_bidder

while player_to_add:
  name = input("What's your name?\n")
  bid = int(input("What's your bid? \n$"))
  players[name] = bid
  os.system('clear')
  if input("Would you like to add more players? 'yes' or 'no'\n") == "no":
    player_to_add = False

highest_bidder = find_max()
print(f"The winner is {highest_bidder} with a bid of ${players[highest_bidder]}")