import random
import hangman_art
import hangman_words
import os
os.system('cls' if os.name == 'nt' else 'clear')

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
guesses = []
lives = 6

print(hangman_art.logo)

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
        display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
                display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word and guess not in guesses:
        print("You guessed a wrong letter")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        else:
            print("You are one step closer to obliteration.")

    if guess not in guesses:
        guesses += guess
    else:
        print(f"You guessed {guess} previously. Be better!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
            end_of_game = True
            print("You win.")

    print(hangman_art.stages[lives])