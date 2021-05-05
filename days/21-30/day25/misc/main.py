import pandas

# with open(r"days\21-30\day25\weather_data.csv") as file:
#     weather_data = file.readlines()

# print(weather_data)

# import csv 
# with open(r"days\21-30\day25\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         temperatures.append((row[1]))

#     print(temperatures)



# data = pandas.read_csv(r"days\21-30\day25\weather_data.csv")
# # print(data["condition"]) 
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(int(monday.temp)

# data_dict = {
#     "students": ['a', 'b', 'c'],
#     "scores": [12, 34, 54]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv(r"days\21-30\day25\random.csv")


data = pandas.read_csv(r"days\21-30\day25\Squirrel_Data.csv")

grey_fur = len(data[data["Primary Fur Color"] == "Gray"])
red_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

fur_dict = {
    "Fur Colour": [ "Gray", "Cinnomon", "Black"],
    "Count": [grey_fur, red_fur, black_fur]
}
sq_data = pandas.DataFrame(fur_dict)
sq_data.to_csv(r"days\21-30\day25\squirrel_count.csv")