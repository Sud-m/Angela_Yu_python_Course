import pandas as pd
data = pd.read_csv("Course_Work/Day-25/Squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240516.csv")



furcolor = data["Primary Fur Color"]
# for row in furcolor:
#     if row == "Gray":
#         newdict["Count"][0] += 1
#     elif row == "Cinnamon":
#         newdict["Count"][1] += 1
#     else:
#         newdict["Count"][2] += 1
        
# print(newdict["Count"])
# newdataframe = pd.DataFrame(newdict)
# newdataframe.to_csv("Course_Work/Day-25/Squirrel/squirrel_count.csv")


gray = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

newdict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count" : [len(gray), len(red), len(black)]
}

# newdict["Count"][0] = len(gray)
# newdict["Count"][1] = len(red)
# newdict["Count"][2] = len(black)

newdataframe = pd.DataFrame(newdict)
newdataframe.to_csv("Course_Work/Day-25/Squirrel/squirrel_count.csv")