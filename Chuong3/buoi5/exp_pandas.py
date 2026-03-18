import pandas

names = ["An", "Hòa", "Bình", "Tiến", "Nghĩa", "Huy"]
dataNames = pandas.Series(data = names, name = "Tên")
print(dataNames)

print("__________________________________________")

ages = ["18", "20", "19", "20", "21", "18"]
dataAges = pandas.Series(data = ages, name = "Tuổi")
print(dataAges)