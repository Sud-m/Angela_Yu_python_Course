import pandas as pd


# with open("Course_Work/Day-25/weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(weather)
    
import csv
with open("Course_Work/Day-25/weather_data.csv") as datafile:
    data = csv.reader(datafile)
    temperatures = []
    for row in data:
        # print(row)
        if row[1] == 'temp':
            continue
        temperatures.append(int(row[1]))
        
    # print(temperatures)

weather = pd.read_csv("Course_Work/Day-25/weather_data.csv")
print(type(weather))
print(type(weather['temp']))

# weather is a data frame, weather['temp'] is a series i.e. column
weatherdict = weather.to_dict()

print(weatherdict)

print(sum(weather["temp"].to_list()) / len(weather["temp"].to_list()))

print(weather.temp)

print(weather[weather.temp == weather.temp.max()])

monday = weather[weather.day == "Monday"]
mondaytemp = monday.temp
print(mondaytemp * 9 / 5 + 32)

# create dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 98]
}

newdata = pd.DataFrame(data_dict)
print(newdata)
newdata.to_csv("newdata.csv")