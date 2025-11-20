from turtle import Turtle

STARTING_POINT_COORDINATES = [(350,0), (350,20), (350,40), (350,-20), (350, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)