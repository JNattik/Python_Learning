import pandas

data = pandas.read_csv("./Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250307.csv")
gray_squirrels_count = len(data[data["Primary_Fur_Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary_Fur_Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary_Fur_Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Angela.csv")
