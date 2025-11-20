import pandas
import csv

data = pandas.read_csv("./Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250307.csv")
color_1_list = data["Primary_Fur_Color"].to_list()
Gray = []
Cinnamon = []
Black = []

for x in color_1_list:
    if x == "Gray":
        Gray.append(x)
    elif x == "Cinnamon":
        Cinnamon.append(x)
    else:
        Black.append(x)

number_gray = len(Gray)
number_cinnamon = len(Cinnamon)
number_black = len(Black)

data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [number_gray, number_cinnamon, number_black]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Fur_Color.csv")