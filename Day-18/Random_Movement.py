import random
import turtle

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed(0)
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def random_movement():
    timmy.pensize(7)
    while True:
        timmy.pencolor(random_color())
        timmy.forward(25)
        timmy.setheading(90 * random.randint(0, 3))


random_movement()
