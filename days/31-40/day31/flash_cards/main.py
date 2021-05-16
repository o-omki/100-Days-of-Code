import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card_chosen = {}
words_to_learn = []

def next_card():
    global card_chosen, card_timer
    window.after_cancel(card_timer)
    card_chosen = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text = "Korean", fill = "black")
    canvas.itemconfig(card_word, text = card_chosen["Korean"], fill = "black")
    canvas.itemconfig(card_background, image = card_front_image)
    card_timer = window.after(3000, func = flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = card_chosen["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_image)

def card_known():
    global words_to_learn
    words_to_learn.remove(card_chosen)
    data = pandas.DataFrame(words_to_learn)
    data.to_csv(r"days\31-40\day31\flash_cards\data\words_to_learn.csv", index = False)
    next_card()
    

try:
    data = pandas.read_csv(r"days\31-40\day31\flash_cards\data\words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"days\31-40\day31\flash_cards\data\ko_to_en_words.csv")
    words_to_learn = data.to_dict(orient = "records")
else:
    words_to_learn = data.to_dict(orient = "records")


window = tkinter.Tk()
window.title("Korean Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

card_timer = window.after(3000, func = flip_card)

canvas = tkinter.Canvas(width = 800, height = 526)
card_front_image = tkinter.PhotoImage(file = r"days\31-40\day31\flash_cards\data\images\card_front.png")
card_back_image = tkinter.PhotoImage(file = r"days\31-40\day31\flash_cards\data\images\card_back.png")
card_background = canvas.create_image(400, 263, image = card_front_image)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
card_title = canvas.create_text(400, 150, text = "Title", font = ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

cross_image = tkinter.PhotoImage(file = r"days\31-40\day31\flash_cards\data\images\wrong.png")
cross_button = tkinter.Button(image = cross_image, highlightthickness = 0, command = next_card)
cross_button.grid(row = 1, column = 0)

tick_image = tkinter.PhotoImage(file = r"days\31-40\day31\flash_cards\data\images\right.png")
tick_button = tkinter.Button(image = tick_image, highlightthickness = 0, command = card_known)
tick_button.grid(row = 1, column = 1)

next_card()


window.mainloop()
