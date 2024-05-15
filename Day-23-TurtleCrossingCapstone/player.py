STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setpos(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        
    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
        
    def check_level_passed(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False