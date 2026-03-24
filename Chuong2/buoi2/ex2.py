isStudent = True
isHomeWork = False

print(type(isStudent))

# Kiểu danh sách
myList = ['Hello', '123', 'ABC']
print(type(myList))

# Kiểu
myTuple = (1,2,3,4,"ABC")
print(myTuple)

mySet = {1,2,3,3}
print(mySet)


myDict = {
    "name": "Huy",
    "age": "20",
    "score": [1,2,3]
}

print("student: ", myDict)

name = myDict["name"] + myDict["age"]
age = myDict["age"]
print(name)
print(age)

