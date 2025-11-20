import csv, pandas, json, random, tkinter, time

FONT_NAME = "Courier"
BG = "#B1DDC6"

#-----------------------------------------Draw Card-------------------------------------------------

try:
    csv_file = pandas.read_csv('./Day 31/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('./Day 31/spanish_words.csv')
    spanish_dict = original_data.to_dict(orient="records")
else:
    spanish_dict = csv_file.to_dict(orient="records")
random_card = {}

def wr_next_card():
    global random_card, flip_timer

    window.after_cancel(flip_timer)
    random_card = random.choice(spanish_dict)
    canvas.itemconfig(flashy_text_1, text="Spanish", fill="black")
    canvas.itemconfig(flashy_text_2, text=random_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=photoimage)
    flip_timer = window.after(5000, func=flip_card)

def cr_next_card():
    global random_card, flip_timer

    spanish_dict.remove(random_card)
    data = pandas.DataFrame(spanish_dict)
    data.to_csv("./Day 31/words_to_learn.csv", index=False)
    flip_timer = window.after(5000, func=flip_card)

    wr_next_card()

def flip_card():
    global random_card
    canvas.itemconfig(card_background, image=card_back_ig)
    canvas.itemconfig(flashy_text_1, text="English", fill="white")
    canvas.itemconfig(flashy_text_2, text=random_card["English"], fill="white")

#--------------------------------------------GUI-------------------------------------------------

window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BG, padx=50, pady=50)

flip_timer = window.after(5000, func=flip_card)

canvas = tkinter.Canvas(height=526, width=800, highlightthickness=0)
photoimage = tkinter.PhotoImage(file="./Day 31/images/card_front.png")
card_back_ig = tkinter.PhotoImage(file="./Day 31/images/card_back.png")
card_background = canvas.create_image((400, 263), image=photoimage)
flashy_text_1 = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, "20", "italic"))
flashy_text_2 = canvas.create_text(400, 250, text="", fill="black", font=(FONT_NAME, "40", "bold"))
canvas.config(bg=BG, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=50)
wr_next_card()

wrong_image = tkinter.PhotoImage(file="./Day 31/images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=wr_next_card)
wrong_button.grid(row=1, column=0, padx=50, pady=50)

right_image = tkinter.PhotoImage(file="./Day 31/images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=cr_next_card)
right_button.grid(row=1, column=1, padx=50, pady=50)




window.mainloop()