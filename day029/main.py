from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + number_list + symbol_list

    random.shuffle(password_list)

    password = "".join(password_list)

    window.clipboard_clear()
    window.clipboard_append(password)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_entries():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops!", message="Please fill out all the fields!")
        return

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open("data.json", "w") as f:
            json.dump(new_data, f, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    website_input.delete(0, END)
    password_input.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def search_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No datafile found")
        return

    if website == "":
        messagebox.showinfo(title="Error", message=f"Please provide a service to search for")
        return

    if website not in data:
        messagebox.showinfo(title=website, message=f"No data saved for {website}")
        return

    messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                        f"Password: {data[website]['password']}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white", justify="left")
website_label.grid(row=1, column=0)

website_input = Entry(width=21, bg="white", justify="left")
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", bg="white", justify="right", command=search_password, width=12)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", bg="white", justify="left")
email_label.grid(row=2, column=0)

email_input = Entry(width=35, bg="white", justify="left")
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "dorian@gmail.com")

password_label = Label(text="Password", bg="white", justify="left")
password_label.grid(row=3, column=0)

password_input = Entry(width=21, bg="white", justify="left")
password_input.grid(row=3, column=1)

gen_pw_button = Button(text="Generate Password", bg="white", command=generate_password, justify="right")
gen_pw_button.grid(row=3, column=2)

add_pw_button = Button(text="Add", width=36, bg="white", command=add_entries)
add_pw_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
