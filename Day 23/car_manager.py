from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def move(self):
        for x in self.all_cars:
            x.forward(self.car_speed)

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_y = random.choice(range(-250, 250))
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT