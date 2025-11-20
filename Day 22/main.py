from turtle import Turtle, Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

turtle = Turtle()
screen = Screen()
player1 = Player((350, 0))
player2 = Player((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong game.")
screen.tracer(0)

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.change_direction()

    if ball.distance(player1) < 60 and ball.xcor() > 320 or ball.distance(player2) < 60 and ball.xcor() < -320:
        ball.change_direction_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_1()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_2()

screen.exitonclick()