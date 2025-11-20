import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract("C:\\Users\\YY992KW\\OneDrive - EY\\Documents\\Justin\\Privat\\Learning\\Programming\\Python_Learning\\hirst.jpg", 30)
#rgb_colors = []
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #rgb_colors.append(new_color)
#print(rgb_colors)
color_list = [(238, 237, 233), (237, 234, 238), (233, 235, 240), (215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), 
(163, 209, 197), (220, 177, 173), (14, 105, 56)]

tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.speed(10)

def random_color():
    random_choice = random.choice(range(30))
    r = color_list[random_choice][0] / 255
    g = color_list[random_choice][1] / 255
    b = color_list[random_choice][2] / 255    
    random_color = (r, g, b)
    return random_color

def painting():
    tim.right(135)
    tim.penup()
    tim.forward(350)
    tim.left(135)
    for _ in range(10):
        for _ in range(10):
            bullet_color = random_color()
            tim.pendown()
            tim.dot(20, bullet_color)
            tim.penup()
            tim.forward(50)
        tim.penup()
        tim.left(180)
        tim.forward(500)
        tim.right(90)
        tim.forward(50)
        tim.right(90)
        tim.pendown()
    
tim.hideturtle()
painting()

screen = Screen()
screen.exitonclick()