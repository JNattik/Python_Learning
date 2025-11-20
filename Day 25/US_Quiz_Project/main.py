import turtle
import pandas
from scoreboard import Scoreboard

data = pandas.read_csv("./Day 25/US_Quiz_Project/50_states.csv")
screen = turtle.Screen()
screen.title("U.S: States Game")

scoreboard = Scoreboard()

image = "./Day 25/US_Quiz_Project/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#def get_mouse_click_coor(x, y):
    #print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

state_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Score: {scoreboard.score}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [z for z in state_list if z not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missed_states.csv")
        break
    for x in state_list:
        if answer_state == x:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(state_data.x.item(), state_data.y.item())
            t.pendown()
            t.write(x)
            scoreboard.increase_score()

turtle.mainloop()