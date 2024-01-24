############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

def draw_player_cards(player_cards, dealer_cards, cards):
    """Adds cards to the players hand as long as they continue requesting them or the point limit is reached.
    Returns the player's cards as a list"""
    draw_flag = True

    while draw_flag:
        print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"\tDealer's first card is {dealer_cards[1]}")
        player_draw = input("Type 'y' to draw another card, type 'n' to pass: ")
        if (player_draw == "y"):
            player_cards.append(random.choice(cards))
            cards.remove(player_cards[-1])
            if sum(player_cards) <= 21 and 11 not in player_cards:
                continue
            elif sum(player_cards) > 21 and 11 in player_cards:
                player_cards[player_cards.index(11)] = 1
            else:
                draw_flag = False
        else:
            draw_flag = False
    return player_cards

def draw_dealer_cards(dealer_cards, cards):
    while sum(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))
        cards.remove(dealer_cards[-1])
    return dealer_cards

def check_outcome(player_cards, dealer_cards):
    """Checks the outcome of a black jack round based on two decks and prints the game results to the console"""

    print(f"\tYour final hand: {player_cards}, current score: {sum(player_cards)}")
    print(f"\tDealer's final hand: {dealer_cards}, current score: {sum(dealer_cards)}")

    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)

    if player_sum > dealer_sum and player_sum <= 21:
        print("Congratulations! You win!")
    elif player_sum == dealer_sum:
        print("You draw... against a machine... pathetic.")
    elif dealer_sum > player_sum:
        print("Dealer wins, you lose. Poor excuse of a player...")
    else:
        print("You went over... You lose. Better luck next time, Loser.")

def black_jack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4
    print(cards)
    player_cards = random.sample(cards, 2)
    for card in player_cards:
        cards.remove(card)
    dealer_cards = random.sample(cards, 2)
    for card in dealer_cards:
        cards.remove(card)

    player_cards = draw_player_cards(player_cards, dealer_cards, cards)
    dealer_cards = draw_dealer_cards(dealer_cards, cards)

    check_outcome(player_cards, dealer_cards)

    print("\n\nDo you want to play another round of Black Jack?")
    continue_game = input("Type 'y' for another game, 'n' to quit: ")
    if continue_game == "y":
        black_jack()
    return

black_jack()
