import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0 
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global REPS, TIMER
    REPS = 0
    window.after_cancel(TIMER)
    label.config(text = "Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
    checks.config(text="")
    canvas.itemconfig(timertext, text = "00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():
    global REPS
    REPS += 1
    worksec = WORK_MIN * 60
    shortbreaksec = SHORT_BREAK_MIN * 60
    longbreaksec = LONG_BREAK_MIN * 60
    
    if REPS %8 == 0:
        label.config(text = "Long break", fg = RED, font = (FONT_NAME, 30, "bold"))
        countdown(longbreaksec)
    elif REPS % 2 == 0:
        label.config(text = "Short break", fg = PINK, font = (FONT_NAME, 30, "bold"))
        countdown(shortbreaksec)
    else:
        label.config(text = "Work", fg = GREEN, font = (FONT_NAME, 30, "bold"))
        countdown(worksec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global REPS, TIMER
    countmin = int(count / 60)
    countsec = count % 60
    canvas.itemconfig(timertext, text = f"{countmin}:{countsec:02d}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    else:
        starttimer()
        checks.config(text = ''.join(["✔\n" for i in range(int(REPS/2))]), font = (FONT_NAME, 15, "bold"))
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pommodoro tactic")
window.config(padx = 100, pady = 50, bg = YELLOW)


canvas = tkinter.Canvas(width = 250, height = 250, bg = YELLOW, highlightthickness = 0)
tomatoimage = tkinter.PhotoImage(file = "Angela_Yu_python_Course_Git/Day-28/tomato.png")
canvas.create_image(125, 125, image = tomatoimage)
canvas.grid(column = 1, row = 1)
timertext = canvas.create_text(125, 150, text = "00:00", fill = "white", font = (FONT_NAME, 30, "bold"))

label = tkinter.Label(text = "Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg = YELLOW)
label.grid(column = 1, row = 0)

startbutton = tkinter.Button(text = "Start", command = starttimer)
startbutton.grid(column = 0, row = 2)

resetbutton = tkinter.Button(text = "Reset", command = reset)
resetbutton.grid(column = 2, row = 2)

checks = tkinter.Label( fg = GREEN, bg = YELLOW, font = (FONT_NAME, 30, "bold"))
checks.grid(column = 1, row = 3)

window.mainloop()