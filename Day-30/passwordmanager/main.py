FONT_NAME = "Courier"
import tkinter
import tkinter.dialog
import tkinter.messagebox
import pyperclip
import json
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
    new_data = {
        web: {
            "email": email,
            "password": password
        }
    }
    
    if password == "" or email == "" or web == "":
        tkinter.messagebox.showinfo("Error", "There should be no empty fields!")
        return
    
    try: # Maybe file doesn't exist
        with open("Angela_Yu_python_Course_Git/Day-30/passwordmanager/passwords.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError: # If file doesn't exist and we need to create new json and store new dict
        with open("Angela_Yu_python_Course_Git/Day-30/passwordmanager/passwords.json", "w") as file:
            json.dump(new_data, file, indent = 4)
    else: # If file exists and we need to continue updating data
        # Updating old data with new data
        data.update(new_data)
            
        with open("Angela_Yu_python_Course_Git/Day-30/passwordmanager/passwords.json", "w") as file:
            # Saving updated data
            json.dump(data, file, indent = 4)
    finally: 
        webentry.delete(0, tkinter.END)
        passwordentry.delete(0, tkinter.END)

# ----------------------------- Search -------------------------------- #        
def search():
    website = webentry.get()
    try: 
        with open("Angela_Yu_python_Course_Git/Day-30/passwordmanager/passwords.json", "r") as file:
            data = json.load(file)
            print(data)
            if website in data:
                tkinter.messagebox.showinfo("Success", f"Password exists!\nEmail: {data[website]["email"]}\nPassword: {data[website]["password"]}")
                return
            else:
                tkinter.messagebox.showinfo("Uh Oh!", "Password doesn't exist :(")
    except FileNotFoundError:
        tkinter.messagebox.showinfo("Error", "No Data File Found")
        return
    finally:
        webentry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = tkinter.Canvas(width = 300, height = 300)
image = tkinter.PhotoImage(file = "Angela_Yu_python_Course_Git/Day-29/logo.png")
canvas.create_image(150, 100, image = image)
canvas.grid(column = 1, row = 0)

website = tkinter.Label(text = "Website: ")
website.grid(column = 0, row = 1)

email = tkinter.Label(text = "Email/Username: ")
email.grid(column = 0, row = 2)

password = tkinter.Label(text = "Password: ")
password.grid(column = 0, row = 3)

webentry = tkinter.Entry(width = 35)
webentry.grid(row = 1, column = 1)
webentry.focus()

emailentry = tkinter.Entry(width = 35)
emailentry.grid(row = 2, column = 1)
emailentry.insert(0, "sudhanvamasti@gmail.com")

passwordentry = tkinter.Entry(width = 21)
passwordentry.grid(row = 3, column = 1)

addbutton = tkinter.Button(text = "Add", width = 36, command = savepassword)
addbutton.grid(row = 4, column = 1, columnspan = 2)

generatebutton = tkinter.Button(text = "Generate Password", command = generaterandom)
generatebutton.grid(row = 3, column = 2)

searchbutton = tkinter.Button(text = "Search", command = search)
searchbutton.grid(row = 1, column = 2)


window.mainloop()
