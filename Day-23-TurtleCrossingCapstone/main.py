import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move, "w")
cars = CarManager()
cars.initialize()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(0, 10) == 1:
        cars.initialize()   
    cars.cars_move()
    
    if cars.checkcollision(player):
        score.gameover()
        break
    
    if player.check_level_passed():
        cars.levelup()
        score.level_up()   
screen.exitonclick()