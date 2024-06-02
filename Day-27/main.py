from tkinter import *

def buttonclicked():
    mylabel.config(text = entry.get())
    
window = Tk()
window.title("First window")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)

mylabel = Label(text = "label", font = ('Arial', 24, 'bold'))
# mylabel["text"] = "New text" # or
mylabel.config(text = "New text", padx = 50, pady = 50)
mylabel.grid(column = 0, row = 0)
# Button
button = Button(text = "Click me", command = buttonclicked)
button.grid(column = 1, row = 1)
# New button
button2 = Button(text = "New Button")
button2.grid(column = 2, row = 0)
# Entry
entry = Entry(width = 10)
inp = entry.get()
entry.grid(column = 3, row = 2)
window.mainloop()
