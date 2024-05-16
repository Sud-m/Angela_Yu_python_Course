import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-420, 420), random.randint(-280, 280))
        self.color(random.choice(COLORS))