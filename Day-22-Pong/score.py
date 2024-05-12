from turtle import Turtle
from typing import Any
FONT = ("Courier", 50, "normal")
CENTER = "center"
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.rightscore = 0
        self.leftscore = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftscore, align = CENTER, font = FONT)
        self.goto(100, 200)
        self.write(self.rightscore, align = CENTER, font = FONT)
        
    def updateright(self):
        self.rightscore += 1
        self.update_scoreboard()
        
    def updateleft(self):
        self.leftscore += 1
        self.update_scoreboard()