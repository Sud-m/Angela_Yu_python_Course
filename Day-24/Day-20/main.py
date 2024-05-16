from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("The official snake game of the century")
screen.tracer(0)
# setting screen event listeners
Snack = Snake()
# Snack.create()
food = Food()
score = Score()
screen.listen()
screen.onkey(Snack.up, "w")
screen.onkey(Snack.down, "s")
screen.onkey(Snack.left, "a")
screen.onkey(Snack.right, "d")
screen.onkey(screen.exitonclick, "space")
screen.update()
game_running = True
# move forward
while game_running:
    screen.update()
    time.sleep(0.1)
    Snack.move()
    
    #detect collision with food
    if Snack.head.distance(food) < 15:
        food.refresh()
        score.inc()
        Snack.extend()
    
    #detect collision
    if Snack.head.xcor() > 440 or Snack.head.xcor() < -420 or Snack.head.ycor() > 290 or Snack.head.ycor() < -290:
        score.reset()
        Snack.reset()
    # Detect tail collision
    # if the head collides with any segments in the tail then end the game
    for segment in Snack.SNAKE[1:]:
            if Snack.head.distance(segment) < 10:
                score.reset()
                Snack.reset()
   
    
screen.exitonclick()
