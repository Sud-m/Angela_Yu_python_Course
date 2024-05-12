from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time
CENTER = "center"
FONT = ('arial', 15, 'normal')
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong better than you could imagine.")

paddle1 = Paddle((375, 0))
paddle2 = Paddle((-375, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")
while True:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)    
    #detection with paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() > 340) or (ball.distance(paddle2) < 50 and ball.xcor() < -340):
        if ball.CHANGE_X < 0:
            scoreboard.updateleft()
        else:
            scoreboard.updateright()
        ball.CHANGE_X *= -1
        continue
    if ball.xcor() > 380 or ball.xcor() < -380:
        a = ball.xcor() > 380
        ball.goto(0, 0)
        if a:
            ball.write(arg = "Left player wins! Right player you are trash.", align = CENTER, font = FONT)
        else:
            ball.write(arg = "Right player wins! Left player you are stupid.", align = CENTER, font = FONT)
            
        break
screen.exitonclick()
