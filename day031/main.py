from tkinter import *
import pandas as p
import random

BACKGROUND_COLOR = "#B1DDC6"
LAN_FONT = "Arial 40 italic"
WORD_FONT = "Ariel 64 bold"
timer = None
# ---------------- Process Data ---------------------

def read_words():
    try:
        data_df = p.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        data_df = p.read_csv("data/french_words.csv")

    data_dict = data_df.to_dict(orient="records")
    return data_dict


dictionary = read_words()
word = None

# ------------------ Pass/Fail function --------------------

def known_card():
    dictionary.remove(word)

    data = p.DataFrame(dictionary)
    data.to_csv("data/words_to_learn.csv", index=False)

    select_new_word()

def show_translation(word):
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=word["English"], fill="white")

def select_new_word():
    global timer, word
    if timer is not None:
        window.after_cancel(timer)
    word = random.choice(dictionary)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text=word["French"], fill="black")
    timer = window.after(3000, show_translation, word)

# ------------------- Create UI ----------------------
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy Flash Cards (Soooo flashy)")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=LAN_FONT)
card_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, command=known_card)
correct_button.grid(row=1, column=1)

false_img = PhotoImage(file="images/wrong.png")
false_button = Button(image=false_img, highlightthickness=0, command=select_new_word)
false_button.grid(row=1, column=0)

select_new_word()

window.mainloop()


