#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pw = ""

# for letter in range(nr_letters):
#     pw += letters[random.randint(0, len(letters) - 1)]
# for symbol in range(nr_symbols):
#     pw += symbols[random.randint(0, len(symbols) - 1)]
# for number in range(nr_numbers):
#     pw += numbers[random.randint(0, len(numbers) - 1)]

# print(pw)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

pw = ""
total_len = nr_letters + nr_symbols + nr_numbers

char_list = []

for letter in range(0, nr_letters):
    char_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    char_list.append(random.choice(symbols))

for number in range(0, nr_numbers):
    char_list.append(random.choice(numbers))

random.shuffle(char_list)

password = ""

for entry in char_list:
    password += entry

print(password)
