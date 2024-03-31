from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.SNAKE = []
        self.create()
        self.head = self.SNAKE[0]
    
    def create(self):
        for i in STARTING_POSITIONS:  
            self.addsegment(i)
            
    def extend(self):
        self.addsegment(self.SNAKE[-1].position())
        
    def addsegment(self, position):
        timmy = Turtle(shape="square")
        timmy.penup()
        timmy.color("white")
        timmy.goto(position)
        self.SNAKE.append(timmy)
    
    def move(self):
        for i in range(len(self.SNAKE) - 1, 0, -1):
            self.SNAKE[i].goto(self.SNAKE[i-1].pos()) 
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    