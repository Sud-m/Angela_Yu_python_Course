from turtle import Turtle
# DID THIS MYSELF HAHA LESSGO WHO ARE YOU 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.CHANGE_X = 13.33
        self.CHANGE_Y = 10   
        self.ball_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.CHANGE_X
        new_y = self.ycor() + self.CHANGE_Y
        self.setpos(new_x, new_y)
        
        if new_y > 280 or new_y < -280:
            self.CHANGE_Y *= -1
            self.ball_speed *= 0.925
        