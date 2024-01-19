import random
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)
screen = Screen()
timmy.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(circles):

    for i in range(circles):
        angle = 360 / circles
        timmy.pencolor(random_color())
        timmy.right(360 / circles)
        timmy.circle(150)
    screen.exitonclick()


draw_spirograph(20)
