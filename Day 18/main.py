from turtle import Turtle, Screen
import heroes
import random
#from turtle import * --> you can skip the top, but at the same time you don't have to write all the time: timmy = turtle.Turtle()
#import turtle as t --> better than "import turtle", because it saves space: "timmy = t.Turtle()"

#timmy = turtle.Turtle() --> if you only write: import turtle --> is the better option, because then you can understand the code more easily
tim = Turtle()
tom = Turtle()
terry = Turtle()
tim.shape("turtle")
tim.color("green")

#for x in range(4):
    #tim.forward(100)
    #tim.left(90)

#for x in range(10): --> dotted line
   # tim.forward(10)
   # tim.penup()
   # tim.forward(10)
   # tim.pendown()

#print(heroes.gen()) --> if you want to access another package you usually have to "pip install" it --> then you have access to it

colors = ["dark blue", "pale green", "slate gray", "gold", "dark red", "pale violet red", "blue violet", "chocolate"]
cardinal_point = [90, 180, 270, 360]

def draw_shape(num_corners): #--> draw every shape between a triangle and a hectagon
    angle = 360 / num_corners
    for _ in range(num_corners):
       tim.forward(100)
       tim.right(angle)
#corners = [3, 4, 5, 6, 7, 8, 9, 10]
#for x in corners:
 #   tim.color(random.choice(colors))
  #  draw_shape(x)

def random_walk():
    global cardinal_point
    for _ in range(100):
        nesw = random.choice(cardinal_point)
        tim.pensize(10)
        tim.speed(5)
        tim.color(random_color())
        tim.right(nesw)
        tim.forward(25)

def random_color():
    r = random.randint(0, 255) / 255
    g = random.randint(0, 255) / 255
    b = random.randint(0, 255) / 255
    random_color = (r, g, b)
    return random_color

def spiral():
    tim.speed(0)
    for _ in range(100):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(3.6)

spiral()

screen = Screen()
screen.exitonclick()