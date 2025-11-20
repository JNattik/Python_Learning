#with open(file = "./Day 25/weather_data.csv") as data_file:
    #data = data_file.readlines()
    #print(data)

#import csv

#with open(file = "./Day 25/weather_data.csv") as data_file:
 #   data = csv.reader(data_file)
  #  temperatures = []
   # for x in data:
    #    if x[1] != "temp":
     #       temperatures.append(int(x[1]))
    #print(temperatures)

import pandas

data = pandas.read_csv("./Day 25/weather_data.csv")
#print(data)

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()  #data["temp"] --> gives you the values of the columns were heading is temp. Other method would be: data.temp
#print(temp_list)
#print(data["temp"].mean())
max_temp = data["temp"].max()

#get data in row
#print(data[data.day == "Monday"])
#print(data[data.temp == max_temp])

#getting a specific value in one row
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32  #converting into farenheit

#create dataframe fromo scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_3 = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")