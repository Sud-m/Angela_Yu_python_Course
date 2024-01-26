from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed(0)


def forward():
    timmy.forward(15)


def backward():
    timmy.back(15)


def c_clock():
    timmy.setheading(timmy.heading() - 10)


def clock():
    timmy.setheading(timmy.heading() + 10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def etch_a_sketch():
    screen.listen()
    screen.onkey(key="w", fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="a", fun=clock)
    screen.onkey(key="d", fun=c_clock)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()


etch_a_sketch()
