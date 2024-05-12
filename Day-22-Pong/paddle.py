from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, coor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.setpos(coor)
        
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 30)