from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"{self.score1}", align="center", font=("Times New Roman", 35, "normal"))
        self.goto(100, 200)
        self.write(f"{self.score2}", align="center", font=("Times New Roman", 35, "normal"))

    def increase_score_1(self):
        self.score1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_2(self):
        self.score2 += 1
        self.clear()
        self.update_scoreboard()