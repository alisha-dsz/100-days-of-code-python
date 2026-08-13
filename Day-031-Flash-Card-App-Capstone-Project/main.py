from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#--------------------------------------------Functionalities---------------------------------------#

random_dict_data = {}
data_dict ={}

# Tries to open words_to_learn.csv if it doesn't exist then opens french_words.csv
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')

# Generates a new card
def generate_card():
    global random_dict_data, flip_timer
    window.after_cancel(flip_timer)
    random_dict_data = random.choice(data_dict)
    french = list(random_dict_data.keys())[0]
    canvas.itemconfig(card_canvas, image=front_card)
    canvas.itemconfig(title, text=french, fill="black")
    canvas.itemconfig(word, text=random_dict_data[french], fill="black")
    flip_timer = window.after(3000, func=flip)

# Flips the card after 3 seconds
def flip():
    english = list(random_dict_data.keys())[1]
    canvas.itemconfig(card_canvas, image=back_card)
    canvas.itemconfig(title, text=english, fill="white")
    canvas.itemconfig(word, text=random_dict_data[english], fill="white")

# If you know the word then removes from the dictionary and stores the unknown ones in words_to_learn.csv
def is_known():
    global data_dict
    data_dict.remove(random_dict_data)
    df = pd.DataFrame(data_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    generate_card()

#-----------------------------------------------UI Layout------------------------------------------#

# Creates a window with background color and padding
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Setting flip timer
flip_timer = window.after(3000, func=flip)

# Creates canvas for the cards, title and words
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_canvas = canvas.create_image(400, 263, image=front_card)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creates a cross mark button using image
cross_mark = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_mark, command=generate_card)
cross_btn.grid(row=1, column=0)

# Creates a check mark button using image
check_mark = PhotoImage(file="images/right.png")
check_btn = Button(image=check_mark, command=is_known)
check_btn.grid(row=1, column=1)

# Calls the generate_card() function just are creating the UI
generate_card()

window.mainloop()