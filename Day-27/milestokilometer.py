from tkinter import *

def buttonclicked():
    label4.config(text = int(entry.get()) * 1.60934)

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width = 200, height = 150)
window.config(padx = 30, pady = 30)

label1 = Label()
label1.config(text = "\t")
label1.grid(column = 0, row = 0)

entry = Entry(width = 10)
inp = entry.get()
entry.grid(column = 1, row = 0)

label2 = Label()
label2.config(text = "Miles")
label2.grid(column = 2, row = 0)

label3 = Label()
label3.config(text = "is equal to")
label3.grid(column = 0, row = 1)

label4 = Label()
label4.grid(column = 1, row = 1)

label5 = Label()
label5.config(text = "Km")
label5.grid(column = 2, row = 1)

button = Button(text = "Calculate", command = buttonclicked)
button.grid(column = 1, row = 2)

window.mainloop()