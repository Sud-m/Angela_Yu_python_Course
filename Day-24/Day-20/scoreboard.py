from turtle import Turtle
CENTER = "center"
FONT = ('arial', 15, 'normal')
class Score(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.highscore = self.get_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(x = 0, y = 275)
        self.update()

    def update(self):
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align = CENTER, font = FONT)
        
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(arg = "GAME OVER LOSER WOMP WOMP", align = CENTER, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()
    
    def get_highscore(self) -> int:
        with open("Course_Work/Day-24/Day-20/data.txt") as file:
            contents = file.read()
            return int(contents)
    
    def write_highscore(self):
        with open("Course_Work/Day-24/Day-20/data.txt", "w") as file:
            file.write(f"{self.highscore}")
    
    def inc(self):
        self.score += 1
        self.clear()
        self.update()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align = CENTER, font = FONT)
        