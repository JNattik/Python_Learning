from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
