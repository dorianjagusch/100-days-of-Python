import pandas as p

alphabet = p.read_csv("nato_phonetic_alphabet.csv")
alphabet_df = p.DataFrame(alphabet)

alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

to_translate = ""
while to_translate != "Q":
    to_translate = input("Enter a word: ").upper()

    result = [alphabet_dict[letter] for letter in to_translate if letter.isalpha()]
    print(result)
