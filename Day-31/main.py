import tkinter
import tkinter.messagebox
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT1 = ("Ariel", 40, "italic")
FONT2 = ("Ariel", 60, "bold")
LANGUAGE = 0
try:
    WORDS = pd.read_csv(
        "Angela_Yu_python_Course_Git/Day-31/data/words_to_learn.csv"
    ).to_dict(orient="records")
except FileNotFoundError:
    WORDS = pd.read_csv(
        "Angela_Yu_python_Course_Git/Day-31/data/french_words.csv"
    ).to_dict(orient="records")
CURRWORD = {}


def getnewcard():
    global CURRWORD, FLIPITIMER
    window.after_cancel(FLIPITIMER)
    CURRWORD = random.choice(WORDS)
    canvas.itemconfig(canvasimage, image=frontimage)
    canvas.itemconfig(LANGUAGE, text="French", fill="black")
    canvas.itemconfig(WORD, text=CURRWORD["French"], fill="black")
    FLIPITIMER = window.after(3000, flipcards)
    WORDS.remove(CURRWORD)
    if len(WORDS) == 0:
        tkinter.messagebox.showinfo("Congrats", "You've mastered all words!")
        file_path = "Angela_Yu_python_Course_Git/Day-31/data/words_to_learn.csv"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
        exit(0)


def flipcards():
    canvas.itemconfig(canvasimage, image=backimage)
    canvas.itemconfig(LANGUAGE, text="English", fill="white")
    canvas.itemconfig(WORD, text=CURRWORD["English"], fill="white")


window = tkinter.Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
FLIPITIMER = window.after(3000, flipcards)


canvas = tkinter.Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
frontimage = tkinter.PhotoImage(
    file="Angela_Yu_python_Course_Git/Day-31/images/card_front.png"
)
backimage = tkinter.PhotoImage(
    file="Angela_Yu_python_Course_Git/Day-31/images/card_back.png"
)
canvasimage = canvas.create_image(400, 263, image=frontimage)
canvas.grid(column=0, row=0, columnspan=2)
LANGUAGE = canvas.create_text(400, 150, text="French", font=FONT1)
WORD = canvas.create_text(400, 263, text="trouve", font=FONT2)

wrongImage = tkinter.PhotoImage(
    file="Angela_Yu_python_Course_Git/Day-31/images/wrong.png"
)

wrongButton = tkinter.Button(image=wrongImage, highlightthickness=0, command=getnewcard)
wrongButton.grid(column=0, row=1)

rightImage = tkinter.PhotoImage(
    file="Angela_Yu_python_Course_Git/Day-31/images/right.png"
)
rightButton = tkinter.Button(image=rightImage, highlightthickness=0, command=getnewcard)
rightButton.grid(column=1, row=1)

getnewcard()
window.mainloop()

pd.DataFrame(WORDS).to_csv(
    "Angela_Yu_python_Course_Git/Day-31/data/words_to_learn.csv", index=False
)
