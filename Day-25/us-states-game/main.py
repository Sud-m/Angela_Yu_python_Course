import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "Angela_Yu_python_Course_Git/Day-25/us-states-game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

turt = turtle.Turtle()
turt.hideturtle()
turt.penup()

data = pd.read_csv("Angela_Yu_python_Course_Git/Day-25/us-states-game/50_states.csv")

states = data["state"].to_list()
x_cords = data["x"].to_list()
y_cords = data["y"].to_list()
strikes = 0
statesgotten = 0
states_gotten = []
while True:
    answer = screen.textinput(title="Guess all 50 states!", prompt=f"You have {50 - statesgotten} state(s) left\nYou have {strikes} strike(s)").title()
    answer.strip()
    if answer in states_gotten:
        screen.textinput(title = "Already guessed!", prompt = "You already guessed that! Click enter and then guess another one!")
        continue
    if answer in states:
        xcor = data[data["state"] == answer]["x"].values[0]
        ycor = data[data["state"] == answer]["y"].values[0]
        turt.goto(xcor, ycor)
        turt.write(answer)
        statesgotten += 1
        states_gotten.append(answer)
    else:
        if answer == "Exit":
            break
        strikes += 1
        if strikes == 3:
            turt.goto(0, 0)
            turt.write("3 strikes, you're out!", align = "center")
            screen.exitonclick()
            break
        turt.goto(0, 0)
        screen.textinput(title = "Wrong!", prompt = f"Try again! Click enter to continue, you have {strikes} strike(s)")
    
    if statesgotten == 50:
        turt.goto(0, 0)
        turt.write("You won! You got all 50 states. ", font = ("Arial", 40, "normal"))
        screen.exitonclick()

notgotten = {"Missed States: If the entry is empty then you guessed correct": []}
# for state in states:
#     if state not in states_gotten:
#         notgotten["Missed States: If the entry is empty then you guessed correct"].append(state)
#     else:
#         notgotten["Missed States: If the entry is empty then you guessed correct"].append(" ")
 
notgotten["Missed States: If the entry is empty then you guessed correct"] = [state if state not in states_gotten else " " for state in states] 
        
newdataframe = pd.DataFrame(notgotten)
newdataframe.to_csv("Angela_Yu_python_Course_Git/Day-25/us-states-game/Missedstates.csv")