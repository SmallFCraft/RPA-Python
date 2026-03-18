class Car:
    # thuộc tính
    def __init__(self, name, style, speed, color):
        self.name = name
        self.style = style
        self.speed = speed
        self.color = color

    # phương thức

    def doiTocDo(self, speed):
        self.speed = speed
        return self.speed
    
    def doiMau(self, color):
        self.color = color
        return self.color
    

# obj_car = Car(name = "VF7", style="Sport", speed = 0, color="yellow")

# print("Xe: ", obj_car)
# print("Tên xe: ", obj_car.name)
# print("Loại xe: ", obj_car.style)
# print("Tốc độ: ", obj_car.speed+111)
# print("Màu xe: ", obj_car.doiMau("Xanh"))


class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def info(self):
        return self.name, self.address, self.phone
    
class Student(Person):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)



# obj_person = Person(name = "", address = '', phone='')
# print(obj_person.name)
# print(obj_person.address)
# print(obj_person.phone)
# obj_student = Student(name = 'Huy', address='12 Núi Thành', phone='123456')
# print(obj_student.name)
# print(obj_student.address)
# print(obj_student.phone)


class Employee(Person):
    def __init__(self, name, address, phone, baseSalary):
        super().__init__(name, address, phone, baseSalary)

    def getSalary(self):
        return self.__base_salary

obj_person = Person(name='', address='', )