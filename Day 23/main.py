import time, random
from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_cars()
    carmanager.move()

    for x in carmanager.all_cars:
        if x.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.increase_score()
        carmanager.increase_speed()

screen.exitonclick()