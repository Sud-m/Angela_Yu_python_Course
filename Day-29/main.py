FONT_NAME = "Courier"
import tkinter
import tkinter.dialog
import tkinter.messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generaterandom():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password = []
    password.extend([random.choice(letters) for i in range(random.randint(8, 10))])
    password.extend([random.choice(symbols) for i in range(random.randint(2, 4))])
    password.extend([random.choice(numbers) for i in range(random.randint(2, 4))])
    random.shuffle(password)
    pyperclip.copy("".join(password))
    passwordentry.delete(0, tkinter.END)
    passwordentry.insert(0, "".join(password))
    tkinter.messagebox.showinfo("Password Generated", "Random password has been copied to the clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def savepassword():
    web = webentry.get()
    email = emailentry.get()
    password = passwordentry.get()
    if password == "" or email == "" or web == "":
        tkinter.messagebox.showinfo("Error", "There should be no empty fields!")
        return
    with open("Angela_Yu_python_Course_Git/Day-29/passwords.txt", "a") as file:
        file.write(f"{web} | {email} | {password}\n")
        webentry.delete(0, tkinter.END)
        passwordentry.delete(0, tkinter.END)
        tkinter.messagebox.showinfo("Password Added", "Your new password has been saved!")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

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
webentry.focus()

emailentry = tkinter.Entry(width = 35)
emailentry.grid(row = 2, column = 1, columnspan = 2)
emailentry.insert(0, "sudhanvamasti@gmail.com")

passwordentry = tkinter.Entry(width = 21)
passwordentry.grid(row = 3, column = 1)

addbutton = tkinter.Button(text = "Add", width = 36, command = savepassword)
addbutton.grid(row = 4, column = 1, columnspan = 2)

generatebutton = tkinter.Button(text = "Generate Password", command = generaterandom)
generatebutton.grid(row = 3, column = 2)

window.mainloop()
