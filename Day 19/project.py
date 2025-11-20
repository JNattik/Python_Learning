from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(800, 500)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [125, 75, 25, -25, -75, -125]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    #tim.shape("turtle") --> both is possible
    new_turtle.penup()
    new_turtle.goto(x=-320, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_speed = random.randint(0, 10)
        turtle.forward(random_speed)

#tom = Turtle(shape="turtle")
#tom.color(colors[1])
#tom.penup()
#tom.goto(x=-320, y=75)

#ted = Turtle(shape="turtle")
#ted.color(colors[2])
#ted.penup()
#ted.goto(x=-320, y=25)

#teddy = Turtle(shape="turtle")
#teddy.color(colors[3])
#teddy.penup()
#teddy.goto(x=-320, y=-25)

#travis = Turtle(shape="turtle")
#travis.color(colors[4])
#travis.penup()
#travis.goto(x=-320, y=-75)

#t = Turtle(shape="turtle")
#t.color(colors[5])
#t.penup()
#t.goto(x=-320, y=-125)

screen.exitonclick()