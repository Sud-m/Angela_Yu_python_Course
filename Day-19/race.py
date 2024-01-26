import random
from turtle import Turtle, Screen


def race():
    screen = Screen()

    screen.setup(width=1000, height=500)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    userguess = screen.textinput("Guess who will win!", "Which turtle do you think will win? Enter a color.")
    turtles = []
    race_winner = ""
    for i in range(7):
        timmy = Turtle(shape="turtle")
        timmy.speed(0)
        timmy.penup()
        timmy.goto(-500, -100 + i * 50)
        timmy.color(colors[i])
        turtles.append(timmy)

    race_over = False
    while not race_over:
        for turtle in turtles:
            turtle.forward(random.randint(0, 10))
            if turtle.xcor() > screen.window_width() / 2 - 20:
                race_over = True
                race_winner = turtle.color()[0]
    if race_winner == userguess:
        print(f"Yay! You guessed correctly, the {race_winner} turtle won!")
    else:
        print(f"RIP! You guessed incorrectly, the {race_winner} turtle won!")
    screen.exitonclick()


race()
