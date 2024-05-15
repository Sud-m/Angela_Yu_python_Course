COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS = []
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()

    def initialize(self):
        for i in range(-250, 280, 20):
            if random.randint(0, 50) % 9 == 1:
                self.create_turtle(i)  
         
    def create_turtle(self, ycor):
        self = Turtle()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_len = 2, stretch_wid = 1)
        self.penup()
        self.goto(300, ycor)
        CARS.append(self)
        
    def cars_move(self):
        for car in CARS:
            car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())
        
    def levelup(self):
        global STARTING_MOVE_DISTANCE   
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        
    def checkcollision(self, turt):
        for car in CARS:
            if turt.distance(car) < 30:
                return True
        return False