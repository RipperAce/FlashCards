from cgitb import text
from tkinter import *
import pandas
import random
import time

#-----------------------------Literals----------------------------------------------
BACKGROUND_COLOR = "#B1DDC6"
word = ""
flip_timer = None
#-----------------------------Functions---------------------------------------------
def flash_word():
    global word, flip_timer
    screen.after_cancel(flip_timer)
    word = random.choice(french_list)
    canvas.itemconfig(title_word, text="French", fill="black")
    canvas.itemconfig(learn_word, text=f"{word}", fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)
    flip_timer = screen.after(3000, display_ans)

def display_ans():   
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(title_word, text="English", fill="white")
    canvas.itemconfig(learn_word, text=f"{data_dict[word]}", fill="white")
#------------------------------READ DATA--------------------------------------------
data = pandas.read_csv("./data/french_words.csv")
data_dict = {row.French: row.English for index, row in data.iterrows()}
french_list = [word for word in data_dict.keys()]
first_word = random.choice(french_list)
# data_new_dict = data.to_dict(orient="records")
# print(data_new_dict)
#------------------------------UI SETUP---------------------------------------------
screen = Tk()
screen.title("French Classes")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, display_ans)


front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_card_image)
title_word = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
learn_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, border=0, command=flash_word)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, border=0, command=flash_word)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

flash_word()

screen.mainloop()