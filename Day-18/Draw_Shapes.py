import random
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

timmy.shape("turtle")
timmy.fillcolor("SkyBlue")
colors = ["red", "green", "blue", "red", "black", "cyan", "hotpink", "gold", "navy", "magenta"]
timmy.speed(0)


def draw_shapes(sides):
    timmy.left(90)
    timmy.penup()
    timmy.forward(350)
    timmy.right(90)
    timmy.pendown()
    for i in range(3, sides + 1):
        timmy.color(random.choice(colors))
        angle = 360 / i
        for j in range(i):
            timmy.forward(50)
            timmy.right(angle)

    screen.exitonclick()




draw_shapes(30)
