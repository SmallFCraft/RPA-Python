# OOP Cơ bản
class Car:
    # thuộc tính 
    def __init__(self, name, style, speed, color):
        self.name = name
        self.style = style
        self.speed = speed
        self.color = color

    def get_name(self):
        return self.name
    
    # phương thức(hành động)
    def change_speed(self, speed):
        self.speed = speed
        return self.speed

    def change_color(self, color):
        self.color = color
        return self.color
    
obj_car = Car(name="VF7", style="Sport", speed=0, color='White')
print(obj_car)
print(obj_car.name)
print(obj_car.get_name())
print(obj_car.change_speed(100))
print(obj_car.change_color("Gray"))

obj_kia = Car(name="K3", style="Base", speed=0, color="Red")
print(obj_kia)
print(obj_kia.name)
print(obj_kia.change_speed(20))
print(obj_kia.change_color("Yellow"))

# print()

# Thêm thuộc tính màu và phương thức(hành động) thay đổi màu

# Kế thừa, đóng gói
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, salary):
        self.name = name
        # private
        self.__salary = salary
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calSalary(self):
        pass
    
class Employee(Person):
    def __init__(self, name, address, salary):
        # Kế thừa thuộc tính name từ lớp Cha(Person)
        super().__init__(name, salary)
        # tạo thuộc tính address cho Nhân viên
        self.address = address
        self.__salary = salary
    
    # kế thừa phương thức get_name từ lớp
    def get_name(self):
        return self.name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
        return self.__salary
    
    def calSalary(self):
        print("Tính lương cho nhân viên")
        salary = self.__salary = 5000000

class Developer(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, salary)
        self.address = address
        self.__salary = salary
    
    def calSalary(self):
        print("Tính lương cho Developer (+20%)")
        salary = self.__salary + self.__salary * 0.2
        return salary

class Manager(Person):
    def __init__(self, name, address, salary):
        super().__init__(name, salary)
        self.address = address
        self.__salary = salary
    
    def calSalary(self):
        print("Tính lương cho Manager (+30%)")
        salary = self.__salary + self.__salary * 0.3
        return salary



obj_person = Person(name="", salary=0)
print(obj_person)
print(obj_person.get_name())
# print(obj_person.__salary)
print(obj_person.get_salary())

obj_employee = Employee(name="An", address="566 Xô viết nghệ tĩnh", salary=1000000)
print(obj_employee)
print(obj_employee.get_name())
# print(obj_employee.__salary)
print(obj_employee.get_salary())
print(obj_employee.set_salary(2000000))

# Thay đổi lương cho nhân viên
print()