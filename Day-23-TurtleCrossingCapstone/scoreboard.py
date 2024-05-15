FONT = ("Courier", 24, "normal")
CENTER = "center"
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1  
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align = CENTER, font = FONT)
        
    def level_up(self):
        self.clear()
        self.goto(-200, 250)
        self.level += 1
        self.write(f"Level: {self.level}", align = CENTER, font = FONT)
        
    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game over!\nYou reached till level {self.level}.", align = CENTER, font = FONT)