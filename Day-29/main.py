FONT_NAME = "Courier"
import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 20, pady = 20)

canvas = tkinter.Canvas(width = 200, height = 200)
image = tkinter.PhotoImage(file = "Angela_Yu_python_Course_Git/Day-29/logo.png")
canvas.create_image(100, 100, image = image)
canvas.grid(column = 1, row = 0)

website = tkinter.Label(text = "Website: ")
website.grid(column = 0, row = 1)

email = tkinter.Label(text = "Email/Username: ")
email.grid(column = 0, row = 2)

password = tkinter.Label(text = "Password: ")
password.grid(column = 0, row = 3)

webentry = tkinter.Entry(width = 35)
webentry.grid(row = 1, column = 1, columnspan = 2)

emailentry = tkinter.Entry(width = 35)
emailentry.grid(row = 2, column = 1, columnspan = 2)

passwordentry = tkinter.Entry(width = 21)
passwordentry.grid(row = 3, column = 1)

addbutton = tkinter.Button(text = "Add", width = 36)
addbutton.grid(row = 4, column = 1, columnspan = 2)

generatebutton = tkinter.Button(text = "Generate Password")
generatebutton.grid(row = 3, column = 2)

window.mainloop()