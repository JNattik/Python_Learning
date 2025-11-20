from turtle import Turtle

FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=("Times New Roman", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Times New Roman", 35, "normal"))