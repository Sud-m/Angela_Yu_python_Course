from turtle import Turtle
CENTER = "center"
FONT = ('arial', 15, 'normal')
class Score(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x = 0, y = 275)
        self.update()

    def update(self):
        self.write(arg = f"Score = {self.score}", align = CENTER, font = FONT)
        
    def gameover(self):
        self.goto(0, 0)
        self.write(arg = "GAME OVER LOSER WOMP WOMP", align = CENTER, font = FONT)

        
    def inc(self):
        self.score += 1
        self.clear()
        self.update()