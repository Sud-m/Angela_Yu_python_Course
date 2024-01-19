# import colorgram
#
# colors = colorgram.extract('Hirst_image.jpg', 100)
#
# # create new array with only RGB tuples, excluding first as it is likely background white
# rgb_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors][4:len(colors)]
#
# print(rgb_tuples)
import random
import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.speed(0)
timmy.pensize(10)
timmy.hideturtle()
colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
          (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
          (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
          (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56),
          (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]


def hirst_dots():
    timmy.penup()
    timmy.setpos(-250, -250)
    for i in range(10):
        timmy_position = timmy.position()
        for j in range(10):
            timmy.pendown()
            timmy.dot(20, random.choice(colors))
            timmy.penup()
            timmy.forward(50)
        timmy.setpos(timmy_position[0], timmy_position[1] + 50)
    screen.exitonclick()


hirst_dots()
